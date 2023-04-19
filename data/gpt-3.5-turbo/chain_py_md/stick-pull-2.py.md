# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    # 1. Put the gripper roughly above the stick
    # 2. Open the gripper and grab the stick
    # 3. Move the gripper and stick to the thermos
    # 4. Put the gripper above the thermos
    # 5. Use the stick to hook onto the thermos handle
    # 6. Pull the thermos towards the target location
    
    # First, position the gripper above the stick.
    if check("the robot's gripper is not above the stick"):
        robot.place("gripper above stick")
    
    # Open the gripper and grab the stick.
    if check("the robot's gripper is above the stick and the robot's gripper is closed"):
        robot.open("gripper")
        robot.grab("stick")
        
    # Move the gripper and stick to the thermos.
    if check("robot's gripper and stick are not near the thermos"):
        robot.reach("gripper and stick near thermos")
    
    # Put the gripper above the thermos.
    if check("the gripper is not above the thermos"):
        robot.place("gripper above thermos")
    
    # Use the stick to hook onto the thermos handle.
    if check("the stick is not hooked onto the thermos handle"):
        robot.hook("the thermos handle with the stick")
    
    # Pull the thermos towards the target location.
    if check("the thermos is not at the target location"):
        robot.pull("the thermos towards the target location")