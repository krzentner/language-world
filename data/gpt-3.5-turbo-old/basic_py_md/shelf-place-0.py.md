# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    if check("the robot's gripper is not above block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.lift("the block")
    if check("the robot's gripper is not near the target location"):
        robot.move("to the target location")
    if check("the robot's gripper is near the target location and the block is not on top of the target location"):
        robot.place("the block on top of the target location")