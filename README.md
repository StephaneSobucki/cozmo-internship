# Faulty Robot

The idea behind this project is finding out whether kids can learn from observing a robot making mistakes. For example, in the context of geometry the robot can wrongly classify quadrilaterals. For this project, we used the robot Cozmo and developped an app in which we can specify what the robot will do (pushing cubes or not) and if it makes mistakes or not.

## Prerequisites

* Cozmo
* Cozmo App
* Phone or tablet
* Python 3.5.1 or later
* pip for Python 3 (Python package installer)
* adb for Android
* iTunes for IOS

## How to use

1. Download and install python3 https://www.python.org/downloads/
2. `git clone https://github.com/StephaneSobucki/cozmo-internship.git`
3. `pip3 install -r "requirements.txt"` to install dependencies
4. For Android follow instructions on http://cozmosdk.anki.com/docs/adb.html
5. For IOS install iTunes
6. Get the Cozmo app on your phone/tablet
7. Connect your phone/tablet to your computer (for android, set the connection in file transfer mode)
8. Connect your phone/tablet to Cozmo WiFi (Move Cozmo's lift up and down to display the password)
9. Run the Cozmo app and go to SDK mode
10. Run `python3 main.py`
