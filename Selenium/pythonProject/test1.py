import os.path
from sys import executable, exception

from selenium import webdriver
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


try:

    # 1: Go to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    # 2: Login to the dashboard
    username_field = driver.find_element(By.NAME, 'username')
    username_field.send_keys("Admin")

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys("admin123")

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.submit()
    time.sleep(5)

    # 3: Navigate to Add Employee page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
    time.sleep(2)

    # 4: Add employee information
    first_name_field = driver.find_element(By.NAME, 'firstName')
    first_name_field.send_keys("Bobert")

    last_name_field = driver.find_element(By.NAME, 'lastName')
    last_name_field.send_keys("Perdolia")

    employee_id_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    employee_id_field.send_keys("7913")

    img_path = os.path.abspath('C:/Users/RK/Desktop/Projects/Selenium/profile.jpg')

    # Attempt to upload file
    try:
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image file not found: {img_path}")

        upload_field = driver.find_element(By.XPATH, '//input[@type="file"]')
        upload_field.send_keys(img_path)
        print("Image uploaded successfully")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")

    except Exception as upload_error:
        print(f"Error uploading image: {upload_error}")


    login_details_enable = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
    login_details_enable.click()

    create_username = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
    create_username.send_keys("bobert")

    create_password = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
    create_password.send_keys("bobert123")

    confirm_password = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
    confirm_password.send_keys("bobert123")

    time.sleep(10)

    save_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    save_button.submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h6[text()="Personal Details"]'))
    )

    # Go to Job window in the description
    job_description = driver.find_element(By.XPATH, '//a[text()="Job"]')
    job_description.click()

    # Select Joined Date
    joined_date_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]'))
    )
    joined_date_field.clear()
    joined_date_field.send_keys("2024-01-15")

    time.sleep(2)

    # Select Job Title
    job_title_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'))
    )
    job_title_dropdown.click()
    time.sleep(2)

    desired_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Software Engineer"]'))
    )
    desired_option.click()
    time.sleep(2)

    # Select Job Category
    job_category_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]')
        )
    )
    job_category_dropdown.click()
    time.sleep(2)

    desired_job_category = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Professionals"]'))
    )
    desired_job_category.click()

    # Select Location
    location_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]'))
    )
    location_dropdown.click()
    time.sleep(2)

    desired_location = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="New York Sales Office"]'))
    )
    desired_location.click()
    time.sleep(2)

    # Select Employment Status
    employment_status_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]'))
    )
    employment_status_dropdown.click()
    time.sleep(2)

    desired_employment_status = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Full-Time Permanent"]'))
    )
    desired_employment_status.click()
    time.sleep(2)

    job_save_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    job_save_btn.submit()
    time.sleep(5)

    # Click on Report-to button

    report_to_btn = driver.find_element(By.XPATH, '//a[text()="Report-to"]')
    report_to_btn.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h6[text()="Report to"]'))
    )

    # toliau koduojam


except Exception as e:
    print(f"An error occurred: {e}")


finally:
    print("Done")



