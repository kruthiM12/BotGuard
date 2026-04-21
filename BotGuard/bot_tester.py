from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

print("🤖 Initialize Attack Bot...")

# 1. Boot up a silent, automated browser
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # Uncomment this to run it invisibly like a real background bot
driver = webdriver.Chrome(options=options)

# 2. Open the local HTML file
file_path = f"file://{os.path.abspath('index.html')}"
driver.get(file_path)
print("🤖 Infiltrated target site.")

try:
   
    transfer_btn = driver.find_element(By.ID, "transfer-btn")
    transfer_btn.click()
    print("🤖 Executed Transfer Click.")

   
    target = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "target-icon"))
    )
    
   
    target.click()
    print("🤖 Bypassed visual security check.")

    time.sleep(5)

finally:
    driver.quit()
    print("🤖 Bot disconnected.")