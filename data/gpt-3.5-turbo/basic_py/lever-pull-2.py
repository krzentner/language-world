if check("the robot's gripper is not near the lever and the robot's gripper is not vertically aligned with the lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with the lever and the lever is not in the 'up' position"):
        robot.pull("lever up")