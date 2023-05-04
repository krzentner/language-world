
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Move puck away from wall
    #  4. Move puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it away from the wall, then to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck away from the wall and then to the goal")

# stack: pick up the block and put it on top of the target block
def stack(robot):
    # Steps:
    #  1. Put gripper above the block
    #  2. Drop gripper around the block
    #  3. Close gripper around the block
    #  4. Lift the block to a little above the goal
    #  5. Place the block on the goal
    # First, put the gripper roughly above block, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the block"):
        robot.place("gripper above block")
    # If the gripper isn't around the block, put it around the block.
    if check("the robot's gripper is not around the block and the robot's gripper is open"):
        robot.drop("gripper around the block