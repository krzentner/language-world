# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.place("block at goal location on the shelf")