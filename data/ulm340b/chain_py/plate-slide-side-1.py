
    # Steps:
    #  1. Move gripper to left edge of the plate
    #  2. Slide the plate to the goal
    # If the robot's gripper is not near the left edge of the plate, move it
    # there.
    if check("the robot's gripper is not left of the plate"):
        robot.put("the gripper left of the plate")
    # If the plate is below the robot's gripper, we've grabbed it.
    # Slide the plate to the target location.
    if check("the plate is below the robot's gripper"):
        robot.slide("plate to goal")

# peg-insert-topdown: insert the peg into the hole from above
def peg_insert_topdown(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Insert the peg down into the hole
    # First, put the gripper above the peg.
    # This will keep us from bumping the peg while reaching down to grab it.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg is right of the robot's gripper, move the robot's gripper
    # above the peg again.
    if check("the peg is right of the robot's gripper"):
        robot.put("gripper above peg")
    # As long as the robot's gripper is vertically aligned with the peg, put it
    # around the peg.
    if check("the robot's gripper is vertically aligned with the peg and the robot's gripper is not around peg"):
        robot.grab("the peg with the gripper")
    # If the gripper is around the peg and the peg is not vertically aligned
    # with the hole, line the peg up with the hole.
    if check("the peg is not vertically aligned with the hole and the robot's gripper is around peg"):
        robot.align("the peg to the hole")
    # As long as the peg is above the hole, we can insert it.
    # Check this as long as the robot's gripper is around the peg to be