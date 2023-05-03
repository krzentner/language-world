

Then add the steps needed to complete the task:

# handle-press-side: push down the handle from the side
def handle_press_side(robot):
    # Steps:
    #  1. Put gripper near handle and horizontally aligned with the handle 
    #  2. Push down on the handle from the side
    # First, put the gripper near the handle and horizontally aligned with the handle.
    if check("the robot's gripper is not horizontally aligned with the handle"):
        robot.move_gripper("horizontally aligned with the handle")
    # Once the gripper is lined up, we can just push down on the handle.
    if check("the robot's gripper is horizontally aligned with the handle"):
        robot.move_gripper("near the handle")