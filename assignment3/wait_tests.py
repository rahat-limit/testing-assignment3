from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
import time

class WaitTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_implicit_wait(self):
        """
        Test implicit wait on a dynamic loading page
        """
        print("\nTesting Implicit Wait...")
        try:
            # Set implicit wait for 10 seconds
            self.driver.implicitly_wait(10)
            
            # Navigate to a page with dynamic content
            self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
            
            # Click the start button
            start_button = self.driver.find_element(By.CSS_SELECTOR, "#start button")
            start_button.click()
            
            # Try to find the element that appears after loading
            finish_text = self.driver.find_element(By.CSS_SELECTOR, "#finish h4")
            print(f"Found text with implicit wait: {finish_text.text}")
            
        except Exception as e:
            print(f"Error in implicit wait test: {str(e)}")

    def test_explicit_wait(self):
        """
        Test explicit wait on a dynamic loading page
        """
        print("\nTesting Explicit Wait...")
        try:
            # Navigate to a page with dynamic content
            self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
            
            # Click the start button
            start_button = self.driver.find_element(By.CSS_SELECTOR, "#start button")
            start_button.click()
            
            # Use explicit wait for the element to be visible
            wait = WebDriverWait(self.driver, 10)
            finish_text = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
            )
            
            print(f"Found text with explicit wait: {finish_text.text}")
            
        except TimeoutException:
            print("Timeout waiting for element to be visible")
        except Exception as e:
            print(f"Error in explicit wait test: {str(e)}")

    def test_fluent_wait(self):
        """
        Test fluent wait on a dynamic loading page
        """
        print("\nTesting Fluent Wait...")
        try:
            # Navigate to a page with dynamic content
            self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")
            
            # Click the remove button
            remove_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
            remove_button.click()
            
            # Create fluent wait
            wait = WebDriverWait(
                driver=self.driver,
                timeout=10,
                poll_frequency=0.5,
                ignored_exceptions=[NoSuchElementException, ElementNotVisibleException]
            )
            
            # Wait for the message to appear
            message = wait.until(
                EC.presence_of_element_located((By.ID, "message"))
            )
            
            print(f"Found message with fluent wait: {message.text}")
            
        except TimeoutException:
            print("Timeout waiting for element")
        except Exception as e:
            print(f"Error in fluent wait test: {str(e)}")

    def run_tests(self):
        """
        Run all wait tests
        """
        try:
            self.test_implicit_wait()
            self.test_explicit_wait()
            self.test_fluent_wait()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    wait_tests = WaitTests()
    wait_tests.run_tests()
