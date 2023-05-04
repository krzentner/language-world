


'''


class Task(object):
    def __init__(self, robot):
        self.robot = robot
        self.success = False

    def step(self):
        '''
        Return False if the robot is in a bad configuration, else True.
        '''
        raise NotImplementedError('step() must be implemented in the subclass.')

    def run(self):
        '''
        Keeps running step() over and over again until done.
        '''
        t = 0
        while not self.step():
            t += 1
            if t > 1000:
                print('task timed out')
                break
        self.success = True


class Reach(Task):
    def step(self):
        if self.robot.check_condition('the robot\'s gripper is not near reach target'):
            self.robot.move_gripper('near the reach target')
            return False
        return True


class Push(Task):
    def step(self):
        if self.robot.check_condition('the robot\'s gripper is not above puck and the robot\'s gripper is not vertically aligned with the puck'):
            self.robot.move_gripper('vertically aligned with the puck')
            return False
        if self.robot.check_condition('the robot\'s gripper is vertically aligned with the puck and the robot\'s gripper is not near puck'):
            self.robot.move_gripper('above the puck', close_gripper=True)
            return False
        if self.robot.check_condition('the robot\'s gripper is near the puck and the puck is below the robot\'s gripper'):
            self.robot.move_gripper('above the target location')
            return False
        return True


class ButtonPressTopdown(Task):
    def step(self):
        if self.robot.check_condition('the robot\'s gripper is not vertically aligned with button'):
            self.robot.move_gripper('vertically aligned with the button', close_gripper=True)
            return False
        if self.robot.check_condition('the robot\'s gripper is vertically aligned with button'):
            self.robot.move_gripper('near the button')
            return False
        return True


class DoorOpen(Task):
    def step(self):
        if self.robot.check_condition('the robot\'s gripper is not almost vertically aligned with door handle'):
            