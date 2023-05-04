

"""

# Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


# The task `button-press-topdown` requires the robot to push the button down from above.
# To push the button down from above reliably, the robot should perform the following steps:
#     Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
#     Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
#     - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
#     Now that the gripper is lined up, just push down on the button.
#     - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button

# The task `door-open` requires the robot to pull the door open.
# To pull the door open reliably, the robot should perform the following steps:
#     Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
#     First, put the gripper mostly above the door handle.
#     - When the robot's gripper is not almost vertically aligned with door handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is closed
#     As long as the gripper is almost lined up, closing it should line it up all the way.
#     - When the robot's gripper is vertically aligned with the door handle, move the robot's gripper until the robot's gripper is left of the door handle

# The task `drawer-open` requires the robot to pull the drawer open.
# To pull the drawer open reliably, the robot should perform the following steps:
#     Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
#     We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
#     - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
#     Once the gripper is lined up above the drawer handle, we should