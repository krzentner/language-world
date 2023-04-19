

Then, write the program:

```
# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the wall")
    if check("the wall is in the way of the puck and the robot's gripper is not above the wall"):
        robot.place("the gripper above the wall")
    if check("the robot's gripper is above the wall and the robot's gripper is open"):
        robot.drop("gripper around wall")
    if check("the robot's gripper is around the wall and the robot's gripper is closed"):
        robot.push("puck to the goal")
```