Here's a program to perform the `push-wall` task:

```
# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        if check("there is a small wall in front of the puck"):
            robot.push("the wall out of the way")
            robot.slide("the puck to the goal")
        else:
            robot.slide("the puck to the goal")
``` 

This program begins by checking if the robot's gripper is in the correct position to pick up the puck. If not, it moves the gripper into position. Then it checks if the gripper is near the puck and the puck is below the gripper. If so, it checks if there is a small wall in front of the puck. If there is, it moves the wall out of the way before sliding the puck to the goal. Otherwise, it just slides the puck to the goal.