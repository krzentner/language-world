# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Grab the puck with the gripper
    #  3. Move gripper to target location
    #  4. Release the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to pick it up.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck")
    # Once the gripper has grabbed the puck, move it to the target location.
    if check("the robot's gripper is holding the puck and is not at the target location"):
        robot.move("gripper to goal")
    # Now that we're at the target location, drop the puck.
    if check("the robot's gripper is at the goal location holding the puck"):
        robot.release("puck")