# hand-insert: pick up the puck and move it to the target location
# def hand_insert(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to the target location
    # This task is similar to 'pick-place', but we don't need to align the puck
    # with any particular object, only move it to a target location afterwards.
    
    # First, put the gripper roughly above the puck
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    
    # If the gripper is not around the puck, move it into position
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    
    # Once the gripper is around the puck, grab it by closing the gripper
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.move_gripper("above the target location", open_gripper=True)
    
    # Once we're above the target location, drop the puck
    if check("the robot's gripper is above the target location and the robot's gripper is open"):
        robot.move_gripper("above the target location", close_gripper=True)