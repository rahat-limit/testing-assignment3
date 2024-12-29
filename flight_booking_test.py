
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service

driver = webdriver.Chrome()

try:
    driver.get("https://www.blazedemo.com/")
    
    departure_city = driver.find_element(By.NAME, "fromPort")
    destination_city = driver.find_element(By.NAME, "toPort")
    find_flights_button = driver.find_element(By.XPATH, "//input[@value='Find Flights']")
    
    departure_city.send_keys("Paris")
    destination_city.send_keys("Buenos Aires")
    find_flights_button.click()
    
    time.sleep(3)

    choose_flight_button = driver.find_element(By.XPATH, "//tbody/tr[3]/td[1]/input[1]")
    choose_flight_button.click()

    name_field = driver.find_element(By.ID, "inputName")
    address_field = driver.find_element(By.ID, "address")
    city_field = driver.find_element(By.ID, "city")
    state_field = driver.find_element(By.ID, "state")
    zip_code_field = driver.find_element(By.ID, "zipCode")
    card_type = driver.find_element(By.ID, "cardType")
    credit_card_number = driver.find_element(By.ID, "creditCardNumber")
    purchase_button = driver.find_element(By.XPATH, "//input[@value='Purchase Flight']")
    
    name_field.send_keys("John Doe")
    address_field.send_keys("123 Elm St")
    city_field.send_keys("Springfield")
    state_field.send_keys("IL")
    zip_code_field.send_keys("62704")
    card_type.send_keys("Visa")
    credit_card_number.send_keys("4111111111111111")
    purchase_button.click()

    time.sleep(3)
    confirmation = driver.find_element(By.TAG_NAME, "h1")
    if confirmation.text == "Thank you for your purchase today!":
        print("Flight booked successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()