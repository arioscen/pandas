from selenium import webdriver
import time
import datetime
from dateutil import parser
import os

driver = webdriver.Chrome()

#set start time
ssday = '2017-01-01'
sday = parser.parse(ssday)
today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
eday = today - 2*delta

def get_csv():
    while True:
        try:
            action = driver.find_elements_by_css_selector(".widget-actions-menu.ic_googleplus_reshare.ng-isolate-scope")
            action[1].click()
            csv = driver.find_elements_by_css_selector(".widget-actions-item.ng-scope.ng-isolate-scope")
            csv[5].click()
            break
        except IndexError:
            time.sleep(0.1)

while sday < eday:
    tA = sday.strftime('%Y-%m-%d')
    sday += delta
    tB = sday.strftime('%Y-%m-%d')
    url = "https://trends.google.com.tw/trends/explore?date=" + tA + "%20" + tB +"&geo=TW"
    driver.get(url)
    time.sleep(1)
    get_csv()
    while True:
        try:
	    #set download path and target path
            from_path = "/home/ubuntu/Downloads/"
            to_path = "/home/ubuntu/google_trends/"
            for filename in os.listdir(from_path):
                if filename.endswith(".csv"):
                    os.rename(from_path + filename, to_path + tA + ".csv")
            break
        except FileNotFoundError:
            time.sleep(0.1)
