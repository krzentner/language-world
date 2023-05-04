
"""
    instructions = [
        r'Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.',
        r'\nHere\'s some code that demonstrates how the robot can do a variety of tasks:',
        r'\n\n'
        r'```',
        # r'\n# reach: reach to the target location',
        r'def reach(robot):\n\t\tif check("the robot\'s gripper is not near reach target"):\n\t\t\trobot.reach("to goal")',
        # r'\n# button-press-topdown: push the button down from above',
        r'def button_press_topdown(robot):\n\t\tif check("the robot\'s gripper is not vertically aligned with button"):\n\t\t\trobot.put("gripper above button")\n\t\tif check("the robot\'s gripper is vertically aligned with button"):\n\t\t\trobot.push("down on button")',
        # r'\n# peg-insert-side: grab the peg and insert it into the hole from the side',
        r'def peg_insert_side(robot):\n\t\tif check("the robot\'s gripper is not vertically aligned with the peg"):\n\t\t\trobot.put("gripper above peg")\n\t\tif check("peg is not left of the robot\'s gripper and peg is not forward aligned with the robot\'s gripper"):\n\t\t\trobot.grab("peg")\n\t\tif check("the robot\'s gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):\n\t\t\trobot.align("peg to hole")\n\t\tif check("peg is horizontally aligned with hole"):\n\t\t\trobot.insert("peg into hole")',
        # r'\n# drawer-close: push the drawer close',
        r'def drawer_close(robot):\n\t\tif check("the robot\'s gripper is not near the drawer handle"):\n\t\t\trobot.grab("drawer handle")\n\t\tif check("the robot\'s gripper is forward aligned with drawer handle"):\n\t\t\trobot.push("drawer closed")',
        # r'\n# drawer-open: pull the drawer open',
        r'def