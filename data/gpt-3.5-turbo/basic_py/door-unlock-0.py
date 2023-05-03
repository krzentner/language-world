if check("the robot's gripper is not near the door handle"):
        robot.move("gripper to door handle")
    if check("the robot's gripper is not around the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around the door handle and the dial is not in the correct position"):
        robot.turn("dial to correct position")