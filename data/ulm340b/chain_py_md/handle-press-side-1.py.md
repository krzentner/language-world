
"""

# TEMPLATE_CODE

# Steps:
#  1. Put gripper above the handle
#  2. Push down the handle

# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # If the robot's gripper isn't vertically aligned with the handle, move it
    # vertically aligned with the handle.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is vertically aligned with the handle, just push down on it.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("handle down")

# check: check the condition of the world
def check(cond):
    # TODO: Implement this function
    if cond == 'the robot\'s gripper is not near reach target':
        return robot.gripper.position.distance_to(robot.reach_target.position) > 0.10
    elif cond == 'the robot\'s gripper is near reach target':
        return robot.gripper.position.distance_to(robot.reach_target.position) <= 0.10
    elif cond == 'the robot\'s gripper is not above puck':
        return robot.gripper.position.z < robot.puck.position.z + 0.001
    elif cond == 'the robot\'s gripper is above puck':
        return robot.gripper.position.z >= robot.puck.position.z + 0.001
    elif cond == 'the robot\'s gripper is not vertically aligned with the puck':
        return robot.gripper.position.distance_to(robot.puck.position) > 0.025
    elif cond == 'the robot\'s gripper is vertically aligned with the puck':
        return robot.gripper.position.distance_to(robot.puck.position) <= 0.025
    elif cond == 'the robot\'s gripper is near puck':
        return robot.gripper.position.distance_to(robot.puck.position) <= 0.03
    elif cond == 'the robot\'s gripper is not near puck':
        return robot.gripper.position.distance_to(robot.puck.position) > 