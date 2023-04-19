
    # Steps:
    #  1. Put gripper above the puck
    #  2. Line the gripper up with the goal on the left
    #  3. Move into goal
    #  4. Let go of the puck
    # First, put the gripper roughly above puck.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the puck is left of the gripper and the gripper is not vertically
    # aligned with the goal, move the gripper to right of the puck.
    if check("the puck is left of the robot's gripper and the robot's gripper is not vertically aligned with the goal"):
        robot.align("gripper with goal")
    # If the gripper is near the goal and vertically aligned, start moving the
    # gripper into the goal.
    if check("the robot's gripper is near the goal and the robot's gripper is vertically aligned with the goal"):
        robot.move("into goal slowly")
    # If the gripper is inside the goal, let go of the puck.
    if check("the robot's gripper is inside the goal"):
        robot.let_go("of the puck")