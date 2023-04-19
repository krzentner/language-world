if check("the robot's gripper is not near the door lock"):
        robot.move("gripper to door lock")
    if check("the robot's gripper is near the door lock and the robot's gripper is not aligned with the dial"):
        robot.align("gripper with the dial")
    if check("the robot's gripper is aligned with the dial and the dial is not in the correct position"):
        robot.rotate("dial to the correct position")