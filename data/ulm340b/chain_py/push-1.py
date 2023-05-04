
    # Steps:
    #  1. Move the gripper towards the puck
    #  2. Move the gripper right into the puck
    #  3. Push the puck into the target
    # As long as the gripper isn't touching the puck, we can move the gripper
    # closer to it.
    if check("the robot's gripper is not near puck"):
        robot.approach("gripper toward puck")
    # Once the gripper touches the puck, push it towards the target
    if check("the robot's gripper is near puck"):
        robot.push("puck into target")

# slide: slide the puck into the target location
def slide(robot):
    # Steps:
    #  1. Move the gripper towards the puck
    #  2. Move the gripper right into the puck
    #  3. Slide the puck into the target
    # As long as the gripper isn't touching the puck, we can move the gripper
    # closer to it.
    if check("the robot's gripper is not near puck"):
        robot.approach("gripper toward puck")
    # Once the gripper touches the puck, slide it towards the target
    if check("the robot's gripper is near puck"):
        robot.slide("puck into target")

# pick-place-side: pick up the puck and hold it at the target location by
# moving it in from the side
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not vertically aligned with puck and the robot's gripper is above puck"):
        robot.move("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and