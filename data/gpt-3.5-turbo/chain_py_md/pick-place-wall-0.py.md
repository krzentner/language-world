# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
# def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper to goal location
    #  2. Check if the wall is in the way
    #  3. Move to the other side of the wall if necessary
    #  4. Put gripper above puck
    #  5. Drop gripper around puck
    #  6. Close gripper around puck
    #  7. Move puck to goal location
    # Move the gripper to the goal location, accounting for the wall in the way.
    if check("the robot's gripper is not near the goal location"):
        if check("there is a wall between the robot's current location and the goal location"):
            robot.go_around("the wall")
        robot.reach("the goal location")
    # Check if the wall is in the way, and move to the other side if necessary.
    if check("there is a wall between the robot's current location and the puck"):
        robot.go_around("the wall")
    # Put the gripper above the puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("the gripper above the puck")
    # Drop the gripper around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("the gripper around the puck")
    # Close the gripper around the puck.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.close("the gripper around the puck")
    # Move the puck to the goal location.
    if check("the robot's gripper is above the puck and the robot's gripper is closed"):
        robot.place("the puck at the goal location")