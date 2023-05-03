# coffee-push: grab the mug and move it to the target location
# def coffee_push(robot):
    # Steps:
    #  1. Put the gripper above the handle of the mug
    #  2. Drop the gripper around the handle of the mug
    #  3. Close the gripper around the mug handle
    #  4. Lift the mug off the surface
    #  5. Move the mug to the target location
    #  6. Release the mug onto the target location

    # First, adjust the robot's gripper to be above the handle of the mug
    if check("the robot's gripper is not above the coffee mug handle"):
        robot.place("gripper above coffee mug handle")
    # Once the gripper is above the handle, we can drop the gripper around the handle of the mug.
    if check("the robot's gripper is above the coffee mug handle and the gripper is open"):
        robot.drop("the gripper around the coffee mug handle")
    # Now that the gripper is around the handle of the mug, we can close the gripper to grab the mug.
    if check("the robot's gripper is around the coffee mug handle and the gripper is open"):
        robot.close("the gripper around the coffee mug handle")
    # Once the gripper is closed around the handle of the mug, we can lift the mug off the surface.
    if check("the robot's gripper is around the coffee mug handle and the mug is on the surface"):
        robot.lift("the mug off the surface")
    # Now that the mug is secured, we can move it to the target location.
    if check("the robot's gripper is holding the mug and is not at the target location"):
        robot.move("the mug to the target location")
    # Once the mug has been moved to the target location, we can release the mug onto the target location.
    if check("the robot's gripper is holding the mug and is at the target location"):
        robot.release("the mug onto the target location")