
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't above the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not below puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is above the robot's gripper"):
        robot.slide("the puck to the goal")

# pick-push: pick up the puck and push it from above to the goal
def pick_push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab the puck with the gripper
    #  3. Move the puck to goal
    # Because the puck is so light, it's okay to pick it up and push it from
    # above to the goal.
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.grab("puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we
 