
"""
    goal = ['stick-push']

    def program_examples(self) -> List[List[str]]:
        return [
            ['the robot\'s gripper is not vertically aligned with button', 'put', 'gripper above button'],
            ['the robot\'s gripper is vertically aligned with button', 'push', 'down on button'],
            ['the robot\'s gripper is not vertically aligned with drawer handle', 'put', 'gripper above drawer handle'],
            [
                'the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle',
                'put', 'gripper around drawer handle'
            ],
            ['the robot\'s gripper is around drawer handle', 'pull', 'away from drawer'],
            ['the robot\'s gripper is not almost vertically aligned with door handle', 'put', 'gripper above door handle'],
            [
                'the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open',
                'put', 'gripper around door handle'
            ],
            ['the robot\'s gripper is vertically aligned with the door handle', 'pull', 'door open'],
            ['the robot\'s gripper is not near the drawer handle', 'grab', 'drawer handle'],
            ['the robot\'s gripper is forward aligned with drawer handle', 'push', 'drawer closed'],
            ['the robot\'s gripper is not vertically aligned with the window handle and the robot\'s gripper is below the window handle',
             'move',
             'gripper to right of window handle'],
            ['the robot\'s gripper is near the window handle', 'slide', 'window left'],
            ['the robot\'s gripper is in front of the window handle', 'push', 'window left harder'],
            ['the window handle is right of the robot\'s gripper and the robot\'s gripper is not near the window handle',
             'move',
             'gripper to left of window handle'],
            ['the robot\'s gripper is near the window handle', 'slide', 'window right'],
            ['the robot\'s gripper is in front of the window handle', 'push', 'window right harder'],
            ['the robot\'s gripper is not vertically aligned