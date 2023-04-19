
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is around the block and the robot's gripper is closed"):
        robot.lift("block up")
    if check("the robot's gripper is not near target shelf"):
        robot.move("gripper to goal")
    if check("the robot's gripper is near the shelf"):
        robot.place("block on shelf")