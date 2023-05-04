
    # Steps:
    #  1. Move gripper above puck
    #  2. Put gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, move the gripper above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not near puck"):
        robot.move("gripper above puck")
    # Next, move the gripper around the puck.
    if check("the robot's gripper is above puck and the robot's gripper is not near puck"):
        robot.put("gripper around puck")
    # Now, close the gripper around the puck.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # Finally, move the puck to the goal.
    if check("the robot's gripper is closed and the robot's gripper is above puck"):
        robot.move("puck to goal")

# pick-place-wall-high: pick up the puck and hold it at the target location with a tall wall in the way
def pick_place_wall_high(robot):
    # Steps:
    #  1. Move gripper above puck
    #  2. Put gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck up
    #  5. Move puck over wall
    #  6. Move puck down
    #  7. Move puck to goal
    # First, move the gripper above the puck.
    if check("the robot's gripper is not above puck"):
        robot.move("gripper above puck")
    # Next, move the gripper around the puck.
    if check("the robot's gripper is above puck"):
        robot.put("gripper around puck")
    # Now, close the gripper around the puck.
    if check("the robot's gripper is near puck"):
        robot.close("gripper around puck")
    # We have the puck, so move the gripper high in the air and out of the way
    # of the wall.
    if check("the robot's gripper is near puck