
    if check("the robot's gripper is not near door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is forward aligned with door handle"):
        robot.rotate("door handle")

# push-left: slide the puck to the target location on the left
def push_left(robot):
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the left")

# turn-right: turn the lever to the right
def turn_right(robot):
    if check("the robot's gripper is not near the lever and the robot's gripper is not right of the lever"):
        robot.grab("lever")
    if check("the robot's gripper is left of the lever"):
        robot.rotate("lever right")

# lever-pull: pull the lever down
def lever_pull(robot):
    if check("the robot's gripper is not left of the lever"):
        robot.move("gripper to left of lever")
    if check("the robot's gripper is below lever and the robot's gripper is not around lever"):
        robot.put("gripper around lever")
    if check("the robot's gripper is around lever and the robot's gripper is open"):
        robot.close("gripper around lever")
    if check("the robot's gripper is around lever"):
        robot.pull("lever down")

# pull-left: pull the object to the left of the target location
def pull_left(robot):
    if check("the object is left of the robot's gripper and the robot's gripper is not near object"):
        robot.move("gripper to left of object")
    if check("the robot's gripper is near object"):
        robot.grab("object")
    if check("the robot's gripper is vertically aligned with object"):
        robot.pull("object left")

# push-back: push the