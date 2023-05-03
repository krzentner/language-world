# hand-insert: pick up the puck and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Open gripper around puck
    #  3. Move gripper and puck to the target location
    #  4. Close gripper around the puck
    # This task is similar to pick-place, but instead of placing the puck at the
    # target location, we just need to move it there.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above the puck")
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.drop("gripper around the puck")
    # Once the gripper is around the puck, move the gripper and puck to the
    # target location.
    if check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
        robot.move("gripper and puck to target location")
    # Once we're at the target location, close the gripper to firmly hold the
    # puck.
    if check("the robot's gripper is near the target and the puck is below the robot's gripper"):
        robot.close("gripper around the puck")