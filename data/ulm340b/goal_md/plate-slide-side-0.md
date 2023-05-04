

The task `plate-slide` requires the robot to slide the plate into the target location.
To slide the plate into the target location reliably, what steps the robot should perform?

"""

def hello():
    print("Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.")
    input("Press Enter to continue:")

def goodbye():
    print("Goodbye.")

def display_task(tasks, task_index):
    """
    Displays the instructions for the given task.
    """
    if task_index >= len(tasks):
        print("No more tasks.")
        return
    print("\n")
    task = tasks[task_index]
    task_name = task["name"]
    print("The task `{0}` requires the robot to {1}.".format(task_name, task["instruction"]))
    print("To {0} reliably, the robot should perform the following steps:".format(task["instruction"]))
    for i in range(len(task["steps"])):
        step_text = task["steps"][i]
        step_action = task["actions"][i]
        print("    {0}".format(step_text))
        print("    {0}".format(step_action))
    print("\n")

def display_help(tasks):
    """
    Displays a summary of the help message.
    """
    print("To push the button down from above reliably, the robot should perform the following steps:")
    print("    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top")
    print("    Because this is \"topdown\", we just need to line up the gripper from above. Line up the robot's gripper from above.")
    print("    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed")
    print("    Now that the gripper is lined up, just push down on the button.")
    print("    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button")
    print("\n")
    print("The task `drawer-open` requires the robot to pull the drawer open.")
    print("To pull the drawer open reliably, the robot should perform the following steps: