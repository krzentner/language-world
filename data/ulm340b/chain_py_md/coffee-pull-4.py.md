

I recommend beginning with "Step 1. Put gripper above mug".
You can use code snippets to fill in the details.

(To make a code snippet, drag the mouse over the code that you want to use
as a snippet, and click the plus (+) icon in the code window.)

Good luck!
    
    """
    import sys
    
    args = sys.argv
    
    def get_task_name(args):
        return args[2].split("_")[0]
    
    
    def get_task_name_with_description(args):
        print (args[2])
        return args[2].split("_")[0]+"_"+args[2].split("_")[1]
    
    
    task_name = args[2].split("_")[0]
    if task_name == "coffee":
        return """
        
# coffee-pull: grab the mug and pull it to the target location
def coffee_pull(robot):
    # Step 1. Put gripper above mug
    # This is because the mug is a bit small to grab from the side.
    # So we'll pick it up from above.
    if check("the robot's gripper is not vertically aligned with mug"):
        robot.put("gripper above mug")
    # Step 2. Grab the mug with the gripper
    # Now that the gripper is lined up, close it to grab the mug.
    if check("the robot's gripper is vertically aligned with mug and the robot's gripper is open"):
        robot.grab("mug")
    # Step 3. Move the mug to the goal location
    # If the gripper is above the mug, it's probably above the goal, so pull the
    # mug to the goal.
    if check("the robot's gripper is above mug"):
        robot.move("mug to goal")
        
        """
        
    elif task_name == "open":
        return """
        
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle