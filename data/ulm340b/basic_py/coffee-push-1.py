
    if check("the robot's gripper is not above coffee mug"):
        robot.place("gripper above coffee mug")
    if check("the robot's gripper is above coffee mug and the robot's gripper is not closed around coffee mug"):
        robot.grab("coffee mug")
    if check("the robot's gripper is closed around coffee mug and the robot's gripper is not near coffee mug"):
        robot.push("coffee mug to goal")
    if check("the robot's gripper is near coffee mug and the robot's gripper is closed around coffee mug"):
        robot.release("coffee mug")

# schunk-push: push the puck to the target location
def schunk_push(robot):
    if check("the robot's gripper is not above puck"):
        robot.put("gripper above puck")
    if check("the robot's gripper is above puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# drawer-push: push the drawer closed
def drawer_push(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

#drawer-pull: pull the drawer open
def drawer_pull(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# door-pull: pull the door open
def door_pull(robot):
