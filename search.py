# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
import time

driver = webdriver.Chrome()
try:
    # Open YouTube
    driver.get("https://www.youtube.com")
    
    # Locate the search box on YouTube and search for "ASMR"
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Testing lesson")
    search_box.send_keys(Keys.RETURN)  # Simulate pressing Enter
    
    # Wait for results to load (simplified with sleep here)
    time.sleep(3)
    
    # Validate results using XPath (YouTube shows results after search)
    result_stats = driver.find_element(By.XPATH, "//ytd-video-renderer")
    if result_stats.is_displayed():
        print("Search results displayed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Quit the driver
    driver.quit()