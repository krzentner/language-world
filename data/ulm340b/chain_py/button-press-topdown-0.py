
    # Steps:
    #  1. Put gripper above button
    #  2. Start pushing the button down
    #  3. Push the button down harder
    # The button is small and on a surface that we can push it into, so push it
    # from above.
    # If the robot's gripper isn't already above the button, move it there.
    if check("the robot's gripper is not above button"):
        robot.put("gripper above button")
    # If the gripper is above the button, try pushing it down.
    if check("the robot's gripper is above button"):
        robot.push("button down")
    # If the gripper is in front of the button, push it down more
    if check("the robot's gripper is in front of button"):
        robot.push("button down harder")

# block-pick-place: pick up the block and hold it at the target location
def block_pick_place(robot):
    # Steps:
    #  1. Put gripper above block
    #  2. Drop gripper around block
    #  3. Close gripper around block
    #  4. Move block to goal
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around block and the robot's gripper is open"):
        robot.drop("gripper around block")
    # If the gripper is near the block and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near block and the robot's gripper is open"):
        robot.close("gripper around block")
    # We closed the gripper, and the block is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the block to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's grip