
    if check("the robot's gripper is above the puck"):
        robot.push("the puck to the goal")

# pick-place-back: pick up the puck and place it at the target location from behind
def pick_place_back(robot):
    if check("the robot's gripper is above the puck"):
        robot.put("gripper around puck")
    if check("the robot's gripper is vertically aligned with the puck"):
        robot.grab("puck")
    if check("the robot's gripper is closed around the puck"):
        robot.place("puck at goal")

# push-grasp: grasp the handle and push it to the target location
def push_grasp(robot):
    if check("the robot's gripper is above the handle"):
        robot.grab("handle")
    if check("the robot's gripper is closed around the handle"):
        robot.push("handle to goal")

# push-back-grasp: grasp the handle and push it backwards to the target location
def push_back_grasp(robot):
    if check("the robot's gripper is above the handle"):
        robot.grab("handle")
    if check("the robot's gripper is closed around the handle"):
        robot.push("handle to goal")

# drawer-close-side: grasp the drawer handle and push the drawer closed
def drawer_close_side(robot):
    if check("the robot's gripper is above the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is closed around the drawer handle"):
        robot.push("drawer handle closed")

# drawer-open-side: grasp the drawer handle and pull the drawer open
def drawer_open_side(robot):
    if check("the robot's gripper is above the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is closed around the drawer handle"):
        robot.pull("drawer handle open")

# slide-and-grasp: grasp the handle and slide it to the target location
def slide_and_grasp(robot):
    if check("the robot's gripper is above the handle"):
        robot.grab("handle")
    if check("the robot's gripper is closed around the handle"):
        robot.slide("handle to goal")

# slide-and-grasp