
    if check("the robot's gripper is not near hammer head and the robot's gripper is not above the nail"):
        robot.put("the gripper above the hammer head and the nail")
    if check("the robot's gripper is near hammer head and the robot's gripper is not around the hammer handle"):
        robot.grab("handle of hammer")
    if check("the robot's gripper is around the hammer handle and the hammer is not above the nail"):
        robot.align("hammer head over nail")
    if check("the hammer is above the nail"):
        robot.punch("hammer down on nail")