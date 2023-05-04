
"""

task_window_close = "window-close"


window_close_subtasks = """
- When the robot's gripper is not vertically aligned with the window handle, the robot should put gripper above window handle.
- When the robot's gripper is near window handle, the robot should push window right.
- When the robot's gripper is in front of window handle, the robot should push window right harder.
"""


task_window_close_demo = """

Hello.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the window handle, the robot should put gripper above window handle.
    - When the robot's gripper is near window handle, the robot should push window right.
    - When the robot's gripper is in front of window handle, the robot should push window right harder.

"""

task_window_close_demo_2 = """

Hello.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the window handle, the robot should place gripper above window handle.
    - When the robot's gripper is near the window handle, the robot should push window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

"""

task_window_close_demo_3 = """

Hello.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the window handle, the robot should place gripper above window handle.
    - When the robot's gripper is not near the window handle, the robot should push gripper into window.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

"""




def create_window_close_task(mturk_agent, task_desc, task_desc_demo, **task_kwargs):
    
    task_window_close = create_task(mturk_agent, 
        task_desc=task_desc,
        task_desc_demo=task_desc_demo,
        policy_time_step_spec=task