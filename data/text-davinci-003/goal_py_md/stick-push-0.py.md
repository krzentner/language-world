

Steps:
  1. Put gripper above the stick
  2. Drop the gripper around the stick
  3. Close the gripper around the stick
  4. Move the stick so that it is pushing the thermos
  5. Push the thermos to the target location
 

# stick-push: grab the stick and use it to push the thermos to the target location
def stick_push(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Drop the gripper around the stick
    #  3. Close the gripper around the stick
    #  4. Move the stick so that it is pushing the thermos
    #  5. Push the thermos to the target location
    # First, put the gripper above the stick so that we can grab it.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the stick isn't around the gripper, put the gripper around the stick.
    if check("the robot's gripper is not around the stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is around the stick and closed, the stick can be moved 
    # to the correct position for pushing the thermos.
    if check("the robot's gripper is around the stick and the robot's gripper is closed"):
        robot.move_gripper("right of the thermos")
    # If the stick is near the thermos, we can push the the thermos to the
    # target location.
    if check("the robot's gripper is left of the thermos and the robot's gripper is near the thermos"):
        robot.move_gripper("above the target location")