
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.lower("gripper onto the puck")
    if check("the puck is not vertically aligned with reach target"):
        robot.hold("the puck over the target")
    if check("the puck is vertically aligned with reach target and the robot's gripper is not near reach target"):
        robot.reach("the puck to the goal")


# pick-place-wall: pick up the puck and hold it at the target location against a wall
def pick_place_wall(robot):
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near the puck"):
        robot.lower("gripper onto the puck")
    if check("the puck is not vertically aligned with reach target"):
        robot.hold("the puck over the target")
    if check("the puck is vertically aligned with reach target and the robot's gripper is not near reach target"):
        robot.reach("the puck to the goal")


# drawer-close-side: push the drawer closed from the side
def drawer_close_side(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# drawer-open-side: pull the drawer open from the side
def drawer_open_side(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.pull("drawer open")

# door-close-side: push the door closed from the side
def door_close_side(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# door-open-