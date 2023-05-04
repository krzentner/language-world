
    # Steps:
    #  1. Put gripper near target location
    #  2. Open gripper
    # If the gripper isn't near the target location, move it there.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("vertically aligned with the target location")
    # The gripper can't be around the target location unless it's near the
    # target location.
    # The target location is a small object, so be precise about lining up with
    # it.
    if check("the robot's gripper is near the target location and the robot's gripper is not vertically aligned with the target location"):
        robot.move_gripper("vertically aligned with the target location")
    # Once the gripper is above the target location, we can put it around the
    # target location.
    if check("the robot's gripper is vertically aligned with the target location"):
        robot.move_gripper("around the target location")
    # Open the gripper.
    if check("the robot's gripper is around the target location and the robot's gripper is closed"):
        robot.move_gripper("at the target location")

# pick-place-side: pick up the puck and hold it at the target location from the side
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper near puck
    #  2. Pick up the puck
    #  3. Hold the puck at the target location
    # First, put the gripper next to the puck, in front of it.
    if check("the robot's gripper is not near the puck and the robot's gripper is not forward aligned with the puck"):
        robot.move_gripper("forward aligned with the puck")
    # Once the gripper is near the puck, pick up the puck.
    if check("the robot's gripper is near the puck"):
        robot.move_gripper("around the puck")
    # If the gripper is around the puck, we can just hold it at the target
    # location.
    # The puck is a small object, so be precise about lining up with it.
    if check("the robot's gripper is near the target location"):
        robot.move_