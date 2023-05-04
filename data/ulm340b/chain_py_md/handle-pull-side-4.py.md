
"""
def handle_pull_side(robot):
    """Steps:
    1. Put the gripper above the handle
    2. Put the gripper around the handle
    3. Pull the handle up
    """
    #If the robot's gripper is not vertically aligned with handle:
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    #If the robot's gripper is vertically aligned with handle but not around handle:
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.put("gripper around handle")
    #If the robot's gripper is not forward aligned with handle:
    if check("the robot's gripper is not forward aligned with handle"):
        robot.pull("handle")


def check(condition):
    """Return True if the condition is satisfied
    Parameters
    ----------
    condition : str
        A condition. See README.md for format.
    """
    return True


def robot_reach(robot):
    """Reach towards the target location
    Parameters
    ----------
    robot : Robot
        The robot to control.
    """
    robot.gripper_open()
    robot.reach_target()


def robot_push(robot):
    """Slide the puck to the target location
    Parameters
    ----------
    robot : Robot
        The robot to control.
    """
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")


def robot_window_close(robot):
    """Slide the window closed to the right
    Parameters
    ----------
    robot : Robot
        The robot to control.
    """
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
 