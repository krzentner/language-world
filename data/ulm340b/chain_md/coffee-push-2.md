:


"""

def train(args):
    from collections import namedtuple
    Instruction = namedtuple('Instruction', [
            'steps',
            'description',
            'instructions',
            'robot_actions',
            ])

    instructions = []

    instructions.append(Instruction(
            'Push Button',
            '''
The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, the robot should push down on button.
''',
            [
                'The task `button-press-topdown` requires the robot to push the button down from above.\n'
                'To push the button down from above reliably, the robot should perform the following steps:'
                '\nSteps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top',
                'Because this is "topdown", we just need to line up the gripper from above. Line up the robot\'s gripper from above.'
                '\n- When the robot\'s gripper is not vertically aligned with button, the robot should put gripper above button.',
                'Now that the gripper is lined up, just push down on the button.'
                '\n- When the robot\'s gripper is vertically aligned with button, the robot should push down on button.',
            ],
            ['LINE_UP_GRIPPER_AS_VIEWED_FROM_ABOVE', 'PUSH_DOWN_ON_BUTTON_FROM_THE_TOP'],
            ))

    instructions.append(Instruction(
            'Pull Drawer Open',
            '''
The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer