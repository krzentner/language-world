if check("the robot's gripper is not near the lever"):
        robot.move("gripper to left of lever")
    if check("the robot's gripper is vertically aligned with the lever and the robot's gripper is not around the lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever and the lever is in the down position"):
        robot.pull("up on lever")