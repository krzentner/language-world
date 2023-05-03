

Solution:
```
# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    if check("the robot's gripper is not above the mug"):
        robot.place("gripper above mug")
    if check("the robot's gripper is not around the mug and the robot's gripper is open"):
        robot.grasp("mug with gripper")
    if check("the robot's gripper is around mug and the robot's gripper is open"):
        robot.lift("mug with gripper")
    if check("the robot's gripper is around mug and the robot's gripper is closed"):
        robot.move("mug to goal")
```