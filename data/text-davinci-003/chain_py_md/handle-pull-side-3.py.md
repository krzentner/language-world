

Steps:
1. Put gripper above the handle 
2. Drop gripper around the handle 
3. Pull handle upwards 

# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop gripper around the handle
    #  3. Pull handle upwards
    if check("the robot's gripper is not above the handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.drop("gripper around handle")
    if check("the robot's gripper is around the handle"):
        robot.pull("handle upwards")