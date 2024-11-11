import os.path
from sys import executable, exception
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

# Go to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

# Login to the dashboard
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys("Admin")

password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys("admin123")

login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.submit()
time.sleep(5)

# Navigate to the created employee in test1.py script
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/275")
time.sleep(2)

# Fill in driver's license and its expiry date
drivers_license_nr = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
drivers_license_nr.send_keys("123456")

driver_licence_exp = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
driver_licence_exp.send_keys("2026-11-11")

# Select Nationality
nationality_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
nationality_dropdown.click()
time.sleep(1)

# Wait for and loop through options to select "Lithuanian"
nationality_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in nationality_options:
    if option.text.strip() == "Lithuanian":
        option.click()
        break
time.sleep(1)

# Select Marital status
marital_status_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
marital_status_dropdown.click()
time.sleep(1)

# Wait for and loop through options to select "Married"
marital_status_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in marital_status_options:
    if option.text.strip() == "Married":
        option.click()
        break
time.sleep(1)

# Date of birth
dob = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')
dob.send_keys("1992-11-11")

# Gender
gender = driver.find_element(By.XPATH, '//label[normalize-space()="Male"]')
gender.click()

# Save info
save_personal_details_btn = driver.find_element(By.XPATH, '//div[@class="orangehrm-horizontal-padding orangehrm-vertical-padding"]//button[@type="submit"][normalize-space()="Save"]')
save_personal_details_btn.submit()

