# selenium 自動化網頁操作
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()

driver.get("https://swordgale.online/")
element=driver.find_element(By.ID, "e")
element.send_keys("wyizhi30@gmail.com")
element=driver.find_element(By.ID, "p")
element.send_keys("tpjh0410403")
SignIn=driver.find_element(By.CLASS_NAME, "chakra-button")
time.sleep(1)
SignIn.click()
time.sleep(5)

hunt = driver.find_element(By.CLASS_NAME, "chakra-link.css-1dho2qc")             #狩獵
hunt.click()
time.sleep(5)
battle = driver.find_elements(By.CLASS_NAME, "chakra-button.css-14jkdoz")[1]         #戰鬥
print(battle.text)

HP = driver.find_elements(By.CLASS_NAME, "css-newptn")[0]                        #血量
stamina = driver.find_elements(By.CLASS_NAME, "css-newptn")[1]                   #體力
state = driver.find_elements(By.CLASS_NAME, "css-newptn")[2]                     #狀態(地區)
Durability = driver.find_elements(By.CLASS_NAME, "css-7sfvbv")[1]                #耐久度
First_town = driver.find_elements(By.CLASS_NAME, "chakra-button.css-5g06p")[0]   #初始城鎮
prairie = driver.find_elements(By.CLASS_NAME, "chakra-button.css-5g06p")[1]      #大草原

# item = driver.find_elements(By.CLASS_NAME, "chakra-link css-1dho2qc")[1]
# hight_switch = driver.find_elements(By.CLASS_NAME, "chakra-switch__thumb css-7roig")[1]
# equipments = driver.find_elements(By.ID, "table0-equipments")

count = 0
print(HP.text)
print(stamina.text)
print(Durability.text)
print(state.text)
while((int)(HP.text[3:6])>300 and (int)(stamina.text[2:5])>200 and (int)(Durability.text)>25):
    print(HP.text)
    print(stamina.text)
    print(Durability.text)
    print(state.text)
    print("--------------")
    
    # if((int)(Durability.text)<25):
    #     item.click()
    #     hight_switch.click()
    #     item.click()

    if(state.text == "狀態：閒置（大草原 10）"):
        First_town.click()
        time.sleep(330)
        driver.find_elements(By.CLASS_NAME, "chakra-button css-1adux0m").click()  #點擊完成移動
        prairie.click()
        time.sleep(330)
    battle.click()
    time.sleep(11)
    
    count += 1
print("總共戰鬥{}次". format(count))

driver.quit()

# driver = webdriver.Chrome()
# driver.quit()

###driver.find_elements()[1]  有多個同名元素時要用elements，反之用element