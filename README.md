# Finger Counting with OpenCV and MediaPipe

This project uses **OpenCV** and **MediaPipe** to create a real-time finger-counting application that works with both hands. The application utilizes the webcam feed to detect hand landmarks and count the number of fingers raised for each hand.

---

## Features

- Real-time hand tracking using MediaPipe Hands.
- Detects finger count for both hands.
- Displays individual finger counts for the left and right hand.
- Displays the total combined finger count.
- Provides a mirrored webcam feed for intuitive interaction.

---

## Requirements

Make sure you have the following dependencies installed:

- Python 3.7 or higher
- OpenCV (`cv2`)
- MediaPipe

You can install the dependencies using the following commands:

```bash
pip install opencv-python
pip install mediapipe
```

---

## How to Run

1. Clone this repository or download the source code.
2. Ensure you have a working webcam connected to your system.
3. Run the `finger_counting.py` script:

```bash
python finger_counting.py
```

4. The application will open a webcam feed window. You can use your hands to see the finger count displayed on the screen.
5. Press `q` to quit the application.

---

## Code Overview

### Key Components:

1. **Hand Detection:**

   - Utilizes MediaPipe Hands for detecting and tracking hand landmarks.
   - Supports detection of both left and right hands.

2. **Finger Counting Logic:**

   - Identifies raised fingers based on landmark positions.
   - Handles the thumb's unique movement for left and right hands.

3. **Real-Time Display:**

   - Draws hand landmarks and connections on the webcam feed.
   - Displays individual finger counts for each hand and a total combined count.

---

## Demo

When you run the script, the application will:

- Open a webcam feed.
- Detect hands and display the finger count for each hand.
- Display the total combined finger count.


---

## Troubleshooting

- **Issue:** Webcam not detected.

  - Ensure your webcam is connected and accessible.
  - Check if another application is using the webcam.

- **Issue:** Finger count is incorrect.

  - Ensure proper lighting for better detection accuracy.
  - Avoid overlapping hands in the webcam feed.


---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Acknowledgments

- **MediaPipe:** For providing robust hand tracking solutions.
- **OpenCV:** For efficient real-time computer vision capabilities.

---

Feel free to fork this repository and contribute to its improvement! If you encounter any issues or have suggestions, please open an issue or submit a pull request.

