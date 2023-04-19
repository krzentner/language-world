

If check("the robot's gripper is not above the button"):
    robot.move("gripper above button")
If check("the robot's gripper is not close to the button and the wall is between the robot's gripper and the button"):
    robot.place("gripper on top of wall")
If check("the robot's gripper is close to the button and the wall is between the robot's gripper and the button"):
    robot.push("gripper through wall to button")
If check("the robot's gripper is close to the button"):
    robot.push("button")