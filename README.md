# Face Distance Measurement with a Normal Webcam

This project demonstrates real-time face distance measurement using a normal webcam. The program detects a face, measures the distance between two facial points, and calculates the depth of the face from the camera using computer vision techniques. Additionally, it displays dynamic text messages based on the measured distance.



## Features

- **Real-time face mesh detection**: Detects facial landmarks using the `cvzone` and `FaceMesh` modules.
- **Distance measurement**: Calculates the depth of the face from the camera using facial landmarks and known focal length.
- **Dynamic text display**: Shows personalized text messages that change according to the face's distance from the camera.
- **Webcam support**: Works with a normal webcam for face detection and distance measurement.

## Demo

Here's a live demo of the project in action:

- [Live Demo](https://drive.google.com/file/d/1lNvFixgGp7SV2iMiicfzDxp6Rgt6qR-w/view?usp=sharing)

## Installation

To run this project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Pahinithi/Face-Distance-Measurement-with-a-Normal-Webcam-Computer-Vision-OpenCV-
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Face-Distance-Measurement
    ```

3. **Install the required dependencies**:
    You can install the necessary libraries using `pip`:
    ```bash
    pip install opencv-python opencv-python-headless cvzone
    ```

4. **Run the project**:
    ```bash
    python3 DynamicTextReader.py
    ```

    Alternatively, you can run the other file:
    ```bash
    python3 FaceDepthMeasurement.py
    ```

## Project Structure

```
Face-Distance-Measurement/
│
├── DynamicTextReader.py       # Main file with dynamic text display based on face distance
├── FaceDepthMeasurement.py    # Basic face depth measurement without text display
└── README.md                  # This file
```

## How it Works

1. **Face Detection**: The application uses the `cvzone.FaceMeshModule` to detect facial landmarks. It identifies two points, one on the left cheek (Point 145) and one on the right cheek (Point 374).
   
2. **Distance Measurement**: The distance between these two points is measured, and based on the known width of an average human face (approx. 6.3 cm), the depth of the face is calculated using the equation:
    ```
    Depth (d) = (W * f) / w
    ```
    where:
    - `W` is the actual width of the face (6.3 cm),
    - `f` is the focal length of the camera (pre-calibrated as 840),
    - `w` is the measured pixel distance between the two face points.

3. **Dynamic Text Display**: Text messages are dynamically displayed on the screen based on the calculated distance, making the interaction more engaging.

## Screenshots

<img width="1728" alt="CV09" src="https://github.com/user-attachments/assets/2e70253d-4861-4c8e-a19d-18ec182191b9">


## Technologies Used

- **OpenCV**: For capturing webcam input and image processing.
- **cvzone**: A library that simplifies the usage of OpenCV for face detection and distance measurement.
- **NumPy**: For efficient numerical computations and array manipulations.

## Future Improvements

- Calibration system for the focal length to make the application work with various camera types.
- Adding a UI to select different sensitivity levels for distance measurement.
- Multi-face support and improved dynamic text features.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Special thanks to the creators of the `cvzone` and `OpenCV` libraries for simplifying computer vision tasks.

## Contact

For any questions or support, please contact:

- **Name**: Pahirathan Nithilan
- **Email**: [nithilan32@gmail.com](mailto:nithilan32@gmail.com)
- **GitHub**: [Pahinithi](https://github.com/Pahinithi)


