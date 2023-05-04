
    if check("the robot's gripper is not above cube"):
        robot.move("gripper to above cube")
    if check("the robot's gripper is vertically aligned with cube"):
        robot.close("gripper around cube")
    if check("the robot's gripper is near cube"):
        robot.move("cube to goal")

# pick-place-side: grab the mug by the handle and hold it at the target location
def pick_place_side(robot):
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("the gripper above the mug")
    if check("the robot's gripper is vertically aligned with the mug and the robot's gripper is not forward aligned with the mug's handle"):
        robot.grab("the mug's handle")
    if check("the robot's gripper is forward aligned with the mug's handle"):
        robot.put("the mug at goal")

# pick-place-above: grab the mug from above and hold it at the target location
def pick_place_above(robot):
    if check("the robot's gripper is not above the mug"):
        robot.move("gripper to above mug")
    if check("the robot's gripper is above the mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    if check("the robot's gripper is near mug"):
        robot.move("mug to goal")

# plate-slide: slide the plate to the target location
def plate_slide(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is above the plate and the robot's gripper is not near the plate"):
        robot.push("gripper into plate")
    if check("the robot's gripper is near plate"):
        robot.slide("plate to goal")

# plate-grasp-turn-reach: grab the plate with both hands and reach to the target location
def plate_grasp_turn_reach(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("the gripper above the plate")
    if check("the robot's gripper is above the plate"):
        robot.grab("the plate")
    if check("