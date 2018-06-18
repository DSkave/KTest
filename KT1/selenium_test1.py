from selenium import webdriver
import datetime
import sys

class Jra_Scraping:
    #url = "http://www.jra.go.jp"
    def __init__(self):
      self.url = "http://www.jra.go.jp"
      self.driver = webdriver.Chrome()

    def Odds_Get(self,place,day,race_no):
       #取得文字列から日付情報を抜き出す
       print('test')

if __name__ == "__main__":
    #driver = webdriver.Chrome()
    #driver.get(Jra_Scraping.url)
    scp = Jra_Scraping()
    scp.driver.get(scp.url)
    scp.driver.execute_script("doAction('/JRADB/accessO.html','pw15oli00/6D')")
    element = scp.driver.find_element_by_class_name('kaisaiDay1')
    #1:開催日チェック
    if(u'6月16日' in element.text):
        print(element.text)
    else:
        print("指定の開催日オッズは取得できませんでした")
        sys.exit()

    #2:開催場所チェック
    place_link = scp.driver.find_element_by_partial_link_text('3回東京5日')
    place_link.click()

    #scp.driver.execute_script("doAction('/JRADB/accessO.html','pw15orl10052018030520180616/3A')")
    #3:レース番号チェック
    race_no_link = scp.driver.find_element_by_xpath("//td[@class='raceNo']/a/img[@alt='2R']")
    race_no_link.click()