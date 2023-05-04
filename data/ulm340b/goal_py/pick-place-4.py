
    # Steps:
    #  1. Put gripper above puck
    #  2. Lower gripper around puck
    #  3. Lift puck and hold it above the target location
    # The puck is small, so the gripper should be above the puck to pick it up.
    # It would also work to grab the puck from the side, but this is probably
    # easier.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # As long as the robot's gripper is above the puck, we can lower the gripper
    # around the puck to pick it up.
    # Since the puck is small, we need to close the gripper to get it to
    # actually pick up the puck.
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Now that we've picked up the puck, we need to move the gripper above the
    # target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is around the puck and the puck is in the robot's gripper"):
        robot.move_gripper("above the target location")

# pick-place-side: pick up the puck and hold it at the target location from the side
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper in front of puck
    #  2. Move gripper around puck
    #  3. Lift puck and hold it above the target location
    # The puck is small, so the gripper should be in front of the puck to pick
    # it up.
    # It would also work to grab the puck from the top, but this is probably
    # easier.
    if check("the robot's gripper is not in front of the puck and the robot's gripper is not forward aligned with the puck"):
        robot.move_gripper("forward aligned with the puck")
    # As long as the robot's gripper is in front of the puck, we can move the
    # gripper around the puck to pick it up.
  