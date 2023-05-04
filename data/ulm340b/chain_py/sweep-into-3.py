
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube by pulling down on it
    #  3. Move the cube to the goal
    # Put the gripper above the cube so that we don't bump it when trying to
    # grab it.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # As long as the gripper is above the cube, pull the gripper down to grab
    # the cube.
    # The cube is large enough that the gripper doesn't need to be around the
    # cube to grab it.
    if check("the robot's gripper is above cube"):
        robot.grab("cube")
    # If the gripper is still above the cube and open, it probably didn't grab
    # it, so move back down to try again.
    if check("the robot's gripper is above cube and the robot's gripper is open"):
        robot.pull("gripper down on cube")
    # If the gripper is near the cube and closed, maybe we grabbed it and can
    # move it to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    if check("the robot's gripper is near cube and the robot's gripper is closed"):
        robot.place("cube at goal")

# hook-into: pick up the mug by hooking it and put it at the target location
def hook_into(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Hook gripper around the mug handle
    #  3. Pull the mug to the goal
    # Put the gripper above the mug handle so that we don't bump it when trying
    # to grab it.
    if check("the robot's gripper is not above mug handle"):
        robot.put("gripper above mug handle")
    # As long as the gripper is above the mug handle, move the gripper around it
    # to hook it.
    # Since we're hooking from the front, check if the gripper is lined up with
    # the mug handle from the front instead of around it.
    if check("the robot'