# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck with gripper
    #  3. Move gripper to target location
    #  4. Release puck
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck")
    # Move the gripper to the target location.
    if check("the robot's gripper is holding the puck and is not at the target location"):
        robot.move("gripper to target location")
    # Release the puck at the target location.
    if check("the robot's gripper is at the target location and holding the puck"):
        robot.release("puck at target location")