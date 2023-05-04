
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.push("into drawer")

# door-close: push the door close
def door_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.push("door closed")

# drawer-pick-place: pick up the puck and place it in the drawer
def drawer_pick_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is not near puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is open and puck is near"):
        robot.close("around puck")
    if check("the robot's gripper is above puck"):
        robot.move("puck to drawer")
    if check("the robot's gripper is above drawer and the puck is above the drawer"):
        robot.move("puck to drawer")
    if check("the robot's gripper is above drawer"):
        robot.drop("puck into drawer")

# pick-orient-place: pick up the object from its initial position and orientation, and place it at the target position with the target orientation
def pick_orient_place(robot):
    if check("the robot's gripper is not above object"):
        robot.put("gripper above object")
    if check("the robot's gripper is not near object and the robot's gripper is open"):
        robot.drop("gripper around object")
    if check("the robot's gripper is open and object is near"):
        robot.close("around object")
   