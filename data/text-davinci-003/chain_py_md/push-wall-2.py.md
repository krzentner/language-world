

Steps:
1. Place the gripper right of the wall
2. Lower the gripper over the top of the puck
3. Push the puck with the wall

```
# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Place the gripper right of the wall
    #  2. Lower the gripper over the top of the puck
    #  3. Push the puck with the wall
    # We need to put the robot's gripper near the wall before beginning the
    # task.
    if check("the robot's gripper is not to the right of the wall"):
        robot.place("gripper to the right of the wall")
    # Once the robot's gripper is near the wall, lower it to the top of the
    # puck.
    # We don't have to be careful about the angle, since the wall limits the
    # movement available.
    if check("the robot's gripper is to the right of the wall and the robot's gripper is not near puck"):
        robot.drop("gripper over puck")
    # Now that the gripper is above the puck and the wall is between the gripper
    # and the puck we can start pushing with the wall.
    if check("the robot's gripper is near puck and the wall is between the gripper and the puck"):
        robot.push("puck with wall")