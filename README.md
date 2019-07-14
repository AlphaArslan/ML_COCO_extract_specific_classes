# ML_COCO_extract_specific_classes
Extract images and annotations from COCO for specific classes

## Table of contents  
- [Explanation](#explanation)
- [Prerequisites](#prerequisites)
- [Running the code](#running-the-code)



## Explanation
This code basically extracts images and its annotations from COCO dataset for specific classes/categories. The output is formatted to work with [Darknet](https://github.com/AlexeyAB/darknet) branch by [AlexeyAB](https://github.com/AlexeyAB).
This script helps with steps 4 and 5 in [How to train (to detect your custom objects)](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects) in [AlexeyAB](https://github.com/AlexeyAB) repo

<p></p>

However, with some tweaks you can get the desired for format for your own dataset as I considered making the code as scalable and modular as possible.

<p></p>

## Prerequisites
- COCO dataset downloaded. use [this guide](https://pjreddie.com/darknet/yolo/#train-coco)
- [Darknet](https://github.com/AlexeyAB/darknet) branch by [AlexeyAB](https://github.com/AlexeyAB).

<p></p>

## Running the code
change these lines to folder location
```python
COCO_FOLDER    = "/path/to/coco/"
DARKNET_FOLDER = "/path/to/darknet/"
```

change the list to the desired class names
```python
cat_names = ['car', 'bus', 'truck', 'traffic light' , 'stop sign', 'parking meter']
```
