

The robot can pull up the handle from the side in a few steps:

1. Put gripper above the handle 
2. Line up the gripper as viewed from the side
3. Pull up on the handle

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Line up gripper as viewed from the side
    #  3. Pull up on handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # As long as the gripper isn't lined up with the handle from the side, keep
    # moving the gripper down until it is lined up.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.put("gripper alongside handle")
    # Now that the gripper is lined up, we can pull up on the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.pull("up on handle")