# pick-place-wall: pick up the puck and hold it at the target location with a short wall in the way
def pick_place_wall(robot):
    # Steps:
    #  1. Move the gripper to the starting position, above and to the left of the puck
    #  2. Move the gripper down and around the puck 
    #  3. Close the gripper around the puck
    #  4. Lift the puck up and move it over the wall
    #  5. Move the puck to the target location
    #  6. Release the puck
    # First, move the gripper above and to the left of the puck. 
    if check("the robot's gripper is not above and to the left of the puck"):
        robot.place("gripper above and to the left of the puck")
    # Move the gripper down around the puck.
    if check("the robot's gripper is above and to the left of the puck and the robot's gripper is not around the puck"):
        robot.drop("gripper around the puck")
    # Close the gripper around the puck.
    if check("the robot's gripper is around the puck and the robot's gripper is open"):
        robot.close("gripper around the puck")
    # Lift the puck up and move it over the wall.
    if check("the robot's gripper is closed around the puck and the puck is still on the other side of the wall"):
        robot.lift("gripper with the puck over the wall")
    # Move the puck to the target location.
    if check("the robot's gripper is holding the puck and not yet at the target location"):
        robot.slide("the puck to the goal")
    # Release the puck.
    if check("the robot's gripper is holding the puck and at the target location"):
        robot.open("gripper to release the puck")