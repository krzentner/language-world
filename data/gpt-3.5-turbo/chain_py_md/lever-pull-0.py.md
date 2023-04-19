# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    # 1. Move the gripper to the center of the lever.
    # 2. Grab the lever.
    # 3. Pull the lever up.
    # 4. Release the lever.
    
    # First, we need to check if the gripper is not above the center of the lever.
    # If the gripper is not above the center of the lever, we need to move it there.
    if check("the robot's gripper is not above the center of the lever"):
        robot.move("gripper to the center of the lever")
        
    # If the gripper is above the center of the lever, we can grab it.
    if check("the robot's gripper is above the center of the lever and the robot's gripper is open"):
        robot.drop("gripper around the center of the lever")
        
    # Once we have secure grip on the lever, we can start pulling it up.
    if check("the robot's gripper is around the center of the lever and the lever is not in upright position"):
        robot.pull("the lever up")
        
    # Once the lever is in upright position, we need to release the lever.
    if check("the lever is in upright position and the robot's gripper is closed"):
         robot.release("the lever")