



'''

def check(string):
    print (string)
    return eval(input("Is this true? ")[:1])

def coffee_push(robot):
    if check('the robot\'s gripper is not above the mug'):
        robot.put('gripper above mug')
    if check('the robot\'s gripper is not near the mug'):
        robot.drop('gripper on mug')
    if check('the robot\'s gripper is near the mug and the mug is below the robot\'s gripper'):
        robot.push('the gripper into the mug')
    if check('the robot\'s gripper is near the mug and the mug is below the robot\'s gripper'):
        robot.slide('the mug to the goal')

'''

# The above code can't be tested using check() -- the problem is
# that check() is just a print statement now. Can you fix check()
# so that it works like eval(input(''))?
'''

# check : eval(input('Is this true? '))

coffee_push(coffee_push)

'''

Here are several more tasks the robot can perform.  Can you write programs
that perform each task?

1. `press-lever`.
2. `slider-push`.
3. `slider-push-alt`.
4. `slider-pull`.
5. `reach-to-goal`.


'''


'''

# press-lever: press the lever down
def press_lever(robot):
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    if check("the robot's gripper is vertically aligned with lever"):
        robot.push("lever down")


# slider-push: slide the puck to the target location
def slider_push(robot):
    if check("the robot's gripper is not above the slider"):
        robot.put("gripper above slider")
    if check("the robot's gripper is above the slider and the robot's gripper is not in front of the slider"):
        robot.push("gripper above slider")
    if check("the robot's gripper is near slider"):
        robot.slide("slider to target")


# slider-push-alt: slide the puck to the target location
def slider_push_alt(robot):
   