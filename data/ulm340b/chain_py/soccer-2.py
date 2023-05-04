
    # Steps:
    #  1. Put gripper above soccer ball
    #  2. Start pushing down into the soccer ball
    #  3. Push the ball into the goal
    # The soccer ball is big, so we'll just push it instead of trying to grab it
    # Put the gripper above the soccer ball, so that we don't bump it when we try
    # to push it
    if check("the robot's gripper is not above soccer ball"):
        robot.put("gripper above soccer ball")
    # If the gripper is aligned with the ball from above, start pushing.
    if check("the robot's gripper is vertically aligned with soccer ball"):
        robot.push("gripper into soccer ball")
    # If the gripper is below the ball (like we're pushing on top of it), try to
    # push it into the goal.
    # Close the gripper to make sure it doesn't fall out of the gripper.
    if check("the robot's gripper is below soccer ball"):
        robot.slide("soccer ball into goal")

# pick-place-side: pick up the puck and hold it at the target location
def pick_place_side(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Move gripper sideways to the puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is above the puck, drop the gripper sideways around the
    # puck.
    if check("the robot's gripper is above puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper