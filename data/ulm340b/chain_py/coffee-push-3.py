
    # Steps:
    #  1. Put gripper above the mug
    #  2. Put gripper around the mug
    #  3. Push the mug to the target location
    # Start by putting the gripper above the mug, to make it easier to grab the
    # mug without bumping it.
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    # Once the gripper is above the mug, put the gripper around the mug.
    if check("the robot's gripper is above mug and the robot's gripper is not around mug"):
        robot.put("gripper around mug")
    # Once the mug is mostly above the gripper, push the mug to the target
    # location.
    if check("the robot's gripper is above mug"):
        robot.push("mug to the goal")

# coffee-pick-place: pick up the mug and move it to the target location
def coffee_pick_place(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Put gripper around the mug
    #  3. Close gripper around the mug
    #  4. Push the mug to the target location
    # Start by putting the gripper above the mug, to make it easier to grab the
    # mug without bumping it.
    if check("the robot's gripper is not above mug"):
        robot.put("gripper above mug")
    # Once the gripper is above the mug, put the gripper around the mug.
    if check("the robot's gripper is above mug and the robot's gripper is not around mug"):
        robot.put("gripper around mug")
    # Once the mug is mostly above the gripper, push the mug to the target
    # location.
    if check("the robot's gripper is above mug and the robot's gripper is open"):
        robot.close("gripper around mug")
    # Once the gripper is around the mug, push the mug to the target location.
    if check("the robot's gripper is above mug"):
        robot.push("mug to the goal")

# coffee-wall-push: grab the mug and move it to the target location around an obstacle
def coffee_wall