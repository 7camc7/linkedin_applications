from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time

chrome_driver_path = "/Users/claudiachurch/Desktop/web_dev/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3331090506&f_AL=true&f_WT=2&geoId=101165590&keywords=writer&location=United%20Kingdom&refresh=true")
sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_link.click()

# Log in:
email = driver.find_element(By.ID, "username")
email.send_keys(os.environ.get("EMAIL"))
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ.get("PASSWORD"))
sign_in_button = driver.find_element(By.CLASS_NAME, "login__form button")
sign_in_button.click()

all_jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")

for job in all_jobs:
    job.click()
    time.sleep(5)
    try:
        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("No save")
        continue





# crypto_job = driver.find_element(By.LINK_TEXT, "Crypto Content Writer")
# crypto_job.click()
# easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card span")
# time.sleep(5)
# easy_apply.click()
# next_button = driver.find_element(By.CSS_SELECTOR, "#ember430 span")
# next_button.click()
# time.sleep(2)
# second_next = driver.find_element(By.CSS_SELECTOR, "#ember430 span")
# second_next.click()


