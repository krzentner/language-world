

Then, write some if-statements that will perform the task.
''',

'correct': '''
```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")
```
''',

'wrong':
'''
The first line should be:
```
# door-open: pull the door open
```

The second line should be:
```
def door_open(robot):
```

Then, write some if-statements that will perform the task.
''',

'example': '''
```
# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")
```
'''
}
[eod] [code]import math

import tensorflow as tf


def swish(x):
    return x * tf.nn.sigmoid(x)


def conv_norm_activation(inputs,
                         num_outputs,
                         kernel_size=3,
                         activation_fn=tf.nn.relu,
                         weights_initializer=tf.variance_scaling_initializer(),
                         weights_regularizer=None,
                         normalizer_fn=tf.contrib.layers.batch_norm,
                         reuse=None,
                         name=None,
                         scope=None,
                         strides=1):
    """Creates a tensor which consists of a convolutional layer,
    a normalization layer and an activation layer"""

    with tf.variable_scope(scope, default_name=name, reuse=reuse):
        # Convolutional layer
        input_tensor_shape = inputs.get_shape()
        n_input_channels = input_tensor_shape.