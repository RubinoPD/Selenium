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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/253")
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
time.sleep(1)

# Gender
gender = driver.find_element(By.XPATH, '//label[normalize-space()="Male"]')
gender.click()
time.sleep(1)

# Save info
save_personal_details_btn = driver.find_element(By.XPATH, '//div[@class="orangehrm-horizontal-padding orangehrm-vertical-padding"]//button[@type="submit"][normalize-space()="Save"]')
save_personal_details_btn.submit()
time.sleep(3)

# Custom fields for blood type and test_field with save button
blood_type_dropdown = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]')
time.sleep(2)
blood_type_dropdown.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
blood_type_dropdown.send_keys(Keys.ENTER)
time.sleep(1)

test_field = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]')
test_field.send_keys("TEST")
time.sleep(1)

custom_fields_save_btn = driver.find_element(By.XPATH, '//div[@class="orangehrm-custom-fields"]//button[@type="submit"][normalize-space()="Save"]')
custom_fields_save_btn.submit()
time.sleep(3)

# Attachments
add_button = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/button[1]')
add_button.click()
time.sleep(2)

file_path = os.path.abspath("C:/Users/RK/Desktop/Projects/Selenium/CV.txt")

# Attempt to upload file
try:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    upload_field = driver.find_element(By.XPATH, '//input[@type="file"]')
    upload_field.send_keys(file_path)
    print("File uploaded successfully")

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")

except Exception as upload_error:
    print(f"Error uploading image: {upload_error}")

time.sleep(2)

comment_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/textarea[1]'))
)
comment_field.send_keys("This is my CV!!!")
time.sleep(1)

save_attachment_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/button[2]')
save_attachment_btn.submit()
time.sleep(5)

# File edit/download/remove
attachment_edit_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[8]/div[1]/button[1]/i[1]')
attachment_edit_btn.click()
time.sleep(3)

edit_comment = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/textarea[1]')
time.sleep(2)
edit_comment.send_keys(Keys.CONTROL + "a")
time.sleep(1)
edit_comment.send_keys(Keys.DELETE)
time.sleep(2)
edit_comment.send_keys("This is edited comment!!!")
time.sleep(2)

save_edit_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[4]/button[2]')
save_edit_btn.submit()
time.sleep(5)

