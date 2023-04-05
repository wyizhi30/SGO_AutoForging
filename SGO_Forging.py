#pip install selenium
#pip install playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from playsound import playsound
import time
import re

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://swordgale.online/")
time.sleep(3)
#==================登入==================
email=driver.find_element(By.ID, "e")
email.send_keys(input("請輸入電子信箱:"))    #鍵盤輸入
# email.send_keys("your@gmail.com")          #記住信箱

password=driver.find_element(By.ID, "p")
password.send_keys(input("請輸入密碼:"))    #鍵盤輸入
# password.send_keys("your password")        #記住密碼

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
equip_input = input("請輸入武器類型:")       #鍵盤輸入
# equip = "短刀"
for i in range(2,len(equip_type)):    
    if(equip_input in equip_type[i].text):
        equip_type[i].click()
        equip_args = re.findall(r"\d+", equip_type[i].text)    #獲取鍛造時間及材料上限，後面判斷會用到
        print(equip_type[i].text)
        print("--------")
        break
# 後續新增輸入錯誤反應
time.sleep(1)

#==================輸入裝備名稱==================
name = driver.find_element(By.CLASS_NAME, "chakra-input.css-1p7h7cr")
name.send_keys(input("請輸入裝備名稱:"))    #鍵盤輸入
# name.send_key("機械煎包飛升")
time.sleep(1)

#==================輸入素材及數量==================
material_list = driver.find_elements(By.CLASS_NAME, "css-1kt2y43")    #素材列表

user_list = []
for i in range(int(input("材料上限%s，請問要使用幾種素材? " %equip_args[1]))):
        material_input = input("請輸入第%d種素材(ex:兔皮 5) :" % (i+1))
        user_list.append(material_input.split()[0])
        user_list.append(material_input.split()[1])

#==================開始自動執行==================
while(1):                 #重複直到程式錯誤，無窮迴圈，之後再訂條件
    
    #==================選取素材==================
    for u in range(0, len(user_list), 2):
        for m in range(len(material_list)):
            if(material_list[m].text == user_list[u]):
                for i in range(int(user_list[u+1])):
                    material_list[m].click()
                    print(user_list[u])
    time.sleep(1)
    # 增加輸入判斷及庫存量判斷

    #==================開始鍛造==================
    start_forging = driver.find_element(By.CLASS_NAME, "chakra-button.css-9xrim4")
    start_forging.click()
    print("等待時間%s分鐘，foring......" %equip_args[0])
    time.sleep(1)

    #==================鍛造完成==================
    move = driver.find_element(By.TAG_NAME, "body")
    move.send_keys(Keys.HOME)
    time.sleep(int(equip_args[0]) * 60 + 10)         #鍛造等待時間隨武器參數變動
    done = driver.find_element(By.CLASS_NAME, "chakra-button.css-1zb9ui")      #完成鍛造
    done.click()
    print("Done!\n-------")
    time.sleep(2)

# playsound("G5SH - (Let Go Of Yourself) ft. Marz23 Official Visualizer.m4a")  #鍛造結束撥放提示音樂
time.sleep(2)
driver.quit()



# 有空再來加圖形化介面
# driver.find_elements() 記得加s