
    if check("the robot's gripper is not above the box lid and the robot's gripper is not vertically aligned with the box lid"):
        robot.put("the robot's gripper above the box lid")
    if check("the robot's gripper is above the box lid"):
        robot.open("the robot's gripper around the box lid")
    if check("the robot's gripper is near the box lid"):
        robot.close("the gripper on the box lid")
    if check("the robot's gripper is closed"):
        robot.place("box lid on top of the box")

# box-open: pick up the box lid and hold it above the box
def box_open(robot):
    if check("the robot's gripper is not above the box lid and the robot's gripper is not vertically aligned with the box lid"):
        robot.put("the robot's gripper above the box lid")
    if check("the robot's gripper is above the box lid"):
        robot.open("the robot's gripper around the box lid")
    if check("the robot's gripper is near the box lid"):
        robot.close("the gripper on the box lid")
    if check("the robot's gripper is closed"):
        robot.raise("box lid above the box")

# pick-hollow-place: pick up the tube and place it at the target location
def pick_hollow_place(robot):
    if check("the robot's gripper is not near tube"):
        robot.open("gripper")
    if check("the robot's gripper is near tube and the robot's gripper is open"):
        robot.lower("gripper around tube")
    if check("the robot's gripper is near tube and the robot's gripper is closed"):
        robot.lift("tube")
    if check("the robot's gripper is vertically aligned with the goal location"):
        robot.place("tube over goal")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# drawer-pick-place: pick up the drawer and hold it at the target location
def drawer_