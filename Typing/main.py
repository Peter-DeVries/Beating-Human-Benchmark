import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui

# Set up the driver
driver = webdriver.Chrome()

# Have driver receive page
url = "https://humanbenchmark.com/tests/typing"
driver.get(url)

# Wait for page to fully load
time.sleep(4)

# Get the page source
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')
spans = soup.find_all('span', class_='incomplete')
text_to_type = ''.join([span.get_text() for span in spans])
print(text_to_type)

# Wait for focused webpage
time.sleep(2)

# Type the text using pyautogui
pyautogui.write(text_to_type, interval=0)

# See results
time.sleep(40000)
