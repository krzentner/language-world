

After you complete that task, I will have some other problems for you to
complete.

Thanks, you can begin now.

'''

# Helper function
def noop(robot, state):
    return (1, state)

def noop_close_gripper(robot, state):
    return (1, robot.close_gripper(), state)

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around the faucet
    #  2. Push the gripper right
    # First, put the gripper around the faucet.
    if check("the robot's gripper is not near the faucet"):
        robot.move_gripper("above the faucet", close_gripper=True)
    # Once the gripper is around the faucet, we can just push the faucet to the right.
    if check("the robot's gripper is not forward aligned with the faucet and the robot's gripper is near the faucet"):
        robot.move_gripper("above the faucet")

# Helper functions for the other problems
def forward(x, z):
    return (0, 1) if z is not None else (0, x)

def behind(z, x):
    return (0, 1) if x is not None else (0, z)

def next_to(x, z):
    return (0, 1) if x is not None else (0, z)

def left_of(x, z):
    return (0, 1) if x is not None else (0, z)

def left_of_2(z, x):
    return (0, 1) if x is not None else (0, z)

def left_of_3(x, z):
    return (0, 1) if x is not None else (0, z)

def left_of_4(z, x):
    return (0, 1) if x is not None else (0, z)

def around(z, x):
    return (0, 1) if z is not None else (0, x)

def near(z, x):
    return (0, 1) if x is not None else (0, z)

def below(x, z):
    return (0, 1) if x is not None else (0, z)

def below_2(z, x):
    return (0, 1) if z