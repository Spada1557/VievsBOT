import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userAgentRandomizer import userAgents
print("Введите количество просмотров:")
count = int(input())
index = 0
print("Введите ULR:")
url_ = input()

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options = options)

while index < count + 1:
 driver.get(url_)
 time.sleep(5)
 driver.delete_all_cookies()
 driver.execute_script("window.scrollTo(0, -250);")
 if index == 0:
  print("Пробная прогонка...")
  index = index + 1
 else:
  print(index)
  index = index + 1
