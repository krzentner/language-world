# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.move("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        robot.lift("the block up")
    if check("the robot's gripper is not near the shelf"):
        robot.move("gripper to the shelf")
    if check("the robot's gripper is almost aligned vertically with the shelf"):
        robot.move("gripper above the shelf")
    if check("the robot's gripper is not above the target location on the shelf"):
        robot.move("gripper above the target location")
    if check("the robot's gripper is not vertically aligned with the target location"):
        robot.move("gripper to the target location")
    if check("the robot's gripper is vertically aligned with the target location and the robot's gripper is closed"):
        robot.drop("the block on the shelf")