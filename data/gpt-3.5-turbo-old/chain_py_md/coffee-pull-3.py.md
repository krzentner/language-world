# coffee-pull: grab the mug and pull it to the target location
# def coffee_pull(robot):
    # Steps:
    #  1. Put gripper around handle
    #  2. Lift mug up
    #  3. Slide mug to goal
    # Put the gripper around the handle of the mug, making sure it has a good grip.
    if check("the robot's gripper is not around the mug handle"):
        robot.drop("gripper around mug handle")
    # Lift the mug up off of the surface.
    if check("the robot's gripper is around mug handle and the mug is on the surface"):
        robot.lift("mug off surface")
    # Slide the mug to the goal location.
    if check("the robot's gripper is holding the mug and the mug is above the goal"):
        robot.slide("mug to goal location")