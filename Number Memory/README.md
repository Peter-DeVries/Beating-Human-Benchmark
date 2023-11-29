Libraries required:
- selenium 
- bs4 (BeautifulSoup4)
- pyautogui

NumberMemory.py opens human benchmark's number memory test in a Selenium window, allowing it to scrape
the required numbers and enter it a few seconds later. Time was used to wait for the delay as there's a
linear delay with each number added to the challenge.

**Image here**

Note: It can go forever, I just stopped it at 35 as that's 100% percentile. It takes an increasing
amount of time with each number, so I just stopped it early.