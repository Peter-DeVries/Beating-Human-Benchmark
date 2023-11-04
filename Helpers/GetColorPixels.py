from ScreenGrabber import *

screen_grabber = ScreenGrabber(0, 0, 1440, 900, -1)
screen_grabber.take_screen_shot()

x, y = 760, 432


def get_color_pixels():
    print(screen_grabber.get_pixel_color(x, y))


if __name__ == '__main__':
    get_color_pixels()
