# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Align the stick with the thermos handle
    #  4. Slide the stick under the thermos handle
    #  5. Use the stick to pull the thermos to the goal
    # First, put the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    # Once the gripper is above the stick, we need to grab it.
    if check("the robot's gripper is near stick and the robot's gripper is open"):
        robot.close("gripper around stick") 
    # The stick should now be grabbed by the gripper.
    # Next, we need to align the stick with the handle of the thermos.
    if check("the robot's gripper is holding the stick and the stick is not lined up with the thermos handle"):
        robot.align("stick with thermos handle")
    # The stick should now be lined up with the thermos handle. We can slide the stick under the thermos handle.
    if check("the stick is aligned with the thermos handle and not under the handle"):
        robot.slide("stick under the thermos handle")
    # We should now be able to use the stick to pull the thermos to the goal.
    if check("the stick is under the thermos handle and the thermos is not at the goal"):
        robot.pull("thermos to goal using stick")