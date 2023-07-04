import cv2

# Global variables to store the coordinates of the selected point
point = (-1, -1)

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global point
    
    if event == cv2.EVENT_LBUTTONDOWN:
        point = (x, y)
        print("Selected point:", point)

# Read the image
image = cv2.imread("images/image.jpeg")

# Create a window and bind the mouse callback function to it
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

while True:
    
    cv2.imshow("Image", image)
    cv2.circle(image,point,1,(0,255,0),5,-1)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Print the final selected point after the window is closed
print("Final selected point:", point)

# Release the OpenCV windows and resources
cv2.destroyAllWindows()
