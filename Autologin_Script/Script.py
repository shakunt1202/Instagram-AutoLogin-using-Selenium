import selenium as se
import urllib.request
from selenium import webdriver
import Credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome("S:\Python Notebooks,files\Projects\Instagram Auto_login\Chromedriver_97.exe",chrome_options=chrome_options)
url = "https://www.instagram.com/"


driver.get(url)
driver.maximize_window

dict = Credentials.id_pass

ID = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name ='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name ='password']")))

ID.send_keys(dict["ID"])
password.send_keys(dict["Password"])
Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

print("you have successfully Logged in Instagram with " + dict["ID"] + " Account")

not_now_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now_notification = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
