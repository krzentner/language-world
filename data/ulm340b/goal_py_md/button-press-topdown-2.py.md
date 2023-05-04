

Then add lines of code by filling in the blanks.
Some helpful code snippets are given below.

```
# Steps:
#  1. Put gripper above the button
#  2. Lower the gripper onto the button
#  3. Slide the gripper into the button
# If the button is left of the gripper, we should move the gripper above the
# button.
if check("the robot's gripper is not vertically aligned with the button"):
    robot.move_gripper("vertically aligned with the button")
# If the gripper is vertically aligned with the button, we can move the gripper
# down to put it near the button to start pushing it down.
if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
    robot.move_gripper("above the button")
# The button is small enough that we should check the gripper is left of the
# button instead of vertically aligned with the button.
if check("the robot's gripper is not left of the button"):
    robot.move_gripper("near the button")


```


# In[ ]:


# button-press-topdown: push the button down from above
def button_press_topdown(robot):
# Steps:
#  1. Put gripper above the button
#  2. Lower the gripper onto the button
#  3. Slide the gripper into the button
# If the button is left of the gripper, we should move the gripper above the
# button.
if check("the robot's gripper is not vertically aligned with the button"):
    robot.move_gripper("vertically aligned with the button")
# If the gripper is vertically aligned with the button, we can move the gripper
# down to put it near the button to start pushing it down.
if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
    robot.move_gripper("above the button")
# The button is small enough that we should check the gripper is left of the
# button instead of vertically aligned with the button.
if check("the robot's gripper is not left of the button"):
    robot.move_gripper("near the button")


# ## 4. Describe what is happening

# In[ ]:


# This function lets you know when you're done with each problem.
def check(condition):
   