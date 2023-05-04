

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?

The task `peg-unstack` requires the robot to grab the top of the peg and lift it off of the bottom of the peg.
To grab the top of the peg and lift it off of the bottom of the peg reliably, what steps the robot should perform?

'''



task_templates = {
    'reach': Template("""
The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    Steps:  1. Reach towards the target
    We don't have any objects to manipulate, so we can just move the robot's gripper directly to the target location
    - When the robot's gripper is not near reach target, the robot should <action> to goal.
"""),
    'peg-insert-side': Template("""
The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
    - When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
    If the peg is lined up with the hole to the side, insert it.
    - When peg is horizontally aligned with hole, the robot should insert peg into hole.
"""),
    'window-close': Template("""
The task `window-close` requires the robot to slide the window closed to the right.
To slide the window