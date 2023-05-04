
"""

TASK_PROMPTS = {
    'button-press-topdown': """
    To press button from above reliably, the robot should perform the following steps:
        - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
        - When the robot's gripper is vertically aligned with button, the robot should push down on button.
    """,
    'drawer-close': """
    To push drawer closed reliably, the robot should perform the following steps:
        - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
        - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.
    """,
    'drawer-open': """
    To pull drawer open reliably, the robot should perform the following steps:
        - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
        - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
        - When the robot's gripper is around drawer handle, the robot should pull away from drawer.
    """,
    'door-open': """
    To pull door open reliably, the robot should perform the following steps:
        - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
        - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
        - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.
    """,
    'window-open': """
    To slide window open to the left reliably, the robot should perform the following steps:
        - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
        - When the robot's gripper is near the window handle, the robot should slide window left.
        - When the robot's gripper is in front of the window handle, the robot should push window left harder.
    """,
    'window-close': """
    To slide window closed to the right reliably, the robot should perform the following steps:
        - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to