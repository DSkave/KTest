from selenium import webdriver
import datetime

class Jra_Scraping:
    #url = "http://www.jra.go.jp"
    def __init__(self):
      self.url = "http://www.jra.go.jp"
      self.driver = webdriver.Chrome()

    def Odds_Get():
       print('test')

if __name__ == "__main__":
    #driver = webdriver.Chrome()
    #driver.get(Jra_Scraping.url)
    scp = Jra_Scraping()
    scp.driver.get(scp.url)
    scp.driver.execute_script("doAction('/JRADB/accessO.html','pw15oli00/6D')")
    element = scp.driver.find_element_by_class_name('kaisaiDay1')
    print(element.text)