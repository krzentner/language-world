# stick-pull: use the stick to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put the end of the stick near the thermos handle
    #  2. Pinch the thermos handle with the stick
    #  3. Move the stick towards the target location
    #  4. Release the thermos handle
    # First, put the end of the stick near the thermos handle.
    if check("the end of the stick is not near the thermos handle"):
        robot.move_stick("near the thermos handle")
    # If the end of the stick is near the thermos handle but not pinching it,
    # pinch the thermos handle.
    if check("the end of the stick is near the thermos handle and the thermos handle is not pinched by the stick"):
        robot.move_stick("around the thermos handle")
    # Once the thermos handle is pinched, move the stick towards the target
    # location by moving the robot's arm.
    if check("the thermos handle is pinched by the stick and the stick is not near the target location"):
        robot.move_arm("near the target location")
    # Once the stick is near the target location, release the thermos handle.
    if check("the stick is near the target location"):
        robot.release_stick()