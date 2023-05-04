
    if check("the robot's gripper is not vertically aligned with the peg and the robot's gripper is not above the peg"):
        robot.put("gripper above peg")
    if check("the robot's gripper is above the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    if check("the robot's gripper is around the peg and the robot's gripper is vertically aligned with the peg"):
        robot.pull("peg out of hole")
    if check("the robot's gripper is above the peg and the robot's gripper is closed"):
        robot.drop("gripper above puck")

# hang-object: hang the object on the hook
def hang_object(robot):
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.put("the gripper near the hook")
    if check("the robot's gripper is near the hook and the robot's gripper is closed"):
        robot.drop("object on hook")

# hang-object-side: pick up the object and hang it on the hook
def hang_object_side(robot):
    if check("the robot's gripper is not above the object"):
        robot.place("gripper above object")
    if check("the robot's gripper is not around object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is above object and the robot's gripper is closed"):
        robot.put("the gripper near the hook")
    if check("the robot's gripper is near the hook and the robot's gripper is closed"):
        robot.drop("object on hook")

# put-object: put the object at the target location
def put_object(robot):
    if check("the robot's gripper is not around object and the robot's gripper is not near puck"):
        robot.put("gripper around object")
    if check("the robot's gripper is around object"):
        robot.put("g