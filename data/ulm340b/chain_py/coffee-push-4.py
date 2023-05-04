
    # Steps:
    #  1. Put gripper around mug
    #  2. Slide mug to goal
    # Put the gripper around the mug
    if check("the robot's gripper is not around coffee mug and the robot's gripper is open"):
        robot.grab("coffee mug")
    # If we think we grabbed the mug, slide it to the goal
    if check("the robot's gripper is around coffee mug"):
        robot.push("coffee mug to goal")

# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Steps:
    #  1. Put gripper around mug
    #  2. Slide mug to goal
    # Put the gripper around the mug
    if check("the robot's gripper is not around coffee mug and the robot's gripper is open"):
        robot.grab("coffee mug")
    # If we think we grabbed the mug, pull it to the goal
    if check("the robot's gripper is around coffee mug"):
        robot.pull("coffee mug to goal")

# coffee-pick-place: grab the mug and move it to the target location
def coffee_pick_place(robot):
    # Steps:
    #  1. Put gripper above the mug
    #  2. Close the gripper around the mug
    #  3. Lift mug up
    #  4. Slide mug over to goal
    # Put the gripper above the mug
    if check("the robot's gripper is not above the mug and the robot's gripper is open"):
        robot.place("gripper above the mug")
    # If we think we grabbed the mug, slide it to the goal
    if check("the robot's gripper is around coffee mug"):
        robot.push("coffee mug to goal")

# coffee-wall-push: move the mug to the wall and push it
def coffee_wall_push(robot):
    # Steps:
    #  1. Move gripper to the right, along the wall
    #  2. Push the mug towards the wall
    #  3. Slide the mug along the wall to the goal
    if check("the mug is to the right of the robot's gripper"):
        robot.move("gripper