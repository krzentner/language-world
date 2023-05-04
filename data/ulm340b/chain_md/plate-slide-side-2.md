

The task `stick-push` requires the robot to slide the stick to the target location.
To slide the stick to the target location reliably, what steps the robot should perform?

"""
[eod] [code]import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
import os
import random
import time
import cv2
from utils import label_map_util
from utils import visualization_utils_color as vis_util

def detect_with_video(graph,video_cap, label_text,min_score_thresh = 0.6):

    # Get handles to input and output tensors
    ops = graph.get_operations()
    all_tensor_names = {output.name for op in ops for output in op.outputs}
    tensor_dict = {}
    for key in [
        'num_detections', 'detection_boxes', 'detection_scores',
        'detection_classes', 'detection_masks'
    ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
            tensor_dict[key] = graph.get_tensor_by_name(
                tensor_name)

    image_tensor = graph.get_tensor_by_name('image_tensor:0')

    fps = 0.0
    count = 0
    while(True):
        start_time = time.time()
        if video_cap.isOpened()==False:
            print("Unable to decode video feed")
            return 0
        count +=1
        print("reading camera feed")
        ret, image_np = video_cap.read()


        if image_np is not None:
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = np.array([image_np])
            


        # Actual detection.
        output_dict = session.run(tensor_dict,
                                  feed_dict={image_tensor: image_np_expanded})
        # print(output_dict['num_detections'])

        # Visualization of the results of a detection.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
