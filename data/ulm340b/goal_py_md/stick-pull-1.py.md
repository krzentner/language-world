

When your code is complete, you can check if it is correct by running
`python check_task.py`, which will verify your code, along with several
test tasks, each in a separate process.
*/

# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Put stick around handle of the thermos
    #  4. Pull stick to bring thermos to target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with stick"):
        robot.move_gripper("vertically aligned with stick")
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is vertically aligned with stick and the robot's gripper is closed"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the gripper isn't around the stick, put it around the stick.
    if check("the robot's gripper is not around stick and the robot's gripper is open"):
        robot.move_gripper("near the stick", close_gripper=True)
    # If the gripper is near the stick and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is vertically aligned with stick and the robot's gripper is closed"):
        robot.move_gripper("around the stick", close_gripper=True)
    # If the robot's gripper is around the stick, and the stick is not around
    # the handle of the thermos, move the stick near the thermos.
    if check("the robot's gripper is around the stick and the stick is not around handle of the thermos"):
        robot.move_gripper("near handle of the thermos")
    # If the robot's grip