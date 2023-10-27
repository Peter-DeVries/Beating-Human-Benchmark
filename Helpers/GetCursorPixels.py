import pyautogui
import time


def print_cursor_position(interval=1):
    try:
        while True:
            # Get the current cursor position
            x, y = pyautogui.position()

            # Print the cursor position
            print(f"Cursor Position: x={x}, y={y}")

            # Wait for the specified interval (in seconds)
            time.sleep(interval)
    except KeyboardInterrupt:
        # Exit the loop if you press Ctrl+C
        pass


# Call the function with an optional interval (default is 1 second)
if __name__ == '__main__':
    print_cursor_position()
