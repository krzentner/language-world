
    - When the robot's gripper is not near dial and the robot's gripper is not vertically aligned with dial, the robot should grab dial from above.
    - When the robot's gripper is near dial and the robot's gripper is not vertically aligned with dial, the robot should move the gripper to dial.
    - When the robot's gripper is near dial and the robot's gripper is vertically aligned with dial, the robot should twist dial.

The task `handle-press` requires the robot to press the door handle.
To press the door handle reliably, what steps the robot should perform?
    - When the robot's gripper is not near door handle and the robot's gripper is not vertically aligned with door handle, the robot should move gripper to door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not near door handle, the robot should grab door handle.
    - When the robot's gripper is near door handle and the robot's gripper is open, the robot should squeeze door handle.

The task `window-open-hard` requires the robot to slide the window open harder.
To slide the window open harder reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with window handle and the robot's gripper is below window handle, the robot should place gripper around window handle.
    - When the robot's gripper is vertically aligned with window handle and the robot's gripper is not forward aligned with window handle, the robot should slide window left.
    - When the robot's gripper is forward aligned with window handle, the robot should push window left harder.

The task `window-close-hard` requires the robot to slide the window closed harder.
To slide the window closed harder reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with window handle and the robot's gripper is above window handle, the robot should place gripper around window handle.
    - When the robot's gripper is vertically aligned with window handle and the robot's gripper is not forward aligned with window handle, the robot should slide window right.
    - When the robot's gripper is forward aligned with window handle, the robot should push window right harder.

"""

print("Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.")
# 
# peg-insert-side
# The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
