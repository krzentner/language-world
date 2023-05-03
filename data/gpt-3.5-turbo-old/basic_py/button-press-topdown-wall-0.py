if check("the robot's gripper is not vertically aligned with button and the robot's gripper is not above the wall"):
        robot.move("gripper above wall")
    if check("the robot's gripper is above the button and the robot's gripper is not aligned with the button"):
        robot.move("gripper to align with button")
    if check("the robot's gripper is aligned with the button and the gripper is not pushing down"):
        robot.push("down on button with the help of the wall")