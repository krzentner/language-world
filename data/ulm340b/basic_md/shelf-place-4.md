
"""
# <solution>
# When the robot's gripper is not above the block, the robot should place gripper above block.
# When the robot's gripper is not around block and the robot's gripper is open, the robot should drop gripper around block.
# When the robot's gripper is near block and the robot's gripper is open, the robot should close gripper around block.
# When the robot's gripper is above block and the robot's gripper is closed, the robot should place block at goal.
# </solution>

instructions_task_pick_place_drawer = """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.

The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
    - When the robot's gripper is around drawer handle, the robot should pull away from drawer.

The task `pick-place` requires the robot to pick up the puck and place it on top of the drawer.
To pick up the puck and place it on top of the drawer reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck on drawer.

The task `shelf-place` requires the robot to pick up the block and place it at the target location.
To pick up the block and place it at the target location reliably, the robot should perform the following steps: