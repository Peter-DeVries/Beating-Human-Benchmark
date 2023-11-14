from ScreenGrabber import *


# Take a screenshot using mss and show it for 5 seconds
def get_monitor_screen_shot():
    screen_grabber = ScreenGrabber(0, 0, 2560, 1440, -1)
    screen_grabber.take_screen_shot()
    screen_grabber.show_screen_shot()


if __name__ == '__main__':
    get_monitor_screen_shot()
