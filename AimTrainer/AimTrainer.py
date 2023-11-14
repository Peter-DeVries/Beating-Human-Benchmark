import time
import pyautogui
from Helpers.ScreenGrabber import *

# Define the RGB values for red and green (values might be different based on machine)
target_color = [149, 195, 232]
stop_color = [255, 209, 84]
width = 2560
height = 1440
step = 15

# Locate pixel location on screen
res = None
while res is None:
    res = pyautogui.locateOnScreen("Aim_Trainer.png", confidence=0.5)
start_x, start_y = res.left, res.top
end_x, end_y = res.left + res.width, res.top + res.height

# Instantiates the ScreenGabber class which utilizes mss for fastest times possible
screen_grabber = ScreenGrabber(0, 0, width, height, -1)
screen_grabber.take_screen_shot()


def aim_trainer():
    try:
        while True:
            screen_grabber.take_screen_shot()

            # Loop through the specified region and check for the target color
            for y in range(start_y, end_y + 1, step):
                for x in range(start_x, end_x + 1, step):
                    pixel_color = screen_grabber.get_pixel_color(x, y)
                    if pixel_color == stop_color:
                        return
                    if pixel_color == target_color:
                        # Click the pixel if the target color is found
                        pyautogui.click(x, y)
                        break  # Stop the inner loop

    except KeyboardInterrupt:
        print("Function stopped by user.")


if __name__ == '__main__':
    pyautogui.PAUSE = 0.0
    pyautogui.MINIMUM_DURATION = 0.0
    pyautogui.FAILSAFE = True
    aim_trainer()
