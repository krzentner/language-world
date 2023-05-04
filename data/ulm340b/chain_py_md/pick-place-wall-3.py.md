

The short wall blocks the path from above, so we can't do the same top-down
motion that we did for `pick_place`.
"""
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above puck to the right of the wall
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck to the right of the wall, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck to the right of the wall"):
        robot.place("gripper above puck to the right of the wall")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck to the right of the wall and the robot's gripper is closed"):
        robot.place("puck at goal")



# This is the end of the task. Don't code below here!

# Here are some tasks that we defined earlier. You can write your own definitions here.
# window_close
window_close=robot_code(code_text.splitlines(), 'window_close', ['the window handle is left of the robot\'s gripper and the robot\'s gripper is not near the window handle', 'the robot\'s gripper is near the window handle', 'the robot\'s gripper is in front of the window handle'])

# window_open
window_open=robot_code(code_text.splitlines(), 'window_