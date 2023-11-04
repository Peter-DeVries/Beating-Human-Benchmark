from Helpers.ScreenGrabber import *
import pyautogui

# Instantiates the ScreenGabber class which utilizes mss for fastest times possible
screen_grabber = ScreenGrabber(0, 0, 1440, 900, -1)
screen_grabber.take_screen_shot()

# Define the RGB values for red and green
red_color = [206, 38, 54]
green_color = [75, 219, 106]

mac_red_color = [189, 56, 60]
mac_green_color = [119, 216, 119]

# Positions here: x and y are the target position for the color pixel and click
# extra_monitor_offset needs to be set if an additional monitor is used.
x, y = 346, 390
extra_monitor_offset = 0


def reaction_time():
    while True:
        screen_grabber.take_screen_shot()
        current_color = screen_grabber.get_pixel_color(x, y)

        # Check if pixel is red
        if current_color == mac_red_color:
            while True:
                # Wait until changes to green
                screen_grabber.take_screen_shot()
                current_color = screen_grabber.get_pixel_color(x, y)
                if current_color == mac_green_color:
                    pyautogui.click(x + extra_monitor_offset, y)
                    break


if __name__ == '__main__':
    reaction_time()
