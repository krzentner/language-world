

Solution:
```
# sweep: grab the cube and move it sideways to the target location
def sweep(robot):
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.grasp("cube")
    if check("the robot's gripper is around cube and the cube is not horizontally aligned with the target location"):
        robot.align("cube with target")
    if check("cube is horizontally aligned with target"):
        robot.push("cube sideways to target")
```