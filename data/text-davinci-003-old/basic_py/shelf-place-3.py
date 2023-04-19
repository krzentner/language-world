
    if check("the robot's gripper is not above the block"):
        robot.move("gripper above block")
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near the block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above the block and the robot's gripper is closed"):
        robot.place("block at goal")