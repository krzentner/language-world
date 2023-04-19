if check("the robot's gripper is not vertically aligned with the door lock and the robot's gripper is not above the door lock"):
        robot.move("gripper above door lock")
    if check("the robot's gripper is above the door lock and the robot's gripper is not around the dial"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial and the dial is not at the lock's code position"):
        robot.rotate("dial to code position")
    if check("the dial is at the lock's code position"):
        robot.release("dial")
        robot.push("lock handle downward")