# sweep-into: grab the cube and move it to the target location
def sweep_into(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Drop gripper around cube
    #  3. Close gripper around cube
    #  4. Lift cube off the surface
    #  5. Move the gripper to the target location
    #  6. Put the cube down on the surface
    
    # First, put the gripper roughly above the cube.
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above cube")
    
    # If the gripper isn't around the cube, put it around the cube.
    if check("the robot's gripper is not around cube and the robot's gripper is open"):
        robot.drop("gripper around cube")
    
    # If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near cube and the robot's gripper is open"):
        robot.close("gripper around cube")
    
    # We closed the gripper, and the cube is still near the gripper, so maybe we grabbed it.
    # Try to lift the cube off the surface.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is around cube and the cube is not lifted off the surface"):
        robot.lift("cube off the surface")
    
    # We have the cube in the gripper and have lifted it off the surface.
    # Move the gripper to the target location.
    if check("the robot's gripper is holding the cube and is not near the target location"):
        robot.move("gripper to the target location")
    
    # We're at the target location with the cube, so put it down on the surface.
    if check("the robot's gripper is holding the cube and is at the target location"):
        robot.put("the cube down on the surface")