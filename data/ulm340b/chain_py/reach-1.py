
    # Steps:
    #  1. Move the robot's gripper towards the target
    #  2. If the robot is near the goal, go to the next step
    #  3. Keep moving the robot's gripper towards the target
    # Move the gripper towards the target.
    if check("the robot is not near the target"):
        robot.move("gripper towards target")
    # If the robot's gripper is near the target, it succeeded.
    if check("the robot is near the target"):
        # Because this is a primitive, don't print the success message, so that
        # this will be transparent to higher-level logic.
        return robot.success()

# pick-place-side: pick up the peg and insert it into the hole to the side
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    # If the peg is lined up with the hole to the side, insert it.
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# button-press-side: push the button from the side
def button_press_side(robot):
    # Steps:
