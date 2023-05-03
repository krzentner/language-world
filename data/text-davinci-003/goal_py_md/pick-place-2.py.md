

Steps:
  1. Put gripper above puck 
  2. Grab the puck with the gripper
  3. Lift the puck above the surface
  4. Move the puck to the target location
  5. Place the puck at the target location

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck 
    #  2. Grab the puck with the gripper
    #  3. Lift the puck above the surface
    #  4. Move the puck to the target location
    #  5. Place the puck at the target location
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # Once the gripper is lined up above the puck, we should be able to grab it
    # by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Now that the gripper is around the puck, we can lift it off the surface.
    if check("the robot's gripper is around the puck"):
        robot.move_gripper("above the surface")
    # Now that the puck is lifted off the surface, we can move it to the target
    # location.
    if check("the puck is above the surface"):
        robot.move_gripper("near the target location")
    # When the gripper is at the target location, we can place the puck.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the target location")