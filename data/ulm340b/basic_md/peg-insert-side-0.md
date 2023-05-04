
"""

INTRO_DIALOG_TEXT_VERSION = """
    Here is a set of instructions that will be helpful for controlling the robot. You can refer back to them anytime, just ask.

    The task `door-open` requires the robot to pull the door open.
    To pull the door open reliably, the robot should perform the following steps:
        - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
        - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
        - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

    The task `drawer-open` requires the robot to pull the drawer open.
    To pull the drawer open reliably, the robot should perform the following steps:
        - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
        - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
        - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

    The task `drawer-close` requires the robot to push the drawer close.
    To push the drawer close reliably, the robot should perform the following steps:
        - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
        - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

    The task `reach` requires the robot to reach to the target location.
    To reach to the target location reliably, the robot should perform the following steps:
        - When the robot's gripper is not near reach target, the robot should reach to goal.

    The task `push` requires the robot to slide the puck to the target location.
    To slide the puck to the target location reliably, the robot should perform the following steps:
        - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
        - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
        - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should