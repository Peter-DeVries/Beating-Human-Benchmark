from Helpers.ScreenGrabber import *
import pyautogui

# Define the RGB values for red and green (values might be different based on machine)
red_color = [206, 38, 54]
green_color = [75, 219, 106]
width = 2560
height = 1440

# Locate pixel location on screen
res = None
while res is None:
    res = pyautogui.locateOnScreen("Reaction_Time_Test.png", confidence=0.5)
x, y = res.left, res.top

# Instantiates the ScreenGabber class which utilizes mss for fastest times possible
screen_grabber = ScreenGrabber(0, 0, width, height, -1)
screen_grabber.take_screen_shot()


def reaction_time():
    while True:
        screen_grabber.take_screen_shot()
        current_color = screen_grabber.get_pixel_color(x, y)

        # Check if pixel is red
        if current_color == red_color:
            while True:
                # Wait until changes to green
                screen_grabber.take_screen_shot()
                current_color = screen_grabber.get_pixel_color(x, y)
                if current_color == green_color:
                    pyautogui.click(x, y)
                    break


if __name__ == '__main__':
    reaction_time()
