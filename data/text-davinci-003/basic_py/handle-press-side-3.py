
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not horizontally aligned with handle"):
        robot.align("gripper with handle")
    if check("the robot's gripper is not near handle"):
        robot.put("gripper around handle")
    if check("the robot's gripper is horizontally aligned with handle"):
        robot.push("down on handle")

# pick-up-lid: pick up the lid 
def pick_up_lid(robot):
    if check("the robot's gripper is not above the lid"):
        robot.put("gripper above lid")
    if check("the robot's gripper is not around lid and the robot's gripper is open"):
        robot.drop("gripper around lid")
    if check("the robot's gripper is around the lid and the robot's gripper is open"):
        robot.close("gripper around lid")
    if check("the robot's gripper is not near the lid and the robot's gripper is closed"):
        robot.lift("gripper with lid")