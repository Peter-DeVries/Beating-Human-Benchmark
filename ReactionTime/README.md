Libraries required:
 - mss
 - numpy
 - cv2 (OpenCV)
 - pyautogui
 - "Helpers" folder must also be available

ReactionTime.py starts by waiting for the "Reaction Time Test" screen to appear on primary (or targeted)
monitor. It will then start taking screenshots using mss for fastest reaction times possible. It will
wait for screen to be the specified red color and then click upon changing to the specified green color.

![Percentile Reaction Time](https://github.com/Peter-DeVries/Beating-Human-Benchmark/assets/71617666/29d9190f-0d1b-43c4-9767-25da2856f86d)

**Note: Width and Height must be changed to targeted monitor resolution. Red and Green RGB values
might also need to be changed based on machine.**

