
    if check("the robot's gripper is not forward aligned with the plate's edge but is below the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not around the plate's edge"):
        robot.grab("the plate's edge")
    if check("the robot's gripper is around the plate's edge and the plate is not forward aligned with the robot's gripper"):
        robot.align("the plate to the robot's gripper")
    if check("the robot's gripper is forward aligned with the plate's edge"):
        robot.slide("the plate to the goal")