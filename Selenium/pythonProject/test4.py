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

# Go to the Buzz window
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
time.sleep(3)

buzz_share_photo_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]')
buzz_share_photo_btn.click()
time.sleep(5)

message_field = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/textarea[1]')
message_field.send_keys("Hello, THIS IS ME NICE TO MEET YOU ALL!!!")
time.sleep(3)

file_path = "C:\\Users\\Robertas\\Desktop\\Selenium\\Selenium\\profile.jpg" # "C:\Users\Robertas\Desktop\Selenium\Selenium\profile.jpg"

file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
driver.execute_script("arguments[0].style.display = 'block';", file_input)  # Unhide the input element
file_input.send_keys(file_path)
time.sleep(2)

share_btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[3]/button')
share_btn.submit()
time.sleep(5)

# Like my own post
like_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/*[name()="svg"][1]/*[name()="g"][1]/*[name()="path"][1]')
like_btn.click()
time.sleep(3)

# Edit your post
triple_dot_btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button/i')
triple_dot_btn.click()
time.sleep(2)

post_edit_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/li[1]/ul[1]/li[2]/p[1]')
post_edit_btn.click()
time.sleep(5)

edit_post_text = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/textarea[1]')
edit_post_text.send_keys(Keys.CONTROL + "a")
time.sleep(2)
edit_post_text.send_keys(Keys.DELETE)
time.sleep(2)
edit_post_text.send_keys("This is my EDITED POST!")
time.sleep(3)

edit_post_btn = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]')
edit_post_btn.submit()
time.sleep(5)

# Comment on your own post
comment_btn = driver.find_element(By.XPATH, '//i[contains(@class, "bi-chat-text-fill")]')
comment_btn.click()
time.sleep(2)

comment_input_field = driver.find_element(By.XPATH, '//input[@placeholder="Write your comment..."]')
comment_input_field.send_keys("Welcome on board! :)")
time.sleep(2)
comment_input_field.send_keys(Keys.ENTER)
time.sleep(4)

# Like your own comment
like_comment_btn = driver.find_element(By.XPATH, '//div[contains(@class, "orangehrm-post-comment-action")]//p[text()="Like"]')
like_comment_btn.click()
time.sleep(2)

# Edit your own comment
edit_comment_btn = driver.find_element(By.XPATH, '//div[contains(@class, "orangehrm-post-comment-action")]//p[text()="Edit"]')
edit_comment_btn.click()
time.sleep(2)

edit_comment_input = driver.find_element(By.XPATH, '//input[contains(@class, "oxd-input--focus")]')
edit_comment_input.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(2)
edit_comment_input.send_keys("This is EDITED COMMENT!!!")
time.sleep(2)
edit_comment_input.send_keys(Keys.ENTER)
time.sleep(2)

# Delete your own comment
like_comment_btn = driver.find_element(By.XPATH, '//div[contains(@class, "orangehrm-post-comment-action")]//p[text()="Delete"]')
like_comment_btn.click()
time.sleep(2)

alert_btn_yes = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]')
alert_btn_yes.click()
time.sleep(4)

# Delete your own POST
menu_for_delete = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button/i')
menu_for_delete.click()
time.sleep(2)

post_delete_btn = driver.find_element(By.XPATH, '//li//p[text()="Delete Post"]')
post_delete_btn.click()
time.sleep(2)
alert2_btn_yes = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]')
alert2_btn_yes.click()
time.sleep(2)

print("Ketvirta uzduotis padaryta")