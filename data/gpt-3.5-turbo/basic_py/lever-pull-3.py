if check("the robot's gripper is not around the lever and the robot's gripper is open"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around the lever and the lever is not rotated up"):
        robot.pull("lever up")