from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

def startBot(username, password, url):
    # Fix ChromeDriver path - point to the actual executable
    path = r'C:\Users\BOI\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    
    try:
        # Open the site
        driver.get(url)

        
        driver.find_element(By.NAME, 'email').send_keys(username)
        
        driver.find_element(By.NAME, 'password').send_keys(password)
        
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        input("Press Enter to close browser...")
        driver.quit()

# Credentials
username = 'pixelalharam@pixel.com'
password = 'Pixels.ceo007'
url = "https://pixel-tuition.netlify.app/auth"

# Call function to start the bot
startBot(username, password, url)