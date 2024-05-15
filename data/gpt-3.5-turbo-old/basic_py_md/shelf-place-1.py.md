# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        if check("the robot's gripper is not near target location"):
            robot.move("gripper to goal location")
        if check("the robot's gripper is near target location"):
            robot.place("block at goal")