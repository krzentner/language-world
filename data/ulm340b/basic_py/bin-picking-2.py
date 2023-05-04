
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    if check("the robot's gripper is forward aligned with the cube and the robot's gripper is open"):
        robot.close("gripper")
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.lift("cube")
    if check("the robot's gripper is not above the target bin"):
        robot.place("gripper above target bin")
    if check("the robot's gripper is not near the target bin"):
        robot.place("gripper into target bin")
    if check("the robot's gripper is near the target bin and the robot's gripper is closed"):
        robot.open("gripper")

# bin-picking-pour-into-bin: pick up the cube and pour it into the target bin
def bin_picking_pour_into_bin(robot):
    if check("the robot's gripper is not vertically aligned with the cube"):
        robot.put("gripper above cube")
    if check("the robot's gripper is vertically aligned with the cube and the robot's gripper is open"):
        robot.put("gripper around cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper")
    if check("the robot's gripper is near the cube and the robot's gripper is closed"):
        robot.lift("cube")
    if check("the robot's gripper is not vertically aligned with the target bin"):
        robot.put("gripper above target bin")
    if check("the robot's gripper is vertically aligned with the target bin and the robot's gripper is closed"):
        robot.pour("cube into target bin")

# assembly: pick up the nut and place it onto the screw
def assembly(robot):
    if check("the robot's gripper is not vertically aligned with nut"):
        robot.place("gripper above nut")
    if check("the robot's gripper is vertically aligned with nut and the robot's gripper is open"):
        robot