

Then provide your commands.
Make sure to include as much detail as possible, as well as information about what state of the world is required before the action can begin.

@end


@section robot_task_analysis_task2
@ttitle 2. Robot Task Analysis: Assembly

You successfully completed the program for the robot.
Unfortunately, when we started the robot, it started acting rather strangely:

```
# > robot.put("gripper above puck")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: robot
```

It seems that you must have written some code to remove `robot`!

You also forgot to finish writing the `assembly` function, which is the most important of them all!

I have provided you with your code from last time, but it seems to be missing something...
Can you add `assembly` to the code, or fix the original?

@begin

# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle