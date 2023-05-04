
    You have two options:
        1. I'm not sure
        2. Push the plate to the right, starting near the middle
        3. Reach towards the right side of the plate to push the plate into the goal
    Which one do you think is better?
"""


def get_demonstration(condition, task_id):
    demonstrations = [
        ("window-close", [
            "When the robot's gripper is in front of the window handle, move the robot's gripper until the robot's gripper is right of the window handle",
            "When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the window handle",
            "When the robot's gripper is near the window handle, move the robot's gripper until the robot's gripper is forward aligned with the window handle"]),
        ("window-open", [
            "When the robot's gripper is near the window handle, move the robot's gripper until the robot's gripper is forward aligned with the window handle",
            "When the robot's gripper is in front of the window handle, move the robot's gripper until the robot's gripper is vertically aligned with the window handle"]),
        ("reach", ["When the robot's gripper is not near reach target, move the robot's gripper until the robot's gripper is near the reach target"]),
        ("peg-insert-side", [
            "When the robot's gripper is not vertically aligned with the peg, move the robot's gripper until the robot's gripper is vertically aligned with the peg",
            "When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, move the robot's gripper until the robot's gripper is forward aligned with the peg and the robot's gripper is closed",
            "When peg is horizontally aligned with hole, move the robot's gripper until the robot's gripper is above the peg",
            "When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, move the robot's gripper until the robot's gripper is horizontally aligned with hole"]),
        ("door-open", [
            "When the robot's gripper is not almost vertically aligned with door handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is closed",
            