
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube
    #  3. Sweep the cube sideways to the goal
    #  4. Drop the cube
    # First, we need to line up the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    # If the gripper is aligned but not around the cube, drop it around the cube.
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.grab("cube")
    # If the gripper is aligned and around the cube, we can sweep it to the goal.
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is around cube"):
        robot.sweep("cube to goal")
    # If the gripper is not below the cube, drop the cube by releasing the
    # gripper and lifting it.
    if check("the robot's gripper is not below cube"):
        robot.release("cube")

# sweep-into-goal: slide the cube into the goal
def sweep_into_goal(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Grab cube
    #  3. Sweep the cube into the goal
    #  4. Drop the cube
    # First, we need to line up the gripper above the cube.
    if check("the robot's gripper is not vertically aligned with cube"):
        robot.put("gripper above cube")
    # If the gripper is aligned but not around the cube, drop it around the cube.
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is not around cube"):
        robot.grab("cube")
    # If the gripper is aligned and around the cube, we can sweep it into the
    # goal.
    if check("the robot's gripper is vertically aligned with cube and the robot's gripper is around cube"):
        robot.sweep("cube into goal")
    # If the gripper is not below the cube, drop the cube by releasing the
    # gripper and lifting it.
    if check