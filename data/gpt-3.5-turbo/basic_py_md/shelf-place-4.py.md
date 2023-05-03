# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.put("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        if check("the block is not above the target location"):
            robot.put("gripper above target location")
        if check("the robot's gripper is vertically aligned with the target location"):
            robot.place("block at target location")