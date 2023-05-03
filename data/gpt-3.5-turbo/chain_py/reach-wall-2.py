# Steps:
    #  1. Move gripper above the wall
    #  2. Grab the top of the wall
    #  3. Move gripper to the goal location
    #  4. Release the gripper to drop the wall
    # This task requires the robot to reach over a short wall to get to the goal
    # location.
    # First, move the gripper above the wall.
    if check("the robot's gripper is not above the wall"):
        robot.move("gripper above the wall")
    # If the gripper is above the wall, we can grab the top of the wall.
    if check("the robot's gripper is above the wall and the robot's gripper is open"):
        robot.grab("the top of the wall")
    # Once we're holding the top of the wall, we can move the gripper to the goal
    # location while keeping the wall in hand.
    if check("the robot's gripper is holding the top of the wall and is not at the goal location"):
        robot.move("gripper to the goal location while holding the wall")
    # Once we're at the goal location, we can release the gripper to drop the wall
    # and complete the task.
    if check("the robot's gripper is at the goal location while still holding the wall"):
        robot.release("the top of the wall")