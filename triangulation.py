import cv2
import numpy as np

# Known parameters
object_width = 10  # Width of the object in centimeters
focal_length = 500  # Focal length of the camera in pixels

def calculate_distance(image_points):
    # Convert image points to homogeneous coordinates
    image_points_homogeneous = np.hstack((image_points, np.ones((len(image_points), 1))))

    # Triangulation
    A = np.zeros((2, 4))
    distances = []

    for i in range(len(image_points_homogeneous) - 1):
        A[0, :] = image_points_homogeneous[i, :]
        A[1, :] = -image_points_homogeneous[i + 1, :]
        _, _, V = np.linalg.svd(A)
        X = V[-1, :3] / V[-1, -1]
        distance = object_width * focal_length / np.abs(X[0])
        distances.append(distance)

    return distances

# Read the image
image = cv2.imread("images/image.jpeg")

# Define image points (e.g., from object detection or feature matching)
image_points = np.array([[100, 200], [200, 250], [300, 220], [400, 180]])

# Calculate distances
distances = calculate_distance(image_points)

# Print the distances
for i, distance in enumerate(distances):
    print("Distance", i+1, ":", distance, "cm")
