
''',
                {
                    'button-press-topdown': [
                        'put gripper above button',
                        'push down on button'
                    ],
                    'drawer-open': [
                        'put gripper above drawer handle',
                        'put gripper around drawer handle',
                        'pull away from drawer'
                    ],
                    'drawer-close': [
                        'grab drawer handle',
                        'push drawer closed'
                    ],
                    'door-open': [
                        'put gripper above door handle',
                        'put gripper around door handle',
                        'pull door open'
                    ],
                    'window-close': [
                        'move gripper to left of window handle',
                        'slide window right',
                        'push window right harder'
                    ],
                    'window-open': [
                        'move gripper to right of window handle',
                        'slide window left',
                        'push window left harder'
                    ],
                    'peg-insert-side': [
                        'put gripper above peg',
                        'grab peg',
                        'align peg to hole',
                        'insert peg into hole'
                    ],
                    'push': [
                        'put the gripper above the puck',
                        'push the gripper into the puck',
                        'slide the puck to the goal'
                    ],
                    'reach': [
                        'reach to goal'
                    ],
                    'pick-place': [
                        'place gripper above puck',
                        'drop gripper around puck',
                        'close gripper around puck',
                        'place puck at goal'
                    ],
                },
                name='baseline'
            ),
            self.task(
                'sweep-into',
                """
The task `sweep-into` requires the robot to grab the cube and move it to the target location.
To grab the cube and move it to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the cube, the robot should put gripper above the cube.
    - When the robot's gripper is vertically aligned with the cube, the robot should put gripper around cube.
    - When the robot's gripper is around cube, the robot should push cube left.
    - When the robot's gripper is left of