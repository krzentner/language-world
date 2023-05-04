
To pull the wrench off the peg reliably, what steps the robot should perform?
"""


instructions = [
    {
        'title': 'peg-insert-side',
        'content': (
            'The task `peg-insert-side` requires the robot to grab the peg and '
            'insert it into the hole from the side. To grab the peg and insert it '
            'into the hole from the side reliably, the robot should perform the '
            'following steps: \n\n'
            'Steps:  1. Put gripper above the peg  2. Grab the peg with the '
            'gripper  3. Line the peg up with the hole  4. Slide the peg sideways '
            'into the hole \n\n'
            'First, put the gripper above the peg. \n\n'
            '- When the robot\'s gripper is not vertically aligned with the peg, '
            'move the robot\'s gripper until the robot\'s gripper is vertically '
            'aligned with the peg \n\n'
            'If the peg becomes left of the gripper, go back to putting the '
            'gripper above the peg. Because the peg is a long object, check if '
            'the gripper is lined up with it from the front instead of around it. '
            '\n\n'
            '- When peg is not left of the robot\'s gripper and peg is not '
            'forward aligned with the robot\'s gripper, move the robot\'s gripper '
            'until the robot\'s gripper is forward aligned with the peg and the '
            'robot\'s gripper is closed \n\n'
            'As long the gripper is still mostly around the peg and the peg '
            'isn\'t lined up with the hole, line up the peg with the hole. \n\n'
            '- When peg is horizontally aligned with hole, move the robot\'s '
            'gripper until the robot\'s gripper is above the peg \n\n'
            'If the peg is lined up with the hole to the side, insert it. \n\n'
            '- When the robot\'s gripper is forward aligned with the peg and the '
            'peg is not horizontally aligned with hole, move the robot\'s gripper '
            'until the robot\'s gripper is horizontally aligned with hole')
    },
    {
        'title