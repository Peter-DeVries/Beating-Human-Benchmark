import pyautogui
import time
from Helpers.ScreenGrabber import *

# Define the RGB values for red and green (values might be different based on machine)
white_color = [255, 255, 255]
width = 2560
height = 1440
step = 15

# Locate pixel location on screen
# res = None
# while res is None:
#     res = pyautogui.locateOnScreen("Starting_Board.png", confidence=0.5)
# start_x, start_y = res.left, res.top
# end_x, end_y = res.left + res.width, res.top + res.height
start_x, start_y = 1081, 261
end_x, end_y = 1563, 670

# Instantiates the ScreenGabber class which utilizes mss for fastest times possible
screen_grabber = ScreenGrabber(0, 0, width, height, -1)
screen_grabber.take_screen_shot()


def visual_memory():
    try:
        while True:
            positions = []
            if not positions:
                screen_grabber.take_screen_shot()

                # Loop through the specified region and check for the target color
                for y in range(start_y, end_y + 1, step):
                    for x in range(start_x, end_x + 1, step):
                        pixel_color = screen_grabber.get_pixel_color(x, y)
                        if pixel_color == white_color:
                            # Click the pixel if the target color is found
                            positions.append((x, y))

            time.sleep(3)
            for pos in positions:
                pyautogui.click(pos[0], pos[1])
                positions.remove(pos)

    except KeyboardInterrupt:
        print("Function stopped by user.")


if __name__ == '__main__':
    pyautogui.PAUSE = 0.0
    pyautogui.MINIMUM_DURATION = 0.0
    pyautogui.FAILSAFE = True
    visual_memory()
