# shelf-place: pick up the block and place it at the target location
# def shelf_place(robot):
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    if check("the robot's gripper is above block and the robot's gripper is closed"):
        if check("the robot's gripper is not near shelf"):
            robot.move("gripper near shelf")
        if check("the block is not aligned with the shelf"):
            robot.align("block to shelf")
        if check("the block is aligned with the shelf"):
            robot.release("block on shelf")