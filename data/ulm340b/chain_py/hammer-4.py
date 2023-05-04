
    # Steps:
    #  1. Line up the robot's gripper as viewed from above
    #  2. Push down on the nail from the top
    #  3. Move the hammer down the length of the nail
    #  4. Pull the hammer back to hit the nail
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with the nail"):
        robot.put("gripper above nail")
    # Now that the gripper is lined up, just push down on the nail from the top.
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.push("down on nail")
    # If the gripper is still vertically aligned with the nail, we're probably
    # hitting it.
    # If it's vertically aligned and forward aligned, we've moved past the nail
    # and we're pulling the hammer back to hit the nail.
    # As long as that's the case, move the hammer back to hit the nail.
    if check("the robot's gripper is vertically aligned with the nail"):
        robot.put("hammer back")

# peg-insert-topdown: push the peg down into the hole
def peg_insert_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the peg from the top
    #  3. Slide the peg down into the hole
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with peg"):
        robot.put("gripper above peg")
    # Now that the gripper is lined up, just push down on the peg from the top.
    if check("the robot's gripper is vertically aligned with peg"):
        robot.push("down on peg")
    # As long as the gripper is still vertically aligned with the peg, it's
    # probably still pushing down on the peg, so keep pushing down.
    # Once it's below the peg, it's probably in