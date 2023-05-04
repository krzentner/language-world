
"""



# ASSEMBLY SCRIPT

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # If the robot's gripper is not in the same place as the wrench
    if check("the robot's gripper is not in the same place as the wrench"):
        robot.put("the gripper in the same place as the wrench")
        robot.put("the gripper in the same place as the wrench")
        robot.put("the gripper in the same place as the wrench")

    if check("the robot's gripper is in the same place as the wrench"):
        robot.push("the gripper down")
        robot.push("the gripper down")
        robot.push("the gripper down")
        robot.push("the gripper down")
        robot.push("the gripper down")
        robot.push("the gripper down")

    if check("the wrench is in the gripper of the robot and the robot is holding the wrench"):
        robot.push("the wrench into the peg")
        robot.push("the wrench into the peg")
        robot.push("the wrench into the peg")

    if check("the wrench is wrapped around the peg"):
        robot.pull("the gripper upwards")
        robot.pull("the gripper upwards")
        robot.pull("the gripper upwards")
        robot.pull("the gripper upwards")
        robot.pull("the gripper upwards")
        robot.pull("the gripper upwards")
        robot.pull("the gripper upwards")

    if check("the robot is no longer holding the wrench and the wrench is wrapped around the peg"):
        robot.place("the gripper to the right of the wrench")
        robot.place("the gripper to the right of the wrench")
        robot.place("the gripper to the right of the wrench")
        robot.place("the gripper to the right of the wrench")
        robot.place("the gripper to the right of the wrench")

    if check("the wrench is wrapped around the peg and the robot's gripper is right of the wrench"):
        robot.put("the gripper down to grip the wrench")
        robot.put("the gripper down to grip the wrench")
        robot.put("the gripper down to grip the wrench")
        robot.put("the gripper down to grip the wrench")

    if check("the wrench is wrapped around the peg and the robot is gripping the wrench"):
        robot.pull("the