
    - When the robot's gripper is not aligned with the nail, the robot should move gripper to above nail.
    - When the robot's gripper is near the nail and the hammer is not near the nail, the robot should drop gripper on nail.
    - When the robot's gripper is on the nail, the robot should lift gripper with nail.
    - When the robot's gripper is around the nail, the robot should move gripper to near hammer.
    - When the hammer is below the robot's gripper and the nail is not above the hammer, the robot should lower gripper to hammer.
    - When the hammer is above the robot's gripper, the robot should release gripper and nail.

The task `door-lock` requires the robot to grab the door handle, insert the key into the keyhole, and lock the door by turning the key.
To grab the door handle, insert the key into the keyhole, and lock the door by turning the key reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with the door handle, the robot should move gripper to above door handle.
    - When the robot's gripper is vertically aligned with the door handle and the robot's gripper is not near the door handle, the robot should put gripper around door handle.
    - When the robot's gripper is around the door handle and the key is not near the keyhole, the robot should move gripper with door handle to keyhole.
    - When the key is near the keyhole and the key is not inserted into the keyhole, the robot should insert key into keyhole.
    - When the key is inserted into the keyhole, the robot should turn key in keyhole.

"""


def _get_instructions_as_text():
    text = [
        _get_instructions_top_down(),
        _get_instructions_bottom_up(),
    ]
    for task in [
        "button-press-topdown",
        "door-open",
        "reach",
        "drawer-close",
        "drawer-open",
        "peg-insert-side",
        "pick-place",
        "push",
        "window-close",
        "window-open",
        "hammer",
        "door-lock",
    ]:
        for line in INSTRUCTIONS[task]:
            line = line.replace(" ", "\n")
            line = "    - " + line + "\n"
            text.append(line)
        text.append("\n")
    return "\n".join(text)


