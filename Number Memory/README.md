Libraries required:
- selenium 
- bs4 (BeautifulSoup4)
- pyautogui

NumberMemory.py opens human benchmark's number memory test in a Selenium window, allowing it to scrape
the required numbers and enter it a few seconds later. Time was used to wait for the delay as there's a
linear delay with each number added to the challenge.

![Percentile Number Memory](https://github.com/Peter-DeVries/Beating-Human-Benchmark/assets/71617666/b475dc3b-2d38-4cc6-9b4d-a763ae56ffc3)

Note: It can go forever, I just stopped it at 35 as that's 100% percentile. It takes an increasing
amount of time with each number, so I just stopped it early.
