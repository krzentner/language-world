

When you have written the `plate-slide-side` function, please let me know.


'''


def plate_slide_side(robot):

     if check("the robot's gripper is not vertically aligned with plate"):
          robot.put("gripper above plate")
     if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not near plate"):
          robot.grab("plate")
     if check("the robot's gripper is near plate"):
          robot.slide("plate to goal")
     if check("the plate is at the goal"):
          robot.release("plate")




'''

#######################################################################

>>> plate_slide_side(robot)
The robot's gripper is not vertically aligned with plate
The robot's gripper is above the plate
The robot's gripper is near plate
The plate is at the goal

>>> plate_slide_side(robot)
The robot's gripper is above the plate
The robot's gripper is near plate
The plate is at the goal

>>> plate_slide_side(robot)
The robot's gripper is above the plate
The robot's gripper is near plate
The plate is at the goal

>>> plate_slide_side(robot)
The robot's gripper is above the plate
The robot's gripper is near plate
The plate is at the goal

>>> plate_slide_side(robot)
The robot's gripper is above the plate
The robot's gripper is near plate
The plate is at the goal

'''



[eod] [code]import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs

# 初始化模型
def train(learning_rate, step, batch_size, display_step, is_test):
    # 定义输入输出的占位符
    