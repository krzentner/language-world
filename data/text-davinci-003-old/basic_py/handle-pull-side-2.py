
    if check("the robot's gripper is not near the handle"):
        robot.reach("gripper above handle")
    if check("the robot's gripper is near the handle and the gripper does not face upwards"):
        robot.orient("gripper upwards")
    if check("the robot's gripper is faced upwards and the robot's gripper is not around handle"):
        robot.grasp("handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("handle up")