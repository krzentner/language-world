if check("the robot's gripper is not near the button and the robot's gripper is not vertically aligned with the button"):
        robot.move("gripper to right of button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not around the button"):
        robot.put("gripper around button")
    if check("the robot's gripper is around the button"):
        robot.push("button towards wall")
    if check("the robot's gripper is around the button and the robot's gripper is touching the wall"):
        robot.pull("button towards robot")