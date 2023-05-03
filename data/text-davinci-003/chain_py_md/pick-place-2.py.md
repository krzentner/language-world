

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to the target location
    #  4. Release the puck at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above puck")
    # If the puck becomes left of the gripper, go back to putting the gripper
    # above the puck.
    # Because the puck is a small object, check if the gripper is around it
    # instead of in front of it.
    if check("puck is not left of the robot's gripper and puck is not around the robot's gripper"):
        robot.grab("puck")
    # Once the puck is sufficiently under the gripper, move the puck to the
    # target location.
    if check("the robot's gripper is around the puck"):
        robot.move("puck to the target location")
    # Once the puck is in the target location and is tight around the gripper,
    # release the puck.
    if check("the puck is in the target location and the robot's gripper is around the puck"):
        robot.release("puck")