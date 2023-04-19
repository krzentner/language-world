
    if check("the robot's gripper is not near block"):
        robot.put("gripper near block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is around block and the block is not near target"):
        robot.move("block to the target")
    if check("the block is near the target"):
        robot.place("block on target")