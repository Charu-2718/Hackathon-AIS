import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import requests

load_dotenv()

def main():
    # -------------------------------------------------------------
    driver_path = os.getenv("DRIVER_PATH")
    driver = webdriver.Edge(service=Service(executable_path=driver_path))

    base_url = os.getenv("BASE_URL")
    
    # -------------------------------------------------------------
    driver.get(base_url)
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtUserName"))
    )
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username = os.getenv("USER")
    password = os.getenv("PASSWORD")
        
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.url_changes(driver.current_url)
    )
    print("Login successful! Session established.")
    
    # -------------------------------------------------------------
    selenium_cookies = driver.get_cookies()
    requests_cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}

    policy_get = os.getenv("POLICY_URL_GET")

    resp = requests.get(policy_get, cookies=requests_cookies)
    data = json.loads(resp.text)

    for policy in data:
        policy_id = policy["PolicyId"]
        policy_title = policy["Title"]
        policy_title = policy_title.replace('/', '_')
        print(f"Processing policy: {policy_title}")

        policy_url_base = os.getenv('POLICY_URL')

        policy_url = f"{policy_url_base}/{policy_id}"

        driver.get(policy_url)
        time.sleep(2)

        rendered_html = driver.page_source
        soup = BeautifulSoup(rendered_html, 'html.parser')
        fetch = soup.find("div", attrs={'ng-bind-html': 'description'})

        if fetch:
            description_html = fetch.get_text()
            # Create a directory if it doesn't exist
            store_dir = os.getenv("POLICY_STORE_DIRECTORY", "Policies")
            os.makedirs(store_dir, exist_ok=True)  # if it already exists delete the prev directory to make a fresh start
            file_name = f"{store_dir}/policy_description_{policy_title}.txt"
            
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(description_html)

    driver.quit()

if __name__ == "__main__":
    main()