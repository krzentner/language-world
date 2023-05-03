# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Move above puck
    #  2. Check if wall is present
    #  3. Move gripper around the wall if present and lift the puck
    #  4. Move gripper above target
    #  5. Drop the puck
    
    # Move the robot above the puck before we do anything else.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
        
    # If there is a wall present, move the gripper around the wall to pick up the puck.
    if check("there is a wall in the way"):
        robot.put("gripper around the wall")
        robot.lift("puck")
    
    # If the wall isn't in the way or we've moved around it, move the gripper above the target.
    if check("the robot's gripper is not above the target"):
        robot.place("gripper above target")
    
    # Finally, drop the puck at the target location.
    if check("the robot's gripper is holding the puck"):
        robot.drop("puck at target location")