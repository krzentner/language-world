

# %%

# disassemble: pull the wrench off the peg
def disassemble(robot):
    print("Here's an example of a 'disassemble' action.")

# %%

# %%

# disassemble: pull the wrench off the peg
def disassemble(robot):
    print("Here's an example of a 'disassemble' action.")

# First, put the gripper around the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.move_gripper("above the wrench")

# %%

# disassemble: pull the wrench off the peg
def disassemble(robot):
    print("Here's an example of a 'disassemble' action.")

# First, put the gripper around the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.move_gripper("above the wrench")

# Once the gripper is around the wrench, we can just pull the wrench off the
# peg.
if check("the robot's gripper is around the wrench"):
    robot.move_gripper("below the wrench")

# %%

# disassemble: pull the wrench off the peg
def disassemble(robot):
    print("Here's an example of a 'disassemble' action.")

# First, put the gripper around the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.move_gripper("above the wrench")

# Once the gripper is around the wrench, we can just pull the wrench off the
# peg.
if check("the robot's gripper is around the wrench"):
    robot.move_gripper("below the wrench")

# Once the wrench is free from the peg, we're done!
if check("the robot's gripper is not around the wrench"):
    robot.move_gripper("free from the wrench")

# %%


# disassemble: pull the wrench off the peg
def disassemble(robot):
    print("Here's an example of a 'disassemble' action.")

# First, put the gripper around the wrench.
if check("the robot's gripper is not above the wrench"):
    robot.move_gripper("above the wrench", close_gripper=True)

# Once the gripper is around the wrench, we can just pull the wrench off the
# peg.
if check("the robot's gripper is around the wrench"):
    robot.move_