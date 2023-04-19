

Steps: 
1. Put gripper in front of the dial
2. Slowly rotate the dial in one direction
3. Switch direction and slowly rotate in the opposite direction
4. Repeat steps 2 and 3 until the door unlocks

if check("the robot's gripper is not forward aligned with dial"):
  robot.move_gripper("forward aligned with dial")

initial_direction = "clockwise"
while(not check("the door is unlocked")):
  robot.rotate_gripper(initial_direction)
  initial_direction = "counter-clockwise" if initial_direction == "clockwise" else "clockwise"