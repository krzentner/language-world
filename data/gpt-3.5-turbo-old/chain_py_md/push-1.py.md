# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    
    # Check if the gripper is not above the puck and not vertically aligned with the puck
    if check("the robot's gripper is not above the puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("gripper above the puck")
        
    # Check if the gripper is above the puck but not around it
    if check("the robot's gripper is above the puck and the robot's gripper is not around the puck"):
        robot.push("gripper into the puck")
        
    # Check if the gripper is around the puck and the puck is below the gripper
    if check("the robot's gripper is around the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")