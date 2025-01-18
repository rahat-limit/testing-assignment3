import pytest
import logging
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
log_directory = "logs"
screenshots_dir = "screenshots"
for directory in [log_directory, screenshots_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

logging.basicConfig(
    filename=os.path.join(log_directory, f'test_execution_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def take_screenshot(driver, name):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshot_path = os.path.join(screenshots_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    logging.info(f"Screenshot saved: {screenshot_path}")

class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method that runs before each test (equivalent to @BeforeMethod in TestNG)"""
        logging.info("Setting up the test")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        logging.info("Tearing down the test")
        self.driver.quit()

    def test_successful_login(self):
        """Test successful login to sauce demo"""
        logging.info("Starting login test")
        self.driver.get("https://www.saucedemo.com/")
        take_screenshot(self.driver, "login_page")
        
        # Login
        username = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        
        # Verify successful login
        products_title = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
        assert products_title.text == "Products"
        take_screenshot(self.driver, "products_page")
        logging.info("Login test completed successfully")

    def test_add_to_cart(self):
        """Test adding item to cart"""
        logging.info("Starting add to cart test")
        self.driver.get("https://www.saucedemo.com/")
        
        # Login first
        username = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        
        # Add item to cart
        add_to_cart_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")))
        take_screenshot(self.driver, "before_add_to_cart")
        add_to_cart_button.click()
        
        # Verify cart badge
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"
        take_screenshot(self.driver, "after_add_to_cart")
        logging.info("Add to cart test completed successfully")

    def test_checkout_process(self):
        """Test checkout process"""
        logging.info("Starting checkout test")
        self.driver.get("https://www.saucedemo.com/")
        
        # Login
        username = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        
        # Add item to cart
        add_to_cart_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']")))
        add_to_cart_button.click()
        
        # Go to cart
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        take_screenshot(self.driver, "cart_page")
        
        # Start checkout
        checkout_button = self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()
        
        # Fill checkout information
        first_name = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        last_name = self.driver.find_element(By.ID, "last-name")
        postal_code = self.driver.find_element(By.ID, "postal-code")
        
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        postal_code.send_keys("12345")
        take_screenshot(self.driver, "checkout_info")
        
        # Continue checkout
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        
        # Verify we're on checkout overview
        finish_button = self.wait.until(EC.presence_of_element_located((By.ID, "finish")))
        assert finish_button.is_displayed()
        take_screenshot(self.driver, "checkout_overview")
        logging.info("Checkout test completed successfully")

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html", "--self-contained-html"])
