
    # Steps:
    #  1. Put gripper in front of the puck
    #  2. Push puck toward target
    # Move the gripper in front of the puck.
    if check("the robot's gripper is not in front of puck"):
        robot.put("gripper in front of puck")
    # Push the puck towards the target.
    if check("the robot's gripper is in front of puck"):
        robot.push("puck towards goal")

# stack: put the block on top of the target object
def stack(robot):
    # Steps:
    #  1. Put gripper on top of the block
    #  2. Drop gripper down
    #  3. Move gripper above the target
    #  4. Drop gripper down
    # Put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper on top of block")
    # Drop the gripper down.
    if check("the robot's gripper is above the block"):
        robot.put("gripper down around block")
    # Move gripper above the target.
    if check("the robot's gripper is around the block"):
        robot.move("gripper above target")
    # Drop gripper down
    if check("the robot's gripper is above the target"):
        robot.put("gripper down around the target")

# stack-side: put the block in front of the target object
def stack_side(robot):
    # Steps:
    #  1. Put gripper on top of the block
    #  2. Drop gripper down
    #  3. Move gripper above the target
    #  4. Drop gripper down
    # Put the gripper above the block.
    if check("the robot's gripper is not above the block"):
        robot.put("gripper on top of block")
    # Drop the gripper down.
    if check("the robot's gripper is above the block"):
        robot.put("gripper down around block")
    # Move gripper above the target.
    if check("the robot's gripper is around the block"):
        robot.move("g