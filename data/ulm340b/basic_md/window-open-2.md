


"""


def test_tutorial():
    tutorial = "tutorial.txt"
    with open(tutorial) as f:
        text = f.read()

    assert all(a in text for a in (
        "When the robot's gripper is not near reach target, the robot should reach to goal.",
        "When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.",
        "When the robot's gripper is vertically aligned with button, the robot should push down on button.",
        "When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.",
        "When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.",
        "When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.",
        "When peg is horizontally aligned with hole, the robot should insert peg into hole.",
        "When the robot's gripper is not near the drawer handle, the robot should grab drawer handle.",
        "When the robot's gripper is forward aligned with drawer handle, the robot should push drawer closed.",
        "When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.",
        "When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.",
        "When the robot's gripper is around drawer handle, the robot should pull away from drawer.",
        "When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.",
        "When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.",
        "When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.",
        "When the robot's gripper is not above the puck, the robot should place gripper above puck.",
        "When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.",
        "When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.",
        "When the robot's gripper is above puck and the robot's