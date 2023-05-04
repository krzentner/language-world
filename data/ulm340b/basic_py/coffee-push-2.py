
    if check("the robot's gripper is not almost vertically aligned with the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is almost vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around the mug and the mug is not in the goal"):
        robot.slide("the mug to the goal")

#coffee-push-retreat: grab the mug and retreat to the start
def coffee_push_retreat(robot):
    if check("the robot's gripper is not almost vertically aligned with the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is almost vertically aligned with the mug and the robot's gripper is not around the mug"):
        robot.put("gripper around mug")
    if check("the robot's gripper is around the mug and the mug is not in the starting position"):
        robot.slide("the mug to the starting position")

# door-close: push the door closed
def door_close(robot):
    if check("the robot's gripper is not almost vertically aligned with the door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is not around the door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle and the door is not closed"):
        robot.push("door closed")

#drawer-pull-out: grab the drawer and pull it out
def drawer_pull_out(robot):
    if check("the robot's gripper is not almost vertically aligned with the drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is not around the drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around the drawer handle and the drawer is not pulled out"):
        robot.pull("drawer out")

# door-pull: pull the door open
def door_pull(robot):
    if check("the robot's gripper is not almost vertically aligned with the door handle"):
        robot.