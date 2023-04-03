#pip install selenium
#pip install playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from playsound import playsound
import time

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://swordgale.online/")

#==================登入==================
email=driver.find_element(By.ID, "e")
# email.send_keys(input("請輸入電子信箱:"))    #鍵盤輸入
email.send_keys("wyizhi30@gmail.com")

password=driver.find_element(By.ID, "p")
# password.send_keys(input("請輸入密碼:"))    #鍵盤輸入
password.send_keys("tpjh0410403") 

SignIn=driver.find_element(By.CLASS_NAME, "chakra-button")
time.sleep(1)
SignIn.click()
time.sleep(3)

#==================鍛造==================
forging = driver.find_elements(By.CLASS_NAME, "chakra-link.css-1dho2qc")[3]
forging.click()
time.sleep(2)

#==================選擇裝備類型==================
equip_type = driver.find_elements(By.CLASS_NAME, "css-0")
print("--------")
# equip = input("請輸入武器類型:")       #鍵盤輸入
equip = "短刀"
for i in range(2,len(equip_type)):    
    if(equip in equip_type[i].text):
        equip_type[i].click()
        print(equip_type[i].text)
        print("--------")
        break
time.sleep(2)
#==================輸入裝備名稱==================
name = driver.find_element(By.CLASS_NAME, "chakra-input.css-1p7h7cr")
# name.send_keys(input("請輸入裝備名稱:"))    #鍵盤輸入
name.send_key("煎包機械飛升")
time.sleep(3)

while(1):      #重複直到程式錯誤，無窮迴圈，之後再訂條件
    #==================選擇素材==================
    rabbit_fur = driver.find_element(By.CLASS_NAME, "css-104kv8y")  #選擇標記為紫色的素材
    for i in range(10):
        print(rabbit_fur.text)              #目前10個兔皮，可優化成輸入自訂素材
        rabbit_fur.click()
    time.sleep(2)

    #==================開始鍛造==================
    start_forging = driver.find_element(By.CLASS_NAME, "chakra-button.css-9xrim4")
    start_forging.click()
    print("foring......")
    time.sleep(3)

    #==================鍛造完成==================
    move = driver.find_element(By.TAG_NAME, "body")
    move.send_keys(Keys.HOME)
    time.sleep(450)         #7分鐘後點擊完成鍛造，更換不同武器要改時間
    done = driver.find_element(By.CLASS_NAME, "chakra-button.css-1zb9ui")
    done.click()
    print("Done!\n-------")
    time.sleep(2)

playsound("G5SH - (Let Go Of Yourself) ft. Marz23 Official Visualizer.m4a")  #鍛造結束撥放提示音樂
time.sleep(2)
driver.quit()