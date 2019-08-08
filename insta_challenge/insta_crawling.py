from selenium import webdriver
import time
import dados_user

chrome_path = r"C:\Users\londo\Documents\psafe_challenge\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)

driver.find_element_by_name("username").send_keys(dados_user.username)
driver.find_element_by_name("password").send_keys(dados_user.password)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
time.sleep(3)

driver.find_element_by_xpath('//div[3]/div/div/div[3]/button[2]').click

#Trocar ahlexpaes pelo seu nome de usuario
driver.get("https://www.instagram.com/ahlexpaes/followers")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(2)

followers_list = driver.find_elements_by_tag_name('li')

#follower = [0]
for follower in followers_list:
    print(follower)

time.sleep(3)

#Trocar ahlexpaes pelo seu nome de usuario
driver.get("https://www.instagram.com/ahlexpaes/following")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(2)

following_list = driver.find_elements_by_tag_name('li')

for follow in following_list:
    print(follower)


