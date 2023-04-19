
    if check("the robot's gripper is not anywhere near the block"):
        robot.navigate("towards the block")
    if check("the robot's gripper is near the block and the robot's gripper is open"):
        robot.grab("block")  
    if check("the robot's gripper is holding the block"):
        robot.move("robot near target position")
    if check("the target position is near the block and the robot is near it"):
        robot.drop("block on target position")