
"""


task_descriptions = {
    'button-press-topdown': task_instructions['button-press-topdown'],
    'drawer-open': task_instructions['drawer-open'],
    'drawer-close': task_instructions['drawer-close'],
    'door-open': task_instructions['door-open'],
    'window-close': task_instructions['window-close'],
    'window-open': task_instructions['window-open'],
    'peg-insert-side': task_instructions['peg-insert-side'],
    'reach': task_instructions['reach'],
    'push': task_instructions['push'],
    'pick-place': task_instructions['pick-place'],
    'sweep': task_instructions['sweep'],
}


# TASK DESCRIPTIONS FOR V1
task_descriptions_v1 = {
    'button-press-topdown': """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
- When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
Now that the gripper is lined up, just push down on the button.
- When the robot's gripper is vertically aligned with button, the robot should push down on button.
""",
    'drawer-open': """
Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.


The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
- When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
Once the gripper is lined up above the drawer handle, we should be able