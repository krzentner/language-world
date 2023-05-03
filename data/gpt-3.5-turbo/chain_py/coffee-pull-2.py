# Steps:
    #  1. Put gripper around handle of mug
    #  2. Lift the mug off the surface
    #  3. Move the mug to the target location
    #  4. Lower the mug onto the surface at the target location
    # First, put the gripper around the handle of the mug.
    if check("the robot's gripper is not around the mug handle"):
        robot.grab("mug handle")
    # Once the gripper is around the handle, lift the mug up off the surface.
    if check("the robot's gripper is holding the mug and the mug is on the surface"):
        robot.lift("mug off surface")
    # Once the mug is lifted off the surface, move it to the target location.
    if check("the robot's gripper is holding the mug and the mug is not on the surface"):
        robot.move("mug to goal")
    # Once the mug is at the target location, lower it onto the surface.
    if check("the robot's gripper is holding the mug and the mug is at the goal"):
        robot.lower("mug onto surface")