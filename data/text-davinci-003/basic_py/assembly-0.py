
    if check("the robot's gripper is not above the peg"):
        robot.place("gripper above peg")
    if check("the robot's gripper is above the peg and the gripper is not around the peg"):
        robot.drop("gripper around peg")
    if check("the robot's gripper is around the peg and the gripper is not tightened"):
        robot.tighten("gripper around peg")

# unscrew: unscrew the bolt
# def unscrew(robot):
    if check("the robot's gripper is not around the bolt head"):
        robot.put("gripper around the bolt head")
    if check("the robot's gripper is around the bolt head"):
        robot.unscrew("the bolt")