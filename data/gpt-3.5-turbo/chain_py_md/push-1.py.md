# push: slide the puck to the target location
def push(robot):
    # Steps:
    # 1. Put gripper above the puck
    # 2. Drop gripper around the puck
    # 3. Close the gripper around the puck
    # 4. Slide the puck to the target location
    # 5. Open the gripper
    
    # First, put the gripper above the puck
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    
    # Next, put the gripper around the puck
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    
    # Close the gripper around the puck
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    
    # Slide the puck to the target location
    if check("the robot's gripper is closed and the puck is not at the target location"):
        robot.slide("puck to goal")
    
    # Open the gripper
    if check("the robot's gripper is closed and the puck is at the target location"):
        robot.lift("gripper up")
        robot.move("gripper to home position")
        robot.release("gripper")