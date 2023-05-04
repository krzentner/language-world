

Now please write code below. The robot needs to do the following steps:

- Move the gripper above the cube
- Close the gripper around the cube
- Lift the cube off the ground
- Slide the cube sideways to the goal location
- Release the gripper

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper above the cube")
    if check("the robot's gripper is open and not around cube"):
        robot.close("gripper around cube")
    if check("the robot's gripper is around cube and the cube is on the table"):
        robot.lift("cube off the table")
    if check("the robot's gripper is around the cube and the cube is not on the table"):
        robot.move("the cube sideways to the goal")
    if check("the cube is at the goal"):
        robot.release("gripper")
```

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is not above the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    if check("the robot's gripper is around the cube and the cube is on the table"):
        robot.lift("cube off the table")
    if check("the robot's gripper is around the cube and the cube is not on the table"):
        robot.slide("the cube sideways to the goal")
    if check("the cube is at the goal"):
        robot.release("gripper")
```

```
# sweep: grab the cube and move sideways it to the target location
def sweep(robot):
    if check("the robot's gripper is not vertically aligned with the cube and the robot's gripper is not below the cube"):
        robot.put("the gripper above the cube")
    if check("the robot's gripper is above the cube"):
        robot.put("the gripper around the cube")
    if check("the robot's gripper is around the cube and the cube is on the table"):
        robot.lift("cube off the table")
    if check("the robot's grip