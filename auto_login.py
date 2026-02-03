from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("🚀 Login bot starting...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Access the login page
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)
print("✅ Login page opened successfully")
time.sleep(2)

try:
    # 2. Locate the username field and input credentials
    # (ID identified as 'username' via Browser DevTools)
    print("⌨️ Entering username...")
    user_box = driver.find_element(By.ID, "username")
    user_box.send_keys("student")
    
    # 3. Locate the password field and input credentials
    # (ID identified as 'password' via Browser DevTools)
    print("🔑 Entering password...")
    pass_box = driver.find_element(By.ID, "password")
    pass_box.send_keys("Password123")
    
    # 4. Locate the login button and perform click
    # (ID identified as 'submit')
    print("🖱️ Clicking Login...")
    btn = driver.find_element(By.ID, "submit")
    btn.click()
    
    # 5. Verification of login status
    time.sleep(3)
    # Successful login redirects the URL or displays a success message
    if "logged-in-successfully" in driver.current_url:
        print("🎉🎉🎉 Login successful! Accessing dashboard...")
        
        # Capture screenshot for verification
        driver.save_screenshot("login_success.png")
        print("📸 Success screenshot saved")
        
    else:
        print("❌ Login failed. Please verify credentials.")

except Exception as e:
    print(f"❌ An error occurred: {e}")

print("Test complete. Shutting down in 10 seconds...")
time.sleep(10)
driver.quit()
