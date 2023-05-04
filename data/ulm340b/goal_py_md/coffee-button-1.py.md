

This task is like `button-press-topdown`, so you should copy-and-paste the body
of that function as the basis for your code.
'''

# Coffee

# coffee-button: push the button on the coffee machine
def coffee_button(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with coffee"):
        robot.move_gripper("vertically aligned with coffee", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with coffee"):
        robot.move_gripper("near coffee")

print('### 3.0')
print('Robot, make me some coffee!')
coffee_button(robot)
print(coffee_button.__doc__)
[eod] [code]# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:40:51 2018

@author: aag14
"""

import tensorflow as tf

#Create some variables.
v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", shape=[5])

print(v1.name)
print(v1.shape)

#Assign values
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
print(sess.run(v1))
sess.run(v1.assign([1,2,3]))
print(sess.run(v1))

#Assign op that increments by 1.
add_one = tf.assign(v1, v1 + 1)
sess.run(add_one)
print(sess.run(v1))

#Save to disk
saver = tf.train.Saver()
sess.run(add_one)
saver.save(sess, "/tmp/model.ckpt")


#Restore from disk
sess = tf.Session()
new_saver = tf.train.import_meta_graph("/tmp/model.ckpt.meta")
new_saver.restore