from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectTests:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_single_select(self):
        """
        Test single select operations using different selection methods
        """
        print("\nTesting Single Select...")
        try:
            # Navigate to dropdown page
            self.driver.get("https://the-internet.herokuapp.com/dropdown")
            
            # Find the dropdown element
            dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
            
            # Select by visible text
            dropdown.select_by_visible_text("Option 1")
            print(f"Selected option by text: {dropdown.first_selected_option.text}")
            
            # Select by value
            dropdown.select_by_value("2")
            print(f"Selected option by value: {dropdown.first_selected_option.text}")
            
            # Select by index
            dropdown.select_by_index(1)
            print(f"Selected option by index: {dropdown.first_selected_option.text}")
            
        except Exception as e:
            print(f"Error in single select test: {str(e)}")

    def test_multiple_select(self):
        """
        Test multiple select operations
        """
        print("\nTesting Multiple Select...")
        try:
            # Navigate to the jQuery UI page with multiple select
            self.driver.get("https://output.jsbin.com/osebed/2")
            
            # Find the multiple select element
            multi_select = Select(self.driver.find_element(By.ID, "fruits"))
            
            # Verify it's a multiple select
            if multi_select.is_multiple:
                # Select multiple options
                multi_select.select_by_value("banana")
                multi_select.select_by_visible_text("Apple")
                multi_select.select_by_index(3)  # Grape
                
                # Get all selected options
                selected_options = multi_select.all_selected_options
                print("Selected options:")
                for option in selected_options:
                    print(f"- {option.text}")
                
                # Deselect specific option
                multi_select.deselect_by_visible_text("Apple")
                print("\nAfter deselecting Apple:")
                for option in multi_select.all_selected_options:
                    print(f"- {option.text}")
                
                # Deselect all options
                multi_select.deselect_all()
                print("\nAll options deselected")
            else:
                print("This is not a multiple select element")
            
        except Exception as e:
            print(f"Error in multiple select test: {str(e)}")

    def test_select_validation(self):
        """
        Test select operations with validation
        """
        print("\nTesting Select Validation...")
        try:
            # Navigate to dropdown page
            self.driver.get("https://the-internet.herokuapp.com/dropdown")
            
            # Find the dropdown element
            dropdown = Select(self.driver.find_element(By.ID, "dropdown"))
            
            # Get all options
            all_options = dropdown.options
            print("Available options:")
            for option in all_options:
                print(f"- {option.text} (value: {option.get_attribute('value')})")
            
            # Select an option and validate
            dropdown.select_by_index(1)
            selected = dropdown.first_selected_option
            assert selected.text == "Option 1", f"Expected 'Option 1' but got {selected.text}"
            print(f"\nValidation passed: Correct option selected ({selected.text})")
            
        except AssertionError as e:
            print(f"Validation failed: {str(e)}")
        except Exception as e:
            print(f"Error in select validation test: {str(e)}")

    def run_tests(self):
        """
        Run all select tests
        """
        try:
            self.test_single_select()
            self.test_multiple_select()
            self.test_select_validation()
        finally:
            self.driver.quit()

if __name__ == "__main__":
    select_tests = SelectTests()
    select_tests.run_tests()
