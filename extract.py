##################### Import
from pycocotools.coco import COCO
import shutil
import os

##################### consts
COCO_FOLDER    = "/path/to/coco/"
DARKNET_FOLDER = "/path/to/darknet/"
our_coco = COCO(COCO_FOLDER+'annotations/instances_train2014.json')

cat_names = ['car', 'bus', 'truck', 'traffic light' , 'stop sign', 'parking meter']

##################### vars
class_counter = 0
image_counter = 0

image_width  = 0                        # in pixels
image_height = 0                        # in pixels
x_center     = 0                        # in pixels
y_center     = 0                        # in pixels
bbox_width   = 0                        # in pixels
bbox_height  = 0                        # in pixels
x_topleft    = 0                        # in pixels
y_topleft    = 0                        # in pixels


##################### main
if __name__ == '__main__':
    cat_ids = our_coco.getCatIds(catNms=cat_names)
    train_file = open(DARKNET_FOLDER+"data/train.txt", "w+")


    for cat_id in cat_ids:
        # get annotations for a specific class
        ann_ids = our_coco.getAnnIds(catIds= cat_id)
        anns = our_coco.loadAnns(ann_ids)

        for ann in anns:
            x_topleft   = ann['bbox'][0]
            y_topleft   = ann['bbox'][1]
            bbox_width  = ann['bbox'][2]
            bbox_height = ann['bbox'][3]

            # print("{}  {}  {}  {}".format(x_topleft, x_topleft, bbox_width, bbox_height))

            img_id = ann['image_id']
            img = our_coco.loadImgs(ids=img_id)
            img_name     = img[0]['file_name']
            image_width  = img[0]['width']
            image_height = img[0]['height']

            # print("{}  {}".format(image_width, image_height))

            x_center = x_topleft + bbox_width/2
            y_center = y_topleft + bbox_height/2

            #darknet annotation format
            a = format(x_center/image_width , '.6f')
            b = format(y_center/image_height , '.6f')
            c = format(bbox_width/image_width , '.6f')
            d = format(bbox_height/image_height , '.6f')

            print("{} {} {} {} {}".format(class_counter, a, b, c, d))


            # copy image
            shutil.copy(COCO_FOLDER + "images/train2014/" + img_name, DARKNET_FOLDER + "data/obj/" + img_name)

            # add image name to train.text
            train_file.write("data/obj/{}\n".format(img_name))

            # create text file for annotation
            with open(os.path.splitext(DARKNET_FOLDER + "data/obj/" + img_name)[0]+".txt" , "w+") as fp:
            	fp.write("{} {} {} {} {} \n".format(class_counter, a, b, c, d))

            image_counter += 1
            print("{}/{} Image .. {}/{} Class\n".format(image_counter, len(anns), class_counter+1, len(cat_names)))

        image_counter = 0
        class_counter += 1

    train_file.close()
