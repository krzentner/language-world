
    if check("the robot's gripper is not near the block"):
        robot.reach("block")
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is above the block and the robot's gripper is not around the block"):
        robot.drop("gripper around block")
    if check("the robot's gripper is around the block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is around the block and the block is not near target shelf"):
        robot.move("block to target shelf")
    if check("the robot's gripper is around the block and the block is near target shelf"):
        robot.place("block on shelf")