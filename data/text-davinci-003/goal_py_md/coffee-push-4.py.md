

Then fill in the instructions to accomplish the task:

# coffee-push: grab the mug and move it to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above mug handle
    #  2. Drop gripper around mug handle
    #  3. Move mug to target location
    # First, put the gripper above the mug handle. The mug handle is the small
    # shelf-like handle situated on the side of the mug.
    if check("the robot's gripper is not vertically aligned with mug handle"):
        robot.move_gripper("vertically aligned with the mug handle")
    # If the mug handle is below the gripper, move the gripper to the mug
    # handle.
    if check("the robot's gripper is above mug handle and the robot's gripper is not near mug handle"):
        robot.move_gripper("near the mug handle")
    # If the robot's gripper is near the mug handle, we should be able to grab
    # it by closing the gripper.
    if check("the robot's gripper is near mug handle and the robot's gripper is open"):
        robot.move_gripper("above the mug handle", close_gripper=True)
    # Once the gripper is closed around the mug handle, move the mug to the
    # target location.
    if check("the robot's gripper is closed around mug handle"):
        robot.move_gripper("above the target location")