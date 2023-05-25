import selenium, os, time, datetime, random, warnings, sys
from os import system #for windows
clear = lambda: system('cls')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from os import system
import re
from webdriver_manager.chrome import ChromeDriverManager

def validate_text(regex,inp):
	if not re.match(regex,inp):
		return False
	return True

print("Enter Your Email : " , end="")
email = input()
while not(validate_text(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)):
        system("clear")
        print("Invalid Email")
        print("Enter Email Again")
        email = input()
system('clear')

print("Enter Your Password : " , end="")
psswd= input()
system('clear')    

print("Enter Meeting Code Without Any Special-Character : " , end="")
code = input()
while not(validate_text(r"^[a-zA-Z0-9]*$",code)):
        system("clear")
        print("Invalid GMeet Code, Try Again")
        print("Without Special Character")
        code = input()
system('clear')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
start_time = input()
while not(validate_text(r"\d\d:\d\d:\d\d",start_time)):
        system("clear")
        print("Enter In Correct Format [ HH:MM:SS ] ")
        print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
        start_time = input()
print("Time to end the class ")
end_time = input()
while not(validate_text(r"\d\d:\d\d:\d\d",end_time)):
        system("clear")
        print("Enter In Correct Format [ HH:MM:SS ] ")
        print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
        end_time = input()



while current_time != (start_time):
    system("clear")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time , " , Start at : " , start_time)
    sleep(1)

if current_time == (start_time):
    path = "chromedriver.exe"
    opt = Options()

    opt.add_argument("start-maximized")

    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1 
    })
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
    driver.get("https://meet.google.com/new")
    
    #Email Passed
   # search = driver.find_element("name","identifier")
    #search.send_keys(email)
    #search.send_keys(Keys.RETURN)
    #driver.implicitly_wait(5)
    #password Passed 
    #searc = driver.find_element("id","password")
    #driver.implicitly_wait(5)
    #print(search)
    #searc.send_keys(psswd)
    #searc.send_keys(Keys.RETURN)
    
    driver.find_element("xpath",'//input[@type="email"]').send_keys(email)
    driver.find_element("xpath",'//*[@id="identifierNext"]').click()
    sleep(3)
    driver.find_element("xpath",'//input[@type="password"]').send_keys(psswd)
    driver.find_element("xpath",'//*[@id="passwordNext"]').click()

    sleep(3)
    driver.get("https://meet.google.com/lookup/" + code)
    sleep(3)
    
    for i in range(6):
    
     try:
     # sleep(8)
      #turn_off_mic_action = ActionChains(driver)
      #turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
      #turn_off_camera_action = ActionChains(driver)
      #turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
      #sleep(1)
      #driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
      #sleep(20)
      WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))

      sleep(2)
      turn_off_mic_action = ActionChains(driver)
      turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
      turn_off_camera_action = ActionChains(driver)
      turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
      print("Sucessfully found landmark...turned off camera and microphone.")
      
    
     except selenium.common.exceptions.TimeoutException:
        try:
            WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Ask to join')]")))

            sleep(2)
            turn_off_mic_action = ActionChains(driver)
            turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
            turn_off_camera_action = ActionChains(driver)
            turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
            print("Sucessfully found landmark...turned off camera and microphone.")
            break
        except selenium.common.exceptions.TimeoutException:
            print("[ERROR]: Attempting to find landmark...")
            if USE_FAILSAFE_PERCAUTIONS: time.sleep(6)
            else: driver.implicitly_wait(6)

    

     if current_time == end_time:
        driver.find_element_by_css_selector('div.VfPpkd.Bz112c.LgbsSe.yHy1rc.eT1oJ.tWDL4c.jh0Tpd.Gt6sbf.QQrMi.ftJPW').click()
        system("clear")
        print("Left Meet")
        driver.close()

    try:
     join_button = WebDriverWait(driver, 36).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))
     driver.execute_script("arguments[0].click();", join_button)
    except selenium.common.exceptions.TimeoutException:
     try:
        join_button = WebDriverWait(driver, 36).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Ask to join')]")))
        driver.execute_script("arguments[0].click();", join_button)
     except selenium.common.exceptions.TimeoutException:
        print("Couldn't join Google Meet. Are you sure you have the right code?")
