
    - When the robot's gripper is not vertically aligned with the handle, the robot should put gripper above handle.
    - When the robot's gripper is vertically aligned with handle and the robot's gripper is open, the robot should drop gripper around handle.
    - When the robot's gripper is around handle and the robot's gripper is open, the robot should close gripper around handle.
    - When the robot's gripper is vertically aligned with handle, the robot should pull handle down.
"""

INSTRUCTIONS_TEMPLATE = """
In this task, you need to program a robot to reach the goal.
To complete this task reliably, the robot should perform the following steps:
    - If the robot's gripper is not near reach target, the robot should reach to goal.

In this task, you need to program a robot to slide the puck to the target location.
To complete this task reliably, the robot should perform the following steps:
    - If the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - If the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - If the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

In this task, you need to program a robot to pull the door open.
To complete this task reliably, the robot should perform the following steps:
    - If the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - If the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - If the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

In this task, you need to program a robot to pull the drawer open.
To complete this task reliably, the robot should perform the following steps:
    - If the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    - If the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    - If the robot's gripper is around drawer handle, the robot should pull away from drawer.

In this task, you need to program a robot to slide the window closed to the right.