from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#Put Your EA Credentials
email = "metalika_expo@hotmail.com"
password = "C0p0@k123"

#Player to find
findPlayer = "Gabriel Martinelli"
#max price to buy now
maxPriceBuyNow = "1100"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#Go to login
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
#Wait the loading stuff
time.sleep(20)
#Click Login
driver.find_elements(By.XPATH, "/html/body/main/div/div/div/button[1]")[0].click()
#Type email
driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/div/form/div[1]/div[1]/div[1]/div/div[1]/input")[0].send_keys(email)
#Type Password
driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/div/form/div[1]/div[2]/input")[0].send_keys(password)
#Send Login Form
driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/section/div/form/div[6]/a")[0].click()
#Click Send Verification Code
driver.find_elements(By.XPATH, "/html/body/div/form/div/section/a[2]")[0].click()
#Enter Verification code to continue with the script
code = input("Enter Code: ")
#Type Verification code
driver.find_elements(By.XPATH, "/html/body/div[1]/form/div/section/div[2]/div/input")[0].send_keys(code)
#Send Verification Code
driver.find_elements(By.XPATH, "/html/body/div[1]/form/div/section/div[5]/a")[0].click()

#Wait Loading stuff
time.sleep(30)

#Click Transfer Button
driver.find_elements(By.XPATH, "/html/body/main/section/nav/button[3]")[0].click()
#Click Search The transfer Market
driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div[2]")[0].click()
time.sleep(1)

#Search for the player
driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input")[0].send_keys(findPlayer)
time.sleep(1)

#Click the name (if not this search dont work)
driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button")[0].click()
time.sleep(1)

#Type the max price buy now
driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")[0].send_keys(maxPriceBuyNow)
time.sleep(1)

#Click Search Button
driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")[0].click()
time.sleep(10)

#Always be true and stop manually when the coins gone xd
while 1<2:
    try:
        #Button Buy Now
        driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")[0].click()
        time.sleep(1)
        #Click Ok
        driver.find_elements(By.XPATH,"/html/body/div[4]/section/div/div/button[1]")[0].click()
        time.sleep(1)
        #Go Back to search
        driver.find_elements(By.XPATH,"/html/body/main/section/section/div[1]/button[1]")[0].click()
        time.sleep(1)
        #Ad number in bid price(if not the script don't work)
        driver.find_elements(By.XPATH,"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]")[0].click()
        time.sleep(1)
        # Click Search Button
        driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")[0].click()
        time.sleep(2)
        continue

    except:
        # Go Back to search
        driver.find_elements(By.XPATH, "/html/body/main/section/section/div[1]/button[1]")[0].click()
        time.sleep(1)
        # Ad number in bid price(if not the script don't work)
        driver.find_elements(By.XPATH,"/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]")[0].click()
        time.sleep(1)
        # Click Search Button
        driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")[0].click()
        time.sleep(2)
        continue






