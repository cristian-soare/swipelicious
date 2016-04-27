#!/usr/bin/python2

import os
import sys
import cv2

ball_window = (1400, 1750)
bask_window = (230, 1300)

def get_ball(img):
	img = img[ball_window[0]:ball_window[1], :]
	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, 
		param1=50, param2=30, 
		minRadius=0, maxRadius=0)
	return (int(circles[0][0][0]), int(circles[0][0][1] + ball_window[0]))

def get_basket(img):
	img = img[bask_window[0]:bask_window[1],:]
	edges = cv2.Canny(img, 50, 150, apertureSize=3)

	_,contours,_ = cv2.findContours(edges, 1, 2)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		if len(approx) == 4:
			break

	fx = lambda x: x[0][0]
	fy = lambda x: x[0][1]
	xmin = min(map(fx, approx)); xmax = max(map(fx, approx))
	ymin = min(map(fy, approx)); ymax = max(map(fy, approx))

	return (int((xmin + xmax) / 2), int((ymin + ymax) / 2) + bask_window[0])

if __name__ == '__main__':
	img = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)
	bimg = cv2.medianBlur(img, 5)

	(ax, ay) = get_basket(bimg)
	(bx, by) = get_ball(bimg)

	with open(sys.argv[2], 'w') as f:
		f.write(str(ax) + ' ' + str(ay) + '\n')
		f.write(str(bx) + ' ' + str(by) + '\n')

	# cv2.circle(bimg, (ax, ay), 10, (0, 0, 255), 10)
	# cv2.circle(bimg, (int(bx), int(by)), 10, (0, 0, 255), 10)

	# cv2.imwrite(sys.argv[2], bimg)
	# os.system('kde-open ' + sys.argv[2])
