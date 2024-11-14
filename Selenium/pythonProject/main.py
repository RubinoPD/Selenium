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

def add_criteria(cname):
    # Select Criteria
    criteria_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
    )
    criteria_dropdown.click()
    time.sleep(2)

    # Wait for and loop through options to select name
    criteria_options = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
    )
    for option in criteria_options:
        if option.text.strip() == cname:
            option.click()
            break
    time.sleep(2)
    add_criteria_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]')
    add_criteria_btn.click()

# Add Criteria
add_criteria("Employee Name")
add_criteria("Gender")

# Delete Criteria
delete_1_criteria_btn = driver.find_element(By.XPATH, '//div[@class="oxd-form-row"]//div[3]//button[1]//i[1]')
delete_1_criteria_btn.click()
time.sleep(2)

delete_2_criteria_btn = driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-trash-fill"]')
delete_2_criteria_btn.click()
time.sleep(2)

# Select Include
criteria_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]'))
)
criteria_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Current And Past Employees"
criteria_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in criteria_options:
    if option.text.strip() == "Current and Past Employees":
        option.click()
        break
time.sleep(2)

# Select Display field group
display_field_grp_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
display_field_grp_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Personal"
display_field_dropdown_grp_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in display_field_dropdown_grp_options:
    if option.text.strip() == "Personal":
        option.click()
        break
time.sleep(2)

# Select Display Field
display_field_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
display_field_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Employee First Name"
display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in display_field_dropdown_options:
    if option.text.strip() == "Employee First Name":
        option.click()
        break
time.sleep(2)

# Add field button
add_display_field_btn = driver.find_element(By.XPATH, '//div[@class="oxd-form-row"]//div[2]//div[2]//div[2]//button[1]//i[1]')
add_display_field_btn.click()
time.sleep(2)

# Enable include header
include_header_enable = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[5]/div[1]/label[1]/span[1]')
include_header_enable.click()
time.sleep(2)

# Add Employee ID
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Employee Id":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Last Name
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Employee Last Name":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Date of Birth
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Date of Birth":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Date of Birth
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Gender":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Select Contact Details GROUP
display_field_grp_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Contact Details"
display_field_dropdown_grp_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in display_field_dropdown_grp_options:
    if option.text.strip() == "Contact Details":
        option.click()
        break
time.sleep(2)

# Add Address
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Address":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Mobile
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Mobile":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Work Email
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Work Email":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Enable header
include_header_enable = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[8]/div[1]/label[1]/span[1]')
include_header_enable.click()
time.sleep(2)

# Select Contact Details GROUP
display_field_grp_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Emergency Contacts"
display_field_dropdown_grp_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in display_field_dropdown_grp_options:
    if option.text.strip() == "Emergency Contacts":
        option.click()
        break
time.sleep(2)

# Add Name
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Name":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Home Telephone
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Home Telephone":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Work Telephone
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Work Telephone":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Relationship
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Relationship":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Enable header
include_header_enable = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[11]/div[1]/label[1]/span[1]')
include_header_enable.click()
time.sleep(2)

# Select Contact Details GROUP
display_field_grp_dropdown.click()
time.sleep(2)

# Wait for and loop through options to select "Languages"
display_field_dropdown_grp_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in display_field_dropdown_grp_options:
    if option.text.strip() == "Languages":
        option.click()
        break
time.sleep(2)

# Add Language
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Language":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Competency
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Competency":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Comments
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Comments":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Add Fluency
display_field_dropdown.click()
time.sleep(2)

display_field_dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)

for option in display_field_dropdown_options:
    if option.text.strip() == "Fluency":
        option.click()
        break
time.sleep(2)

add_display_field_btn.click()
time.sleep(2)

# Enable header
include_header_enable = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[14]/div[1]/label[1]/span[1]')
include_header_enable.click()
time.sleep(2)

# Delete 3 display field rows
delete_field_button = driver.find_element(By.XPATH, '//span[normalize-space()="Employee Id"]//i[@class="oxd-icon bi-x --clear"]')
delete_field_button.click()
time.sleep(2)

delete_field_button = driver.find_element(By.XPATH, '//span[normalize-space()="Relationship"]//i[@class="oxd-icon bi-x --clear"]')
delete_field_button.click()
time.sleep(2)

delete_field_button = driver.find_element(By.XPATH, '//span[normalize-space()="Fluency"]//i[@class="oxd-icon bi-x --clear"]')
delete_field_button.click()
time.sleep(2)

# Delete whole GROUP
delete_whole_group = driver.find_element(By.XPATH, '//div[6]//button[1]//i[1]')
delete_whole_group.click()
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

add_another_criteria_btn.click()
time.sleep(2)

# Add name to criteria Employee Name
employee_name_field = driver.find_element(By.XPATH, '//input[@placeholder="Type for hints..."]')
employee_name_field.send_keys("Bobert Perdolia")
time.sleep(2)
employee_name_field.send_keys(Keys.ARROW_DOWN + Keys.ENTER)
time.sleep(2)

# Select Gender
gender_select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]'))
)
gender_select.click()
time.sleep(2)

# Wait for and loop through options to select "Male"
gender_select_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
for option in gender_select_options:
    if option.text.strip() == "Male":
        option.click()
        break
time.sleep(2)

# Save report
save_report_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
save_report_btn.submit()
time.sleep(2)

print("Task 5 is done!")