Libraries required:
 - mss
 - numpy
 - cv2 (OpenCV)
 - pyautogui
 - "Helpers" folder must also be available

AimTrainer.py starts by waiting for the "Aim Trainer" screen to appear on primary (or targeted)
monitor. It will then start taking screenshots using mss for fastest reaction times possible. It will then
click on all targets and stop once the "Save Score" button appears. It recognizes the targets by their
light blue color and the stop button by its yellow color.

![Percentile Aim Trainer](https://github.com/Peter-DeVries/Beating-Human-Benchmark/assets/71617666/384655c5-5bb2-4b15-b163-cce4d4c23251)

**Note: Width and Height must be changed to targeted monitor resolution. Target and Stop RGB values
might also need to be changed based on machine.**
