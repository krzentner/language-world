

Steps:
1. Reach the robot's gripper to the side of the hole 
2. Line up the gripper with the peg and slightly above it
3. Drop the gripper around the peg
4. Close the gripper around the peg
5. Move the peg to the goal location 

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Reach the robot's gripper to the side of the hole 
    #  2. Line up the gripper with the peg and slightly above it
    #  3. Drop the gripper around the peg
    #  4. Close the gripper around the peg
    #  5. Move the peg to the goal location 
    
    # Reach the robot's gripper to the side of the hole 
    if check("the robot's gripper is not near the hole"):
        robot.reach("to hole")
    # Line up the gripper with the peg and slightly above it
    if check("the robot's gripper is near the hole and the robot's gripper is not vertically aligned with peg and the robot's gripper is above the peg"):
        robot.put("gripper at peg")
    # Drop the gripper around the peg
    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is open"):
        robot.drop("gripper around peg")
    # Close the gripper around the peg
    if check("the robot's gripper is ready to pick peg"):
        robot.close("gripper around peg")
    # Move the peg to the goal location 
    if check("the robot's gripper is above peg and the robot's gripper is closed"):
        robot.place("peg at goal")