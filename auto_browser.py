from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("🚀 Initializing bot...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

print("✅ Accessing Bing...")
driver.get("https://cn.bing.com")
time.sleep(3)

try:
    print("👀 Locating search box...")
    search_box = driver.find_element(By.ID, "sb_form_q")
    search_box.click()
    
    print("🤖 Typing search query...")
    search_box.send_keys("Fiverr")
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    
    print("⏳ Waiting for search results to load (3s)...")
    time.sleep(3)
    
    # [New Feature] Capture and save screenshot
    # This serves as "Proof of Work" for clients
    print("📸 Taking screenshot...")
    driver.save_screenshot('fiverr_search_result.png')
    print("✅ Screenshot saved successfully!")

except Exception as e:
    print(f"❌ Error occurred: {e}")

print("Test complete, closing in 5 seconds...")
time.sleep(5)

driver.quit()
