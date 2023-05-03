if check("the robot's gripper is not near the handle and the robot's gripper is not vertically aligned with the handle"):
        robot.move("gripper near handle")
    if check("the robot's gripper is not around the handle and the robot's gripper is open"):
        robot.pickup("handle")
    if check("the robot's gripper is around the handle and the handle is not lifted up"):
        robot.lift("handle up")
    if check("the handle is lifted up"):
        robot.pull("handle from the side")