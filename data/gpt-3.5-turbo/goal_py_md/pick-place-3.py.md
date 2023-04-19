# pick-place: pick up the object and hold it at the target location
def pick_place(robot, object_location, target_location):
    # Steps:
    #  1. Move gripper above object
    #  2. Move gripper around object and close gripper to pick it up
    #  3. Move gripper to target location and open gripper to place object
    
    # First, put the gripper roughly above the object, so that we don't bump into it
    if check(f"the robot's gripper is not above {object_location}"):
        robot.move_gripper(f"above {object_location}")
    # If the gripper isn't around the object, put it around the object
    if check(f"the robot's gripper is not around {object_location} and the robot's gripper is open"):
        robot.move_gripper(f"near {object_location}", close_gripper=True)
    # If the gripper is around the object and closed, move it to the target location
    if check(f"the robot's gripper is around {object_location} and the robot's gripper is closed and the robot's gripper is not above {target_location}"):
        robot.move_gripper(f"above {target_location}")
    # If the gripper is above the target location, open the gripper to release the object
    if check(f"the robot's gripper is above {target_location} and the robot's gripper is closed"):
        robot.move_gripper(f"near {target_location}", close_gripper=False)