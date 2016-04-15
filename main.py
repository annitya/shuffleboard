import argparse
import cv2
import Table
import os
import Tracker
import json

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points

# grab a reference to the video file
if args.get("video", False):
    camera = cv2.VideoCapture(args["video"])
# if a video path was not supplied, grab the reference to the webcam
else:
    camera = cv2.VideoCapture(0)

greenTracker = Tracker.Tracker((45, 75, 30), (105, 255, 180), 10, 40, "green")
redTracker = Tracker.Tracker((130, 105, 170), (200, 255, 255), 10, 40, "red")

greenScore = 0
redScore = 0
# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    edgeOffset = 50  # TODO: Some cleverly detected value.

    table = Table.Table(edgeOffset)
    greenTracker.track(frame, table)
    redTracker.track(frame, table)

    # if we are viewing a video and we did not grab a frame, then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    newGreenScore = table.get_green_score()
    newRedScore = table.get_red_score()
    if newGreenScore != greenScore or newRedScore != redScore:
        os.system("clear")
        print "Green score of: " + str(newGreenScore)
        print "Red score of: " + str(newRedScore)
        number_of_pucks = len(table.greenPucks) + len(table.redPucks)
        print "Pucks on table: " + str(number_of_pucks)
        greenScore = newGreenScore
        redScore = newRedScore
        with open('data.json', 'w') as outfile:
            json.dump([greenScore, redScore, number_of_pucks], outfile)

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
