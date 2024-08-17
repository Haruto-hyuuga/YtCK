from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Set up the web driver (for Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

# Navigate to YouTube login page
driver.get('https://accounts.google.com/ServiceLogin?service=youtube')

# Enter your email
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys('YOUR_EMAIL')
email_input.send_keys(Keys.RETURN)

time.sleep(2)  # Wait for password field to appear

# Enter your password
password_input = driver.find_element(By.XPATH, '//*[@name="password"]')
password_input.send_keys('YOUR_PASSWORD')
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for the login process to complete

# Save cookies to a file
cookies = driver.get_cookies()
with open('cookies.txt', 'w') as file:
    file.write(json.dumps(cookies))

driver.quit()

print("Cookies have been saved to cookies.txt")

