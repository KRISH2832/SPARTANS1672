from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import undetected_chromedriver as uc

options = uc.ChromeOptions() 
options.headless = False

# chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = uc.Chrome(options=options) 
driver.get("https://spartans-uidai.netlify.app/")

# driver = webdriver.Chrome(options=chrome_options)


# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "container"))
# )

import time
time.sleep(5)

# put "krish" in input tag with id="name"
name_input = driver.find_element(By.ID, "name")
name_input.send_keys("krish")

number_input = driver.find_element(By.ID, "mobile")
number_input.send_keys("8287735005")

email_input = driver.find_element(By.ID, "email")
email_input.send_keys("krishsharma0413@gmail.com")


# time.sleep(5)
# label tag with class "cb-lb" has an input checkbox as children click it
# checkbox = driver.find_element(By.CLASS_NAME, "cb-lb")
# # find checkbox child input tag
# checkbox = checkbox.find_element(By.TAG_NAME, "input")
# # click the checkbox
# checkbox.click()

time.sleep(5)
# press submit button
submit_button = driver.find_element(By.ID, "send-otp")
submit_button.click()

time.sleep(10)


# with open("website.html", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)