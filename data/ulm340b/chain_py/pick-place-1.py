
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Line the puck up with the goal
    #  4. Put the puck in the goal
    #  5. Move the gripper above the puck
    # First, put the gripper above the puck.
    if check("the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the puck is not aligned with the gripper as seen from the front, move
    # the gripper down to grab the puck.
    if check("the puck is not horizontally aligned with the gripper as seen from the front and the puck is not forward aligned with the gripper and the puck is below the gripper"):
        robot.grab("the puck")
    # If the gripper is not near the puck and the puck is not lined up with the
    # goal, line up the gripper with the goal.
    if check("the robot's gripper is not near the puck and the puck is not horizontally aligned with the goal"):
        robot.align("the puck with the goal")
    # Now that the puck is lined up with the goal, put the gripper above the
    # goal.
    if check("the robot's gripper is not above the goal"):
        robot.put("the gripper above the goal")
    # If the gripper is above the goal, we can put the puck there.
    if check("the robot's gripper is above the goal"):
        robot.insert("the puck into the goal")
    # Finally, move the gripper away from the puck and goal.
    if check("the robot's gripper is near the goal"):
        robot.put("the gripper away from the puck and goal")

# pick-place-side: pick up the puck and hold it at the target location (from the side)
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper next to puck
    #  2. Grab the puck with the gripper
    #  3. Line the puck up with the goal
    #  4. Put the puck in the goal
    #  5. Move the gripper next to the puck
    # First, put the