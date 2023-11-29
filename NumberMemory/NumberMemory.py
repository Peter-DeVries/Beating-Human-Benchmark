import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui


def number_memory():
    # Set up the driver
    driver = webdriver.Chrome()

    # Have driver receive page
    url = "https://humanbenchmark.com/tests/number-memory"
    driver.get(url)

    # Use BeautifulSoup to parse the page source
    answer = ''
    while True:
        if not answer:
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            span = soup.find(class_='big-number')
            answer = span.text if span else None
            print(answer)
        else:
            # Type the text using pyautogui
            time.sleep(len(answer) + 2)
            pyautogui.write(answer, interval=0)
            time.sleep(1)
            pyautogui.press('enter')
            answer = ''
            time.sleep(1)
            pyautogui.press('enter')


# Call the function with an optional interval (default is 1 second)
if __name__ == '__main__':
    number_memory()
