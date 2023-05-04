

and then write a program, in the same style as the above examples, that performs the basketball task.





# This is not an example code
def basketball(robot):
    if check('the robot\'s gripper is not near basketball'):
        robot.grab('basketball')
    if check('the robot\'s gripper is near basketball and the robot\'s gripper is not around basketball'):
        robot.put('gripper around basketball')
    if check('the robot\'s gripper is around basketball and the basketball is forward aligned with the robot\'s gripper'):
        robot.raise('basketball to goal')
    if check('basketball is not vertically aligned with the hoop and the robot\'s gripper is near the basketball'):
        robot.align('basketball to hoop')
    if check('the basketball is vertically aligned with the hoop and the robot\'s gripper is near the basketball'):
        robot.drop('basketball into hoop')

def reach(robot):
    if check('the robot\'s gripper is not near reach target'):
        robot.reach('to goal')

def door_open(robot):
    if check('the robot\'s gripper is not almost vertically aligned with door handle'):
        robot.put('gripper above door handle')
    if check('the robot\'s gripper is almost vertically aligned with the door handle and the robot\'s gripper is open'):
        robot.put('gripper around door handle')
    if check('the robot\'s gripper is vertically aligned with the door handle'):
        robot.pull('door open')

def drawer_close(robot):
    if check('the robot\'s gripper is not near the drawer handle'):
        robot.grab('drawer handle')
    if check('the robot\'s gripper is forward aligned with drawer handle'):
        robot.push('drawer closed')

def push(robot):
    if check('the robot\'s gripper is not above puck and the robot\'s gripper is not vertically aligned with the puck'):
        robot.put('the gripper above the puck')
    if check('the robot\'s gripper is vertically aligned with the puck and the robot\'s gripper is not near puck'):
        robot.push('the gripper into the puck')
    if check('the robot\'s gripper is near the puck and the puck