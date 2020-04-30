#########################################
#										#
# 	Course	 :	Capstone Design 		#
# 	Code	 :	openCV.py 				#
# 	Created  : 	2020-04-15 11:07 PM		#
# 	Author   : 	Rakhmatjon Khasanov		#
#	ID 		 :	U1610183				#
#	Section# :	1						#
#	HomeWork#:	4						#
#										#
#########################################

import os			#	load module os
import cv2			#	load module cv2
import numpy as np 	#	load module numpy


def task_1(img):	# task 1 of the homework
	
	cv2.imshow('Task 1 Original', img) 	# shows the image
	cv2.waitKey(1000)				  	# for 1000 msec					

	img = cv2.rectangle(img, (70, 90), (200, 315), (0, 0, 255), 3) 	# draws a rectangle with 3px-red-border 	
	img = cv2.rectangle(img, (392, 122), (432, 162), (0, 0, 0), 1)	# draws a rectangle with 1px-black-border

	cv2.imwrite('img/generated/task_1.jpg', img)	# writes the generated image
	cv2.imshow('Task 1', img)	# shows the image
	cv2.waitKey(1000)			# for 1000 msec	

	img = np.vstack((tmp, img))	# concatenates a tuple of images vertically
	cv2.imwrite('img/generated/task_1[combined].jpg', img)	# writes the generated image
	cv2.imshow('Task 1 Combined', img)	# shows the image
	cv2.waitKey(1000)					# for 1000 msec	
	
	return 	# terminate the function


def task_2(img):	# task 2 of the homework

	cv2.imshow('Task 2 Original', img) 	# shows the image
	cv2.waitKey(1000)					# for 1000 msec	
	
	part_1 = img[90:315, 70:200]	# gets the region of interest 
	cv2.imwrite('img/generated/task_2[part_1].jpg', part_1)	# writes the generated image
	cv2.imshow('Part 1 of Task 2', part_1)	# shows the image
	cv2.waitKey(1000)						# for 1000 msec	

	part_2 = img[100:300, 220:500]	# gets the region of interest 
	cv2.imwrite('img/generated/task_2[part_2].jpg', part_2)	# writes the generated image
	cv2.imshow('Part 2 of Task 2', part_2)	# shows the image
	cv2.waitKey(1000)						# for 1000 msec	
	
	return	# terminate the function


def task_3(img):	# task 2 of the homework

	height, width = img.shape[:2] # gets height & width
	img = cv2.resize(img, (width // 4, height // 4), interpolation=cv2.INTER_CUBIC)	# decreases the size of the image 4 times 

	cv2.imshow('Task 3 Original', img)	# shows the image
	cv2.waitKey(1000)					# for 1000 msec	

	blurred = cv2.blur(img, (5, 5))	# blurs the image
	cv2.imwrite('img/generated/task_3[part_1].jpg', blurred)	# writes the generated image
	cv2.imshow('Part 1 of Task 3', blurred)	# shows the image
	cv2.waitKey(1000)						# for 1000 msec	

	sharpened = cv2.filter2D(img, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32))	# sharpens the image
	cv2.imwrite('img/generated/task_3[part_2].jpg', sharpened)	# writes the generated image
	cv2.imshow('Part 2 of Task 3', sharpened)	# shows the image
	cv2.waitKey(1000)							# for 1000 msec	

	img = np.vstack((img, blurred, sharpened))	# concatenates a tuple of images vertically
	cv2.imwrite('img/generated/task_3[combined].jpg', img)	# writes the generated image
	cv2.imshow('Task 3 Combined', img)	# shows the image
	cv2.waitKey(1000)					# for 1000 msec	

	return # terminate the function


def task_4(img):	# task 2 of the homework

	cv2.imshow('Task 4 Original', img)	# shows the image
	cv2.waitKey(1000)					# for 1000 msec	

	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	# converts to greyscale image
	
	cv2.imshow('Task 4 in Greyscale', img)	# shows the image
	cv2.waitKey(1000)						# for 1000 msec	

	equ = cv2.equalizeHist(img) # Equalizes the histogram of a grayscale image.
	cv2.imwrite('img/generated/task_4.jpg', img)	# writes the generated image
	cv2.imshow('Task 4', img)	# shows the image
	cv2.waitKey(1000)			# for 1000 msec	

	img = np.hstack((img, equ))	# concatenates a tuple of images horizontally
	cv2.imwrite('img/generated/task_4[combined].jpg', img)	# writes the generated image
	cv2.imshow('Task 4 combined', img)	# shows the image
	cv2.waitKey(1000)					# for 1000 msec	

	return # terminate the function


if __name__ == '__main__': # executes only the part below of this script

	if not os.path.exists('img/generated'):	# checks if the folder doesn't exists
	    os.makedirs('img/generated')		# if the condition is true, then create a folder

	task_1(cv2.imread('img/original/moon-photography-camera.jpg')) 	# call function task_1

	task_2(cv2.imread('img/original/moon-photography-camera.jpg'))	# call function task_2

	task_3(cv2.imread('img/original/flower.jpg'))					# call function task_3

	task_4(cv2.imread('img/original/dark.jpg'))						# call function task_4
