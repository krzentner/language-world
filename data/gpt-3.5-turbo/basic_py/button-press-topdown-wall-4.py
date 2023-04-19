if check("the robot's gripper is not above the button"):
        robot.move("gripper to the side of the button")
    if check("the robot's gripper is aligned with the button"):
        robot.move("gripper close to the button")
    if check("the wall is blocking the robot's gripper from pushing the button"):
        robot.move("gripper above the wall")
    if check("the robot's gripper is above the wall and aligned with the button"):
        robot.push("down on button")