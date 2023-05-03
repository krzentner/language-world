
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("toward drawer")

# pull-out: pull the object out of the slot
def pull_out(robot):
    if check("the robot's gripper is not vertically aligned with the object"):
        robot.put("gripper above object")
    if check("the robot's gripper is vertically aligned with the object and the robot's gripper is not around object"):
        robot.put("gripper around object")
    if check("the robot's gripper is around object"):
        robot.pull("out of slot")