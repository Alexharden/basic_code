from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
import time

#自動下載及安裝webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() #視窗大化
#連線到 LeetCode登入頁面
driver.get("https://worker.myviewboard.cloud/")
# driver.implicitly_wait(40)
time.sleep(6)
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys("admin")
password = driver.find_element(By.XPATH,"//input[@placeholder='密碼']")
password.send_keys("12345")
login = driver.find_element(By.CLASS_NAME,"btn.btn-primary.px-4")
login.send_keys(Keys.ENTER)
time.sleep(15)
driver.close()