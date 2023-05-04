
"""

help_texts = {
    "button-press-topdown": help_text_button_press_topdown,
    "peg-insert-side": help_text_peg_insert_side,
    "drawer-open": help_text_drawer_open,
    "door-open": help_text_door_open,
    "drawer-close": help_text_drawer_close,
    "window-open": help_text_window_open,
    "window-close": help_text_window_close,
    "pick-place": help_text_pick_place,
    "reach": help_text_reach,
    "push": help_text_push,
    "door-close": help_text_door_close,
}

help_text = help_texts[task_name]

# help_text_button_press_topdown = '''
# The task `button-press-topdown` requires the robot to push the button down from above.
# To push the button down from above reliably, the robot should perform the following steps:
#     Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
#     Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
#     - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
#     Now that the gripper is lined up, just push down on the button.
#     - When the robot's gripper is vertically aligned with button, the robot should push down on button.
# '''


help_text_peg_insert_side = '''
The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into the hole from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Slide the peg sideways into the hole
    First, put the gripper above the peg.
    - When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
    If the peg becomes left of the gripper, go back to putting the gripper above the peg. Because the peg is a long object, check if the gripper is lined up with it from the front instead of around it.
    - When peg is not left