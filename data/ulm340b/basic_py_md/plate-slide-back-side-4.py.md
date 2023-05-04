

For more information about the task, type:

```
help('plate_slide_back_side')
```

To submit your code, type:

```
submit_worksheet()
```

For example, you can copy the following code into the interpreter to complete the task:

```
if check("the robot's gripper is not horizontally aligned with plate"):
    robot.push("the gripper left")
if check("the robot's gripper is left of the plate and the robot's gripper is forward aligned with the plate"):
    robot.grab("the plate")
if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not below plate"):
    robot.align("the plate to the goal")
if check("the plate is below the robot's gripper and the robot's gripper is vertically aligned with plate"):
    robot.slide("plate to goal")
if check("the robot's gripper is horizontally aligned with plate and the plate is at goal"):
    robot.place("plate at goal")
```
"""


def plate_slide_back_side(robot):
    if check("the robot's gripper is not horizontally aligned with plate"):
        robot.push("the gripper left")
    if check("the robot's gripper is left of the plate and the robot's gripper is forward aligned with the plate"):
        robot.grab("the plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is not below plate"):
        robot.align("the plate to the goal")
    if check("the plate is below the robot's gripper and the robot's gripper is vertically aligned with plate"):
        robot.slide("plate to goal")
    if check("the robot's gripper is horizontally aligned with plate and the plate is at goal"):
        robot.place("plate at goal")


class Robot(object):

    def place(self, object_and_position):
        pass

    def slide(self, object_and_position):
        pass

    def move(self, target):
        pass

    def reach(self, goal):
        pass

    def put(self, object_and_position):
        pass

    def grab(self, object):
        pass

    def align(self, object_and_position):
        pass

    def push(self, object_and_position):
