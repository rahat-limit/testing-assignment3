from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service

driver = webdriver.Chrome()

try:
    # Open the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    wait = WebDriverWait(driver, 15)

    username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))

    username_field.send_keys("student")
    password_field.send_keys("Password123")
    submit_button.click()

    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Logged In Successfully']")))
    if success_message.is_displayed():
        print("Login successful.")

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log out']")))
    logout_button.click()

    login_button = wait.until(EC.visibility_of_element_located((By.ID, "submit")))
    if login_button.is_displayed():
        print("Logout successful.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Quit the driver
    driver.quit()