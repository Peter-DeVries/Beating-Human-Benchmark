import time
import pyautogui
from Helpers.ScreenGrabber import *

# Locate pixel location on screen
res = None
while res is None:
    res = pyautogui.locateOnScreen("Aim_Trainer.png", confidence=0.5)
x, y = res.left, res.top

# Define the target color in (R, G, B) format
target_color = [177, 215, 252]

screen_grabber = ScreenGrabber(0, 0, 2560, 1440, -1)
screen_grabber.take_screen_shot()

pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0


def click_grid():
    for i in range(15):
        screen_grabber.take_screen_shot()
        for y in range(start_y, end_y + 1, 30):
            for x in range(start_x, end_x + 1, 30):
                pyautogui.click(x, y)
                print(screen_grabber.get_pixel_color(x, y))


def aim_trainer():
    try:
        while True:
            screen_grabber.take_screen_shot()

            # Loop through the specified region and check for the target color
            for y in range(start_y, end_y + 1, 25):
                for x in range(start_x, end_x + 1, 25):
                    pixel_color = screen_grabber.get_pixel_color(x, y)
                    if pixel_color == target_color:
                        # Click the pixel if the target color is found
                        pyautogui.click(x, y)
                        break  # Stop the inner loop

    except KeyboardInterrupt:
        print("Function stopped by user.")


if __name__ == '__main__':
    time.sleep(1)
    aim_trainer()
    # click_grid()
