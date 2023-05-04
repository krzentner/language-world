
"""

def make_paragraphs(s):
    paragraphs = []
    text = [s]
    while True:
        i = 0
        for sentence in text:
            if len(sentence) <= 250:
                paragraphs.append(sentence)
                break
            paragraphs.append(sentence[:i])
            i += 1
        if i == len(sentence):
            break
        text = [sentence[i:]]
    return paragraphs

tasks = {
    "button-press-topdown":"""

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.
    """,
    "drawer-close":"""

The task `drawer-close` requires the robot to push the drawer closed.
To push the drawer closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.
    """,
    "door-open":"""

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot'