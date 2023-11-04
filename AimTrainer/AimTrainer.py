import time
import pyautogui
from Helpers.ScreenGrabber import *

# Define the region to search for the target color
start_x = 326
start_y = 242
end_x = 1226
end_y = 680

# Define the target color in (R, G, B) format
target_color = [163, 194, 229]

screen_grabber = ScreenGrabber(0, 0, 1440, 900, -1)
screen_grabber.take_screen_shot()


def aim_trainer():
    try:
        while True:
            screen_grabber.take_screen_shot()

            # Loop through the specified region and check for the target color
            for y in range(start_y, end_y + 1):
                for x in range(start_x, end_x + 1):
                    pixel_color = screen_grabber.get_pixel_color(x, y)
                    if pixel_color == target_color:
                        # Click the pixel if the target color is found
                        pyautogui.click(x, y)
                        break  # Stop the inner loop

    except KeyboardInterrupt:
        print("Function stopped by user.")


if __name__ == '__main__':
    time.sleep(5)
    aim_trainer()
