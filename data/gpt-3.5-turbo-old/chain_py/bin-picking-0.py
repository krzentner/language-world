# Steps:
#  1. Use computer vision to locate the cube
#  2. Move the gripper above the cube
#  3. Grab the cube with the gripper
#  4. Move the gripper to the target bin
#  5. Release the cube into the bin
# We need to use computer vision to locate the cube before we can pick it up.
# Once we locate the cube, we need to move the gripper above it and grab it.
# After grabbing the cube, we need to move the gripper to the target bin and
# release the cube into it.

def bin_picking(robot):
    # Use computer vision to locate the cube
    cube_location = robot.find("cube")
    
    # Move the gripper above the cube
    if check("the robot's gripper is not above the cube"):
        robot.move("gripper to cube", cube_location)
    
    # Grab the cube with the gripper
    if check("the robot's gripper is above the cube and the gripper is open"):
        robot.grab("cube")
    
    # Move the gripper to the target bin
    bin_location = robot.find("bin")
    if check("the robot's gripper is holding the cube and is not above the target bin"):
        robot.move("gripper to bin", bin_location)
    
    # Release the cube into the bin
    if check("the robot's gripper is above the target bin and is holding the cube"):
        robot.release("cube into the bin")