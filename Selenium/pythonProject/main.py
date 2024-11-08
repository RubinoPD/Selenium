from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

# Set up Firefox options
options = Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"  # Update path if necessary

# Initialize WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

try:
    # Step 1: Go to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)

    # Step 2: Login as Admin
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)  # Wait for the dashboard to load

    # # 3: Navigate to Add Employee page
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
    # time.sleep(2)
    #
    # # 4: Add employee information
    # first_name_field = driver.find_element(By.NAME, 'firstName')
    # first_name_field.send_keys("Bobert")
    #
    # last_name_field = driver.find_element(By.NAME, 'lastName')
    # last_name_field.send_keys("Perdolia")
    #
    # employee_id_field = driver.find_element(By.XPATH,
    #                                         '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
    # employee_id_field.send_keys("7913")
    #
    # img_path = os.path.abspath('C:/Users/RK/Desktop/Projects/Selenium/profile.jpg')
    #
    # # Attempt to upload file
    # try:
    #     if not os.path.exists(img_path):
    #         raise FileNotFoundError(f"Image file not found: {img_path}")
    #
    #     upload_field = driver.find_element(By.XPATH, '//input[@type="file"]')
    #     upload_field.send_keys(img_path)
    #     print("Image uploaded successfully")
    #
    # except FileNotFoundError as fnf_error:
    #     print(f"Error: {fnf_error}")
    #
    # except Exception as upload_error:
    #     print(f"Error uploading image: {upload_error}")
    #
    # login_details_enable = driver.find_element(By.XPATH,
    #                                            '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
    # login_details_enable.click()
    #
    # create_username = driver.find_element(By.XPATH,
    #                                       '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
    # create_username.send_keys("bobert")
    #
    # create_password = driver.find_element(By.XPATH,
    #                                       '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input')
    # create_password.send_keys("bobert123")
    #
    # confirm_password = driver.find_element(By.XPATH,
    #                                        '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')
    # confirm_password.send_keys("bobert123")
    #
    # time.sleep(10)
    #
    # save_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    # save_button.submit()
    # time.sleep(5)

    # Step 3: Navigate to the User Management page in Admin
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    time.sleep(2)

    # Step 4: Click "Add" to add a new user
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]'))
    )
    add_button.click()

    # Step 5: Fill out the new user details
    # Select User Role (e.g., ESS, Admin, etc.) - assuming "ESS" for Supervisor role
    role_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
    )
    role_dropdown.click()
    role_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="ESS"]'))
    )
    role_option.click()

    # Enter employee name (e.g., "John Smith") in the Employee Name field
    emp_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Type for hints..."]'))
    )
    emp_name_field.send_keys("Bobert Perdolia")
    time.sleep(2)  # Wait briefly for the autocomplete suggestions

    # Select "John Smith" from the suggestions
    emp_name_suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "oxd-autocomplete-dropdown")]//div[text()="John Smith"]'))
    )
    emp_name_suggestion.click()

    # Enter a unique username for the supervisor
    driver.find_element(By.XPATH, '//label[text()="Username"]/following-sibling::div//input').send_keys("john.smith.supervisor")

    # Select status as "Enabled"
    status_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//label[text()="Status"]/following-sibling::div//div[@role="combobox"]'))
    )
    status_dropdown.click()
    status_enabled = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and text()="Enabled"]'))
    )
    status_enabled.click()

    # Set password and confirm password
    driver.find_element(By.XPATH, '//label[text()="Password"]/following-sibling::div//input').send_keys("Password123!")
    driver.find_element(By.XPATH, '//label[text()="Confirm Password"]/following-sibling::div//input').send_keys("Password123!")

    # Step 6: Save the new user
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Save")]'))
    )
    save_button.click()

    # Optional: Wait to confirm the entry is saved
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser if you're done
    driver.quit()
    print("New supervisor creation automation complete.")
