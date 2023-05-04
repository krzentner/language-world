

## 2. Code Examples and Hints

You can also read about some other tasks below.

For the tasks with pictures, click to switch between different steps of the task.
When you click on a step, the program that does that step will be shown below
the picture, and you can click on its steps.

For instance, you can try this one:

<div style="width:372px">
<img src="images/push-task.jpg" style="border:2px solid black"/>
<img src="images/push-task1.jpg" style="border:2px solid black;display:none"/>
<img src="images/push-task2.jpg" style="border:2px solid black;display:none"/>
<img src="images/push-task3.jpg" style="border:2px solid black;display:none"/>
</div>

```
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the target location")
```



# Appendix

This is a demonstration of how we check if the robot's gripper is in a