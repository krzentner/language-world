
'''

def lever_pull(robot):
    if check("the robot's gripper is above the lever"):
        robot.grab("the lever")
    if check("the robot's gripper is near the lever"):
        robot.pull("the lever up")

## Test
'''
# lever-pull: rotate the lever up
def lever_pull(robot):
    if check("the robot's gripper is above the lever"):
        robot.grab("the lever")
    if check("the robot's gripper is near the lever"):
        robot.pull("the lever up")
'''





'''
######################################################################
#                        Question 4 (Pong)                           #
######################################################################


def agent(ob):
    if ob['player'] == 'a':
        ob['player'] = 'b'
    else:
        ob['player'] = 'a'
    if check("ob['player'] is 'a'"):
        return 1  # Move upward
    else:
        return 0  # Move downward


def opponent(ob):
    if check("ob['player'] is 'a'"):
        return 1  # Move upward
    else:
        return 0  # Move downward


def play(env, policy=agent):
    ob = env.reset()
    while True:
        ac = policy(ob)
        ac = int(ac)
        ob, rew, done, info = env.step(ac)
        if done:
            break


## Test

def agent(ob):
    if ob['player'] == 'a':
        ob['player'] = 'b'
    else:
        ob['player'] = 'a'
    if check("ob['player'] is 'a'"):
        return 1  # Move upward
    else:
        return 0  # Move downward


def opponent(ob):
    if check("ob['player'] is 'a'"):
        return 1  # Move upward
    else:
        return 0  # Move downward


def play(env, policy=agent):
    ob = env.reset()
    while True:
        ac = policy(ob)
        ac = int(ac)
        ob, rew, done, info = env.