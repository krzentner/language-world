
    # Steps:
    #  1. Put the gripper above the puck
    #  2. Grab the puck
    #  3. Put the gripper above the goal location
    #  4. Ungrab the puck
    # If the gripper is not above the puck, move it there.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is lined up with the puck but not near it, grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck")
    # If the gripper has the puck in it, we can move it to the goal.
    if check("the robot's gripper has puck"):
        robot.move("to goal")
    # Once the gripper is above the goal, release the puck.
    if check("the robot's gripper is above the goal and the robot's gripper has puck"):
        robot.release("puck")

# pick-place-wall: pick up the puck and hold it at the target location on a wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put the gripper above the puck
    #  2. Grab the puck
    #  3. Put the gripper on the wall, near the goal location
    #  4. Ungrab the puck
    # If the gripper is not above the puck, move it there.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is lined up with the puck but not near it, grab it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.grab("puck")
    # If the gripper has the puck in it, we can move it to the wall.
    if check("the robot's gripper has puck and the robot's gripper is not near the wall"):
        robot.move("to wall")
    # Once the gripper is