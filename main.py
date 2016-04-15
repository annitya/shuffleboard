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

greenTracker = Tracker.Tracker((45, 75, 30), (105, 255, 180), 10, 40)

greenScore = 0
# keep looping
while True:
    # grab the current frame
    (grabbed, frame) = camera.read()

    edgeOffset = 50  # TODO: Some cleverly detected value.

    table = Table.Table(edgeOffset)
    greenTracker.track(frame, table)

    # if we are viewing a video and we did not grab a frame, then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    newGreenScore = table.get_green_score()
    if newGreenScore != greenScore:
        os.system("clear")
        print "Green score of: " + str(newGreenScore)
        print "Pucks on table: " + str(len(table.greenPucks))
        greenScore = newGreenScore
        with open('data.json', 'w') as outfile:
            json.dump(greenScore, outfile)

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
