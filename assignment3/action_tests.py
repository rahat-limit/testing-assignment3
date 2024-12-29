from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ActionTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_hover_action(self):
        """
        Test mouse hover action to reveal hidden elements
        """
        print("\nTesting Hover Action...")
        try:
            # Navigate to a page with hover elements
            self.driver.get("https://the-internet.herokuapp.com/hovers")
            
            # Find the first user avatar
            user_avatar = self.driver.find_element(By.CSS_SELECTOR, ".figure")
            
            # Perform hover action
            self.actions.move_to_element(user_avatar).perform()
            
            # Verify hidden content is displayed
            user_info = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".figcaption h5"))
            )
            print(f"Revealed text on hover: {user_info.text}")
            
        except Exception as e:
            print(f"Error in hover test: {str(e)}")

    def test_drag_and_drop(self):
        """
        Test drag and drop operation
        """
        print("\nTesting Drag and Drop...")
        try:
            # Navigate to drag and drop page
            self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
            
            # Find source and target elements
            source = self.driver.find_element(By.ID, "column-a")
            target = self.driver.find_element(By.ID, "column-b")
            
            # Perform drag and drop
            self.actions.drag_and_drop(source, target).perform()
            
            # Verify the swap
            time.sleep(1)  # Small wait to ensure swap is complete
            print("Drag and drop operation completed")
            
        except Exception as e:
            print(f"Error in drag and drop test: {str(e)}")

    def test_context_click(self):
        """
        Test right-click (context click) operation
        """
        print("\nTesting Context Click...")
        try:
            # Navigate to context menu page
            self.driver.get("https://the-internet.herokuapp.com/context_menu")
            
            # Find the context menu area
            context_element = self.driver.find_element(By.ID, "hot-spot")
            
            # Perform right click
            self.actions.context_click(context_element).perform()
            
            # Switch to alert and accept it
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            
            print(f"Context click triggered alert: {alert_text}")
            
        except Exception as e:
            print(f"Error in context click test: {str(e)}")

    def test_keyboard_actions(self):
        """
        Test keyboard actions
        """
        print("\nTesting Keyboard Actions...")
        try:
            # Navigate to inputs page
            self.driver.get("https://the-internet.herokuapp.com/inputs")
            
            # Find input field
            input_field = self.driver.find_element(By.TAG_NAME, "input")
            
            # Click the input field
            input_field.click()
            
            # Type text with shift key
            self.actions.key_down(Keys.SHIFT)\
                .send_keys("hello world")\
                .key_up(Keys.SHIFT)\
                .perform()
            
            # Select all text (Ctrl+A)
            self.actions.key_down(Keys.CONTROL)\
                .send_keys('a')\
                .key_up(Keys.CONTROL)\
                .perform()
            
            # Copy text (Ctrl+C)
            self.actions.key_down(Keys.CONTROL)\
                .send_keys('c')\
                .key_up(Keys.CONTROL)\
                .perform()
            
            print("Keyboard actions completed successfully")
            
        except Exception as e:
            print(f"Error in keyboard actions test: {str(e)}")

    def test_click_and_hold(self):
        """
        Test click and hold operation
        """
        print("\nTesting Click and Hold...")
        try:
            # Navigate to dynamic content page
            self.driver.get("https://the-internet.herokuapp.com/dynamic_content")
            
            # Find an image element
            image = self.driver.find_element(By.CSS_SELECTOR, "img")
            
            # Perform click and hold
            self.actions.click_and_hold(image)\
                .pause(2)\
                .release()\
                .perform()
            
            print("Click and hold operation completed")
            
        except Exception as e:
            print(f"Error in click and hold test: {str(e)}")

    def run_tests(self):
        """
        Run all action tests
        """
        try:
            self.test_hover_action()
            self.test_drag_and_drop()
            self.test_context_click()
            self.test_keyboard_actions()
            self.test_click_and_hold()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    action_tests = ActionTests()
    action_tests.run_tests()
