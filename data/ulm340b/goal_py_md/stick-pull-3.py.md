

(If you don't finish your code by the time you are asked to stop, you can continue working on it after the other part of the study is finished.)
"""

###########################################################
# Start writing code here:
###########################################################
def stick_pull(robot):
    # Steps:
    #  1. Move the gripper to the target location of the stick.
    if check("the robot's gripper is not near the stick and the robot's gripper is not near the goal location of the stick"):
        robot.move_gripper("near the stick", close_gripper=True)
    if check("the robot's gripper is not above the stick and the robot's gripper is not above the goal location of the stick"):
        robot.move_gripper("above the stick", close_gripper=True)
    #  2. Move the gripper to above the target location of the stick.
    if check("the robot's gripper is above the stick and the robot's gripper is not above the goal location of the stick"):
        robot.move_gripper("above the goal location of the stick", close_gripper=True)
    #  3. Grab the stick using the gripper.
    if check("the robot's gripper is above the goal location of the stick and the stick is not in the robot's gripper"):
        robot.move_gripper("in the robot's gripper", close_gripper=True)
    #  4. Move the gripper to the target location of the thermos.
    if check("the stick is in the robot's gripper and the robot's gripper is not near the thermos and the robot's gripper is not near the goal location of the thermos"):
        robot.move_gripper("near the thermos", close_gripper=True)
    if check("the stick is in the robot's gripper and the robot's gripper is not above the thermos and the robot's gripper is not above the goal location of the thermos"):
        robot.move_gripper("above the thermos", close_gripper=True)
    #  5. Move the gripper to the target location of the thermos.
    if check("the stick is in the robot's gripper and the robot's gripper is above the thermos and the robot's gripper is not above the goal location of the thermos"):
       