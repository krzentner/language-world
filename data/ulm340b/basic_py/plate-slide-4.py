
    if check("the robot's gripper is not around the plate and the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is above the plate"):
        robot.slide("the gripper to the plate")
    if check("the robot's gripper is near the plate and the robot's gripper is not closed"):
        robot.close("the gripper on the plate")
    if check("the robot's gripper is around the plate and the plate is not in the goal"):
        robot.slide("the plate to the goal")

# handle-press: push the plate into the target location
def handle_press(robot):
    if check("the robot's gripper is not near the handle"):
        robot.grab("handle")
    if check("the robot's gripper is near the handle and the robot's gripper is not closed"):
        robot.close("gripper on the handle")
    if check("the robot's gripper is near the handle and the handle is not pressed"):
        robot.push("the handle")

# lever-pull: push the plate into the target location
def lever_pull(robot):
    if check("the robot's gripper is not near the lever"):
        robot.grab("lever")
    if check("the robot's gripper is near the lever and the robot's gripper is not closed"):
        robot.close("gripper on the lever")
    if check("the robot's gripper is closed and the lever is not pulled"):
        robot.pull("the lever down")

# door-pull-side: pull the door open
def door_pull_side(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle"):
        robot.pull("door open")

# door-pull-towards: pull the door open
def door_pull_towards(robot):
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle"):
        robot.pull("door open")


# button-press-bottomup: press the button down
