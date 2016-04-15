from collections import deque
import imutils
import Puck
import cv2
import numpy as np


class Tracker:
    lowerLimit = None
    upperLimit = None
    minRadius = None
    maxRadius = None
    pts = None
    buffer = 64
    frameName = None

    def __init__(self, lower_limit, upper_limit, min_radius, max_radius, frame_name):
        self.lowerLimit = lower_limit
        self.upperLimit = upper_limit
        self.minRadius = min_radius
        self.maxRadius = max_radius
        self.pts = deque(maxlen=self.buffer)
        self.frameName = frame_name

    def track(self, frame, table):
        # resize the frame, blur it, and convert it to the HSV
        # color space
        frame = imutils.resize(frame, height=400)

        frame = cv2.medianBlur(frame, 3, frame)
        frame = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, self.lowerLimit, self.upperLimit)
        mask = cv2.erode(mask, None, iterations=1)
        mask = cv2.dilate(mask, None, iterations=1)
        cv2.imshow("Mask_" + self.frameName, mask)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        for contour in contours:
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            if radius < self.minRadius or radius > self.maxRadius:
                continue

            m = cv2.moments(contour)
            center = (int(m["m10"] / m["m00"]), int(m["m01"] / m["m00"]))
            puck = Puck.Puck(center, radius)
            # TODO: NOOOO! JUST NOOO!
            if self.frameName == "red":
                table.redPucks.append(puck)
            else:
                table.greenPucks.append(puck)

        # self.render(contours, frame)

    def render(self, contours, frame):
        for contour in contours:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            # c = max(greenContours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            m = cv2.moments(contour)
            if not m["m00"]:
                continue

            center = (int(m["m10"] / m["m00"]), int(m["m01"] / m["m00"]))

            # only proceed if the radius meets a minimum size
            if self.minRadius < radius < self.maxRadius:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # update the points queue
            self.pts.appendleft(center)

        # loop over the set of tracked points
        for i in xrange(1, len(self.pts)):
            # if either of the tracked points are None, ignore
            # them
            if self.pts[i - 1] is None or self.pts[i] is None:
                continue

            # otherwise, compute the thickness of the line and
            # draw the connecting lines
            thickness = int(np.sqrt(self.buffer / float(i + 1)) * 2.5)
            cv2.line(frame, self.pts[i - 1], self.pts[i], (0, 0, 255), thickness)

        # show the frame to our screen
        frame = cv2.flip(frame, 1)
        cv2.imshow("Frame_" + self.frameName, frame)
