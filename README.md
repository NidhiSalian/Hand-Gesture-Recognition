# Hand-Gesture-Recognition
A few simple applications for hand gesture recognition with OpenCV and Python. 

## About
I've been trying to learn to learn a little more about human computer interaction and thought I'd start off with this simple project.
All I've got to work with is the VGA nose cam on my laptop though, and it's hard to judge how well/ badly my code would perform otherwise on standard/good feeds.

If you use my code, let me know what you think! You can write to me at nidhisalian08@gmail.com or open an issue with the label feedback. 

## Setup

This project was developed using VS Code and Python 3.7.4
I'd recommend using a virtual environment to prevent conflicting package dependencies across different projects. You can find some helpful hints in the [tips section](./Tips.md).

Package dependencies are listed program-wise below.

## Usage

1. __hand_to_mouse.py__

   Control your cursor with your hands! This neat little program uses OpenCV haar cascades trained for fist/palm detection from a video feed(in this case, my webcam), and maps it to the mouse controller (move/click respectively).

   Package Used : PyAutoGUI(v0.9.48), imutils(v0.5.3), opencv-contrib-python(v4.1.0.25), numpy(1.17.4) 

   Simple pip install should work for all of these, including any dependencies.


## Acknowledgements
Pre-trained Haar Cascades from [ravindlivewire](https://github.com/Aravindlivewire). Found them [here](https://github.com/Aravindlivewire/Opencv/tree/master/haarcascade). Pretty old, but they work. If you find better detectors or train your own

## License

[MIT License](./LICENSE)
