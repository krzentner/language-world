
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the peg is forward aligned with the robot's gripper and the robot's gripper is not around peg"):
        robot.place("gripper around peg")
    if check("the peg is forward aligned with the robot's gripper and the robot's gripper is around peg"):
        robot.pull("unplug peg from hole")