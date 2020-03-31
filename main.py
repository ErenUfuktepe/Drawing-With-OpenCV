import cv2
import numpy as np
from settings import Settings
import threading


# Global variables.
drawing = False
glob_x, glob_y = -1, -1
# Default variables.
settings = ['pen', (0, 255, 0), 3, 50]


# Drawing circle. Puts circle on the screen.
# Left click puts normal circle.
# Right click puts filled circle.
def draw_circle(event, x, y, flags, param):
    global settings
    # Left click event.
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), settings[3], settings[1], 0)
    # Right click event.
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), settings[3], settings[1], -1)


# Drawing rectangle. Puts rectangle with mouse movements.
def draw_rectangle(event, x, y, flags, param):
    global glob_x, glob_y, drawing, settings
    # Left button click action.
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        glob_x, glob_y = x, y
    # Mouse movement action when clicked.
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (glob_x, glob_y), (x, y), settings[1], -1)
    # Left button release action.
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (glob_x, glob_y), (x, y), settings[1], -1)


# Drawing lines.
def draw_line(event, x, y, flags, param):
    global glob_x, glob_y, drawing, settings
    # Left click button action.
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        glob_x, glob_y = x, y
    # Mouse movement action when clicked.
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (glob_x, glob_y), (x, y), settings[1], settings[2])
            glob_x, glob_y = x, y
    # Left button release action.
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (glob_x, glob_y), (x, y), settings[1], settings[2])


# Opens black screen for drawing.
def drawing_action():
    global settings
    cv2.namedWindow('Paint With OpenCV')
    cv2.moveWindow('Paint With OpenCV', 0, 0)
    while True:
        settings = setting_bar.get_dynamic_settings()
        if settings[0] == 'pen':
            cv2.setMouseCallback('Paint With OpenCV', draw_line)
        elif settings[0] == 'rectangle':
            cv2.setMouseCallback('Paint With OpenCV', draw_rectangle)
        elif settings[0] == 'circle':
            cv2.setMouseCallback('Paint With OpenCV', draw_circle)
        cv2.imshow('Paint With OpenCV', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


setting_bar = Settings()
img = np.zeros((700, 700, 3), np.uint8)
thread = threading.Thread(target=drawing_action, args=())
thread.start()
setting_bar.start()
