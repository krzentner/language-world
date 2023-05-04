
"""

TASK_COMMENTS = [
    # button-press-topdown: push the button down from above
    {
        "text": "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.",
        "image": os.path.join(ASSETS_ROOT, "button_press_topdown.gif"),
        "comment": """\
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")""",
    },
    # drawer-open: pull the drawer open
    {
        "text": "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.",
        "image": os.path.join(ASSETS_ROOT, "drawer_open.gif"),
        "comment": """\
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")""",
    },
    # peg-insert-side: grab the peg and insert it into the hole from the side
    {
        "text": "Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.",
        "image": os.path.join(ASSETS_ROOT, "peg_insert_side.gif"),
        "comment": """\
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg