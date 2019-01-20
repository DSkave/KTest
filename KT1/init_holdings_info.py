from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time,re,os,sys,unicodedata

class Keiba_Scraping:

    def __init__(self):
        self.options = ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(os.path.abspath('chromedriver'),chrome_options=self.options)
        self.url = "http://www.jra.go.jp/"

    def KaisaiData_Get(self,year):
        print("引数チェック:",year)
        print("JRA開催情報取得開始")

        kaisaiinfo_link = scp.driver.find_element_by_xpath("//li[@id='q_menu2']/a/img[@alt='レーシングカレンダー']")
        kaisaiinfo_link.click()
        tmp_cal=[]
        tmp_dic={}
        tmp_y=""
        tmp_m=""
        tmp_d=""
        #開催カレンダーページ
        try:
          #カレント年情報取得
          get_calyear = scp.driver.find_elements_by_xpath("//div[contains(@class,'cal_year')]/ul/li")
          for i in range(len(get_calyear)):
           if(year in get_calyear[i].text):
              print("JRA Webサイトに%s年のカレンダーデータがあることを確認" %year)
              tmp_y=year
              get_calyear[i].click()
              #clickの後に再度エレメントの取得は必要かもしれない
              break
           else:
              print("%sは入力データと一致しません" %get_calyear[i].text)
              if i == len(get_calyear)-1:
                print("入力データ[year:%s]は情報がないかサイト構成が変わっている可能性があります" %year)
                print("プログラム又はサイト構成を見直して下さい")
                exit()

          #月情報取得
          get_calmonth = scp.driver.find_elements_by_xpath("//div[contains(@class,'month')]/ul/li")
          for i in range(len(get_calmonth)):
              get_calmonth[i].click()
              get_calmonth = scp.driver.find_elements_by_xpath("//div[contains(@class,'month')]/ul/li")
              print(get_calmonth[i].text)
              tmp_m = re.sub(r'\D','',get_calmonth[i].text)
              tmp_m = unicodedata.normalize('NFKC',tmp_m)

              #day情報取得
              get_calday = scp.driver.find_elements_by_xpath("//td[contains(@class,'kaisai')]")
              for j in range(len(get_calday)):
                 # print(get_calday[j].text)
                  get_day=get_calday[j].find_element(By.TAG_NAME,"span")
                  get_keibajou = get_calday[j].find_elements(By.CLASS_NAME,"rc")
                  tmp_d = get_day.text
                  for k in range(len(get_keibajou)//2):
                      print(get_keibajou[k].text)
                      tmp_dic={'kaisaibi':year+'-'+ tmp_m + '-' + tmp_d,
                               'keibajou':get_keibajou[k].text
                              }
                      tmp_cal.append(tmp_dic)


          print("リストに入れたカレンダー一括表示出来るか？")
          for i in range(len(tmp_cal)):
              print(tmp_cal[i])
          #開催情報取得
          # テーブル内容取得
          tableElem = scp.driver.find_element_by_class_name("rc_table")
          kaisaiinfo = tableElem.find_elements_by_xpath("//td[contains(@class,'kaisai')]")
          for i in range(len(kaisaiinfo)):
           print(kaisaiinfo[i].text)

          trs = tableElem.find_elements(By.TAG_NAME, "tr")

          # ヘッダ行は除いて取得
          for i in range(1, len(trs)):
              tds = trs[i].find_elements(By.TAG_NAME, "td")
              line = ""
              for j in range(0, len(tds)):
                  if j < len(tds) - 1:
                      line += "%s\t" % (tds[j].text)
                  else:
                      line += "%s" % (tds[j].text)
              #print(line + "\r\n")
        except SyntaxError as e:
          print(e)
        except TypeError:
          print('SEX!!')
        finally:
          scp.driver.quit()

if __name__ == "__main__":

     scp = Keiba_Scraping()
     scp.driver.get(scp.url)
     scp.driver.implicitly_wait(10)
     scp.KaisaiData_Get("2019")

