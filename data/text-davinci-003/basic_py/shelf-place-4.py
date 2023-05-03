
    if check("the robot's gripper is not near the shelf and the shelf is not forward aligned with the robot's gripper"):
        robot.move("gripper to front of shelf")
    if check("the robot's gripper is forward aligned with the shelf and the gripper is not above the shelf block"):
        robot.put("gripper above shelf block")
    if check("the robot's gripper is above shelf block and the robot's gripper is open"):
        robot.drop("gripper around shelf block")
    if check("the robot's gripper is above shelf block and the robot's gripper is closed"):
        robot.place("shelf block at goal")