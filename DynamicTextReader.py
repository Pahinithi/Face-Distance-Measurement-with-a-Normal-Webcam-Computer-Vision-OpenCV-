import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

# Change camera index if 0 doesn't work; 0 is the default
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Camera could not be initialized")
    exit()

detector = FaceMeshDetector(maxFaces=1)

textList = [
    "Welcome to my AI world.", "I am Nithilan.",
    "This is my", "Face Distance Measurement project.",
    "If you like this Project", "Like, Share", "and Comments."
]


sen = 25  # Sensitivity for depth scaling

while True:
    success, img = cap.read()
    
    # Check if the frame was captured successfully
    if not success or img is None:
        print("Failed to grab frame")
        break

    imgText = np.zeros_like(img)  # Blank image for the text
    img, faces = detector.findFaceMesh(img, draw=False)  # Face mesh detection

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        w, _ = detector.findDistance(pointLeft, pointRight)  # Distance between two face points
        W = 6.3  # Approximate width of face in cm

        # Calculate the distance (depth) of the face from the camera
        f = 840  # Focal length (adjust as necessary for calibration)
        d = (W * f) / w  # Depth equation
        print(f"Depth: {d} cm")

        # Display the depth information on the image
        cvzone.putTextRect(img, f'Depth: {int(d)} cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)

        # Display dynamic text based on distance
        for i, text in enumerate(textList):
            singleHeight = 20 + int((int(d/sen)*sen) / 4)
            scale = 0.4 + (int(d/sen)*sen) / 75
            cv2.putText(imgText, text, (50, 50 + (i * singleHeight)),
                        cv2.FONT_ITALIC, scale, (255, 255, 255), 2)

    # Stack the images (original and text) for display
    imgStacked = cvzone.stackImages([img, imgText], 2, 1)

    # Show the final stacked image
    cv2.imshow("Image", imgStacked)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
