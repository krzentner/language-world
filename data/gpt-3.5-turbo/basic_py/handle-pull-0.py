if check("the robot's gripper is not above the handle"):
        robot.move("gripper above handle")
    if check("the robot's gripper is above the handle and the robot's gripper is not around the handle"):
        robot.grab("the handle")
    if check("the robot's gripper is around the handle and the handle is in the down position"):
        robot.pull("up on the handle")