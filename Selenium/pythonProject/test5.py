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

# Get Predefined Report page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/definePredefinedReport")
time.sleep(3)

# Report name
report_name = driver.find_element(By.XPATH, '//input[@placeholder="Type here ..."]')
report_name.send_keys("TEST REPORT")
time.sleep(2)

# Select Criteria
criteria_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
criteria_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Employee Name"
criteria_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in criteria_options:
    if option.text.strip() == "Employee Name":
        option.click()
        break
time.sleep(2)

# Add another CRITERIA
add_another_criteria_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]')
add_another_criteria_btn.click()
time.sleep(2)

criteria_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
criteria_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Gender"
criteria_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in criteria_options:
    if option.text.strip() == "Gender":
        option.click()
        break
time.sleep(2)

add_another_criteria_btn2 = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]')
add_another_criteria_btn2.click()
time.sleep(2)