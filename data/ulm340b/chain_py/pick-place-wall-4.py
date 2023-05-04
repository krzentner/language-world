
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Lift gripper above wall
    #  5. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to lift the puck over the wall.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.lift("gripper above wall")
    # If the gripper is above the wall and the puck is still near the gripper,
    # we probably lifted the puck over the wall, so try to move the puck to the
    # goal location.
    if check("the robot's gripper is above the wall and the robot's gripper is above the puck"):
        robot.place("puck at goal")

# pick-place-back: pick up the puck and hold it at the target location from the other side
def pick_place_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move around and place the puck at goal
    # The robot is on the opposite side of the table than normal for pick-place,
   