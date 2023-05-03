
    if check("the robot's gripper is not in front of the button and the wall"):
        robot.move("gripper to front of button and wall")    
    if check("the robot's gripper is not horizontally aligned with button and the wall"):
        robot.place("gripper at wall")     
    if check("the robot's gripper is horizontally aligned with button and the wall"):
        robot.push("the button")