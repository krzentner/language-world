

You can submit your code with the button below.
'''

def button_press_topdown_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

if __name__ == "__main__":
    import sys

    print(f"Running on python version: {sys.version}")

    mturk_agent_id = os.environ.get("MTURK_AGENT_ID")
    if mturk_agent_id is None:
        url = "http://localhost:8080"
        print(f"Starting a local server at {url}...")
        server = MTurkServer(url)
    else:
        print(f"Submitting to MTurk server with agent id {mturk_agent_id}")
        server = MTurkConnection(mturk_agent_id, "https://mturk-requester-sandbox.us-east-1.amazonaws.com", "ap-northeast-1")

    print("Connecting to server...")
    if not server.setup():
        raise Exception("Could not connect to mturk server!")

    task_description = '''Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

Here's some code that demonstrates how the robot can do a variety of tasks:

```
# window-close: slide the window closed to the right
def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window