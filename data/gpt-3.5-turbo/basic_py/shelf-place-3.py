if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above target location and the robot's gripper is closed"):
        robot.place("block at target location")