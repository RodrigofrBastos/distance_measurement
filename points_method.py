import cv2
import numpy as np

# Global variables
rectangle = False  # Indicates if drawing the rectangle is in progress
top_left_pt = (-1, -1)  # Top-left corner of the rectangle
bottom_right_pt = (-1, -1)  # Bottom-right corner of the rectangle

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global rectangle, top_left_pt, bottom_right_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        rectangle = True
        top_left_pt = (x, y)
        print("top_left_pt:", top_left_pt)
             
    elif event == cv2.EVENT_LBUTTONUP:
        rectangle = False
        bottom_right_pt = (x, y)
        print("bottom_right_pt:", bottom_right_pt)
        
        # Draw the rectangle
        cv2.rectangle(image, top_left_pt, bottom_right_pt, (0, 255, 0), 2)
        cv2.imshow("Rectangle", image)

# Create a black image
image = cv2.imread("images/image.jpeg")
cv2.imshow("Rectangle", image)

# Set the callback function for mouse events
cv2.setMouseCallback("Rectangle", draw_rectangle)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

