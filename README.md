# AugmentedReality
Simple AR algorithm to display a custom warped image on top of an aruco board
![Alt text](utils/frame_aruco.png?raw=true "Title")
*Fig. 1 - frame without applying AR algorithm*
![Alt text](utils/frame_aruco_ar.png?raw=true "Title")
*Fig. 2 - After applying AR*

## About:
This simple python program uses your webcam and tries to find an aruco board in the frame. if it does, it replaces it with a custom image. Inside this repo theres a testing iamage (escanor.jpg), but you can use whatever image you want by passing it as an argument when running the script.

## Requirements
* Python 3.5 or greater;
* Opencv library.

To run the program:
```
$ python ar.py <your_img>
```

## How the code works:
At each frame of the video, the program tries to find the four corner markers of a 5x7 aruco board. The image below shows the board used:
![Alt text](utils/board_aruco_57.png?raw=true "Title")
After finding the four corners, it gets the coordinates on the frame, and applies an homography of your cusom image to these coordinates. Combining the warped image into your frame replaces the aruco board with your custom image. The results i've got are shwon in the start of this document


