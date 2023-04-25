

Steps:
  1. Put the gripper above the stick
  2. Grab the stick with the gripper
  3. Line up the stick with the thermos
  4. Pull the thermos towards the target location using the stick

# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put the gripper above the stick
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the stick isn't left of the gripper, we need to move the gripper back
    # above the stick to grab it.
    if check("the stick is not left of the robot's gripper and the stick is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the stick", close_gripper=True)
    # Once the gripper is lined up with the stick, we can grab it by closing the
    # gripper.
    if check("the robot's gripper is left of the stick and the robot's gripper is closed"):
        robot.move_gripper("near the stick")
    # Now that we have the stick, line it up with the thermos.
    if check("the robot's gripper is near the stick and the stick is not horizontally aligned with the thermos"):
        robot.move_gripper("horizontally aligned with the thermos")
    # Finally, pull the thermos towards the target location using the stick.
    if check("the robot's gripper is horizontally aligned with the thermos"):
        robot.move_gripper("near the target location")