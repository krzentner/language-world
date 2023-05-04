"""

'''
    - When the robot's gripper is not above wall, the robot should put gripper above wall.
    - When the robot's gripper is near wall, the robot should reach to goal.
'''


def get_instructions_str(task_id: str) -> str:
    tasks = {
        "drawer-open": "The task `drawer-open` requires the robot to pull the drawer open. To pull the drawer open reliably, the robot should perform the following steps: \n    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.\n    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.\n    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.",
        "window-open": "The task `window-open` requires the robot to slide the window open to the left. To slide the window open to the left reliably, the robot should perform the following steps: \n    - When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.\n    - When the robot's gripper is near the window handle, the robot should slide window left.\n    - When the robot's gripper is in front of the window handle, the robot should push window left harder.",
        "door-open": "The task `door-open` requires the robot to pull the door open. To pull the door open reliably, the robot should perform the following steps: \n    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.\n    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.\n    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.",
        "window-close": "The task `window-close` requires the robot to slide the window closed to the right. To slide the window closed to the right reliably, the robot should perform the following steps: \n    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.\n    - When the robot's gripper is near the window handle, the robot should slide window right.\