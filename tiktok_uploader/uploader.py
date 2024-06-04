from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config

def upload_to_tiktok(video_path, description):
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
    driver.get('https://www.tiktok.com/login')
    
    # Add your TikTok login automation here
    # Example login (you need to adapt this based on TikTok's login mechanism)
    username_input = driver.find_element_by_name('username')
    password_input = driver.find_element_by_name('password')
    login_button = driver.find_element_by_xpath('//button[text()="Log In"]')
    
    username_input.send_keys(config.TIKTOK_USERNAME)
    password_input.send_keys(config.TIKTOK_PASSWORD)
    login_button.click()
    
    time.sleep(5)  # Wait for login to complete
    
    driver.get('https://www.tiktok.com/upload')
    
    file_input = driver.find_element_by_xpath('//input[@type="file"]')
    file_input.send_keys(video_path)
    
    desc_box = driver.find_element_by_xpath('//textarea[@placeholder="Description"]')
    desc_box.send_keys(description)
    
    time.sleep(10)  # Adjust this sleep time as needed
    post_button = driver.find_element_by_xpath('//button[text()="Post"]')
    post_button.click()
    
    time.sleep(5)
    driver.quit()
