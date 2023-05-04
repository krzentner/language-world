

If you can correctly complete this task, you'll be able to work with
my collaborator on more complex programs.''')


def check(condition):
    raise NotImplementedError


if __name__ == "__main__":
    HIT_ONBOARDING.main(HIT_ONBOARDING.demo_world())

# end demo

def check(condition):
    return True


def door_open(robot):
    if check('the robot\'s gripper is not almost vertically aligned with door handle'):
        robot.move_gripper('almost vertically aligned with the door handle',
                           close_gripper=True)
    if check('the robot\'s gripper is vertically aligned with door handle'):
        robot.move_gripper('left of the door handle')


def drawer_open(robot):
    if check('the robot\'s gripper is not vertically aligned with drawer handle'):
        robot.move_gripper('vertically aligned with the drawer handle')
    if check('the robot\'s gripper is vertically aligned with drawer handle and the robot\'s gripper is not around drawer handle'):
        robot.move_gripper('around the drawer handle')
    if check('the robot\'s gripper is around drawer handle'):
        robot.move_gripper('horizontally aligned with the drawer handle')


def drawer_close(robot):
    if check('the robot\'s gripper is not near the drawer handle'):
        robot.move_gripper('near the drawer handle')
    if check('the robot\'s gripper is forward aligned with drawer handle'):
        robot.move_gripper('around the drawer handle')


def reach(robot):
    if check('the robot\'s gripper is not near reach target'):
        robot.move_gripper('near the reach target')


def push(robot):
    if check('the robot\'s gripper is not above puck and the robot\'s gripper is not vertically aligned with the puck'):
        robot.move_gripper('vertically aligned with the puck')
    if check('the robot\'s gripper is vertically aligned with the puck and the robot\'s gripper is not near puck'):
        robot.move_gripper('above the puck', close_gripper=True)
    if check('the robot\'s gripper is near the puck and the puck is below the robot\'