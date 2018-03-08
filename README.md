![capture](https://user-images.githubusercontent.com/36031736/36649655-69b84130-1ad1-11e8-8c55-3bdcbb61a471.JPG)

# Computer_Google_game
## Project Objective: 

The project objective is simply to build a program to autonomously play the google game. For the core of this prject I want to use Python and OpenCV. Then I shall expand to something like a neural network to test how well that does. 
Game URL: http://www.trex-game.skipser.com/

## Learning Goals:

* Familiarity with Coding in python
* Familiarity with OpenCV Library
* Familiarity with training and setting up Nueral Networks

## Tutorials

OpenCV Template matching:
https://pythonprogramming.net/template-matching-python-opencv-tutorial/?completed=/canny-edge-detection-gradients-python-opencv-tutorial/

## Stages:
- [X] 1 Code Foundational Project
- [X] 2 Configure Screen Capture
- [ ] 3 Code Object Detection
- [ ] 4 Test Code
- [ ] 5 Study Nueral networking
- [ ] 6 Train Nueral network
- [ ] 7 Test new code
### Stage 1 Code Foundational Project
I started out by breaking this project into 6 coded sections.  

The first is the timing section. This section consists of just a while loop timer that counts approximately 5 seconds before continuing to the rest of the program. This section is needed because it will give time for the human to quickly navigate to the right browser to start the game and center the browser on the screen.  

The second is the Image Grabbing. In this section some library will be used to capture images of the screen for later processing. This section will also be used to initailize images. For example turning them to gray scale for later processing. 

The third section is the object detection. This is the section that will detect where the incoming obstacles are, and highlight them with boxes.

The fourth section deals with the decision making. This code will judge when the player needs to take an action to avoid an incomming obstacle. For example if it detects a cactus coming in close it will press the space key to make the character clear the obstacle. 

The fifth and Sixth sections deal with human interface debugging. This will allow me to see how fast the screen grabber is getting images, how well the object detector is detecting the incoming obstacles. This will serve to help me build the code better, and combat problems as they come up. Hopefully in the final version you could remove this portion of the code and still have a working program. 

### Stage 2 Configure Screen Capture

I first used pyautogui to take screenshots, but I find it to operate really slowly at approximately 1 frame a second. This is way to slow to play any but the slowest online games. I will continue to search, and work on a solution for this problem. For now I can will continue to the object detection and decision making stages.

Possible Solutions:
- Use a c++ algorithm to capture the screen and just write into a jpeg file, and just have the python just read off it.
- Switch to windows to make use of ImageGrab from the Pil Library
- Use a camera for capturing needs

Solution:

In the end after researching and being stuck on this one issue for perhaps a month and a half I fixed it. the solution was simple, as I was on a two moniter system with one HDPI moniter the screen capture took a long time to capture the pixels. When I remove the HDPI moniter the speed increases by 400% to around 5.55 fps. While this frame count still leads something to be desired it is a signifigant improvement from my sometimes 0.83 fps. I will come back to address a few fixs to this issue in later builds, especially as in the later levels of this game high frame count becomes more and more needed. 

![slow loops](https://user-images.githubusercontent.com/36031736/37132612-1c92a38a-22c1-11e8-9b02-d67bc0feed87.png)
This image shows the slow loops that it was taken. This is time taken of the Capture each image. sS 1 divided by the time taken calculates the frame rate. 

![fastloop](https://user-images.githubusercontent.com/36031736/37132567-dabc0578-22c0-11e8-89dc-3a14119da2e3.png)
This image showcases the faster frame rate

### Stage 3 Code Object Detection:

To do object detection I originally tried to do OpenCVs template matching. This will slide a template image over the picture searching for matches in the neighboring pixels. This method immediately ran into a couple problems. The first is that there are multiple objects to watch out for, as sometimes cacti come at the player in groups of three. Secondly this doesn't lead to any portability as you have to use exact size demension for the template image to match what is going on the screen. This would likely mean that different computers or even internet browsers would have to set up matching templates to their game enviroment. All in all it wouldn't lead to robust code. 
