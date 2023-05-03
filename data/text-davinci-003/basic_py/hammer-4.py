
    if check("the robot's gripper is not near the hammer and the hammer is left of the robot's gripper"):
        robot.move("gripper to right of hammer")
    if check("the robot's gripper is near the hammer and the robot's gripper is not around the hammer"):
        robot.grab("hammer")
    if check("the robot's gripper is vertically aligned with the nail and the robot's gripper is not around the hammer and the hammer is forward of the robot's gripper"):
        robot.align("hammer to nail")
    if check("the hammer is above the nail"):
        robot.hit("nail with hammer")