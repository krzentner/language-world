
    if check("the robot's gripper is not below the plate and the robot's gripper is not near the plate"):
        robot.move("gripper below plate")
    if check("the robot's gripper is below the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate"):
        robot.slide("plate into goal")


# plate-slide: slide the plate away from the target location
def plate_slide(robot):
    if check("the robot's gripper is not below the plate and the robot's gripper is not near the plate"):
        robot.move("gripper below plate")
    if check("the robot's gripper is below the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate"):
        robot.slide("plate away from goal")

# plate-width-push: push the plate sideways into the target location
def plate_width_push(robot):
    if check("the robot's gripper is not below the plate and the robot's gripper is not near the plate"):
        robot.move("gripper below plate")
    if check("the robot's gripper is below the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate"):
        robot.push("plate into goal")

# plate-pick: pick up the plate and hold it above the target location
def plate_pick(robot):
    if check("the robot's gripper is not below the plate and the robot's gripper is not near the plate"):
        robot.move("gripper below plate")
    if check("the robot's gripper is below the plate"):
        robot.put("gripper near plate")
    if check("the robot's gripper is near the plate"):
        robot.grab("plate")
    if check("the robot's gripper is around the plate and the plate is not above the target location"):
        robot.place("plate at goal")

# door-undo-close: pull the door open
def door_undo_close(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with the door handle and