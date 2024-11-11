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

# Go to Add candidate page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
time.sleep(2)

# Fill in candidate information
first_name = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]')
first_name.send_keys("Billie")
time.sleep(1)

last_name = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/input[1]')
last_name.send_keys("Eilish")
time.sleep(1)

# Select Nationality
vacancy_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
vacancy_dropdown.click()
time.sleep(1)

# Wait for and loop through options to select "Software Engineer"
vacancy_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in vacancy_options:
    if option.text.strip() == "Software Engineer":
        option.click()
        break
time.sleep(1)

email_input = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]')
email_input.send_keys("billie.eilish@gmail.com")
time.sleep(1)

contact_nr_input = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/input[1]')
contact_nr_input.send_keys("869754312")
time.sleep(1)

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

keywords_input = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')
keywords_input.send_keys("Singer, Model, Young")
time.sleep(1)

date_application = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]')
date_application.send_keys(Keys.CONTROL + "a")
time.sleep(1)
date_application.send_keys(Keys.DELETE)
time.sleep(1)
date_application.send_keys("2024-11-11")
time.sleep(1)

notes_input = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[2]/textarea[1]')
notes_input.send_keys("Motivated and willing to go!")
time.sleep(1)

candidate_save_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[8]/button[2]')
candidate_save_btn.submit()
time.sleep(6)

# After creating the candidate
shortlist_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/button[2]')
shortlist_btn.click()
time.sleep(4)

notes_shortlist_field = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/textarea[1]')
notes_shortlist_field.send_keys("Seems nice IDK.")
time.sleep(2)

shortlist_save_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]')
shortlist_save_btn.submit()
time.sleep(5)

# Shedule interview
shedule_interview_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/div[2]/button[2]')
shedule_interview_btn.click()
time.sleep(5)

interview_title_input = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]')
interview_title_input.send_keys("Billie")
time.sleep(2)

current_admin_name = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p').text
interviewer_field_input = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')
interviewer_field_input.send_keys(current_admin_name)
time.sleep(5)
interviewer_field_input.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
interviewer_field_input.send_keys(Keys.ENTER)
time.sleep(3)

schedule_date = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/input[1]')
schedule_date.send_keys("2024-12-11") # galimai reikes pakeisti per pristatyma
time.sleep(2)

schedule_time = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/input[1]')
schedule_time.click()
time.sleep(2)

schedule_notes = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[5]/div[1]/div[2]/textarea[1]')
schedule_notes.send_keys("Very excited to finally meet Billie EILISIH!")
time.sleep(2)

schedule_save_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]')
schedule_save_btn.submit()
time.sleep(5)