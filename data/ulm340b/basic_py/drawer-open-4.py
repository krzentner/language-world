
    if check("the robot's gripper is not almost vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with drawer handle and the robot's gripper is open"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle"):
        robot.pull("drawer open")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# hook-and-throw: pull the handle and throw it at the peg
def hook_and_throw(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open and hold it open")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("gripper forward")
    if check("the robot's gripper is in front of the door handle"):
        robot.release("gripper around door handle")

# push-throw: slide the puck over to the target location and release it
def push_throw(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
    if check("the robot's gripper is in front of the puck"):
        robot.release("gripper around puck")

# pick-place-side: grab the puck and place it