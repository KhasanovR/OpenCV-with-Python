#  OpenCV with Python

## Tasks

1. From image moon-photography-camera.jpg manually find the position of a people and a moon and draw rectangles as following. Make sure to choose correct color and line thickness.
	
	![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_1.jpg?raw=true)
	
	Save resulted image.
2. Using ROI separate moon-photography-camera.jpg image into two different images as following:
	
	![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_2[part_1].jpg?raw=true) ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_2[part_2].jpg?raw=true) 
	
	Save resulted images
3. First decrease the size of an image then create blurred and sharpen images from flower.jpg image. Save resulted images
4. Convert the image to the grayscale and using histogram equalization increase the brightness of the dark.jpg image. Save resulted images

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required wrappers.

```bash
pip install -r requiremnts.txt
```

#### or

Use [tutorial_py_table_of_contents_setup](https://raw.githubusercontent.com/opencv/opencv/blob/master/doc/py_tutorials/py_setup) to install OpenCV from the official documentary.


## Usage

``` bash
	python openCV.py
```


## Results

#### Task 1

| Original | Generated |
| -------- | --------- |
|![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/original/moon-photography-camera.jpg?raw=true "Task 1 Original") | ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_1.jpg?raw=true "Task 1 Generated") |

#### Task 2

| Original | Generated[Part 1] | Generated[Part 2] |
| -------- | ----------------- | ----------------- |
|![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/original/moon-photography-camera.jpg?raw=true "Task 2 Original") | ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_2[part_1].jpg?raw=true "Task 2 Generated Part 1") | ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_2[part_2].jpg?raw=true "Task 2 Generated Part 2") |
	

#### Task 3

| Original | Generated[Part 1] | Generated[Part 2] |
| -------- | ----------------- | ----------------- |
|![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/original/flower.jpg?raw=true "Task 3 Original") | ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_3[part_1].jpg?raw=true "Task 3 Generated Part 1") | ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_3[part_2].jpg?raw=true "Task 3 Generated Part 2") |

#### Task 4

| Original | Generated |
| -------- | --------- |
|![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/original/dark.jpg?raw=true "Task 4 Original") | ![alt text](https://raw.githubusercontent.com/KhasanovR/OpenCV-with-Python/master/img/generated/task_4.jpg?raw=true "Task 4 Generated") |
	