mt10_instruction_map = {
    "close_drawer": {
        "the robot's gripper is above the drawer handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down into the drawer handle",
        },
        "the robot's gripper is around the drawer handle": {
            "controller_coeff": 10.0,
            "grip_effort": 1.0,
            "target": "",
        },
        "the robot's gripper is not near the drawer handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the drawer handle",
        },
    },
    "insert_peg_right_into_slot": {
        "the robot is holding a peg": {
            "controller_coeff": 50.0,
            "grip_effort": 0.0,
            "target": "right into the slot",
        },
        "the robot's gripper is above the peg": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down into the peg",
        },
        "the robot's gripper is around the peg": {
            "controller_coeff": 10.0,
            "grip_effort": 1.0,
            "target": "",
        },
        "the robot's gripper is not near the peg": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the peg",
        },
    },
    "open_door": {
        "the robot's gripper is above the door handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down into the door handle",
        },
        "the robot's gripper is around the door handle": {
            "controller_coeff": 10.0,
            "grip_effort": 1.0,
            "target": "",
        },
        "the robot's gripper is not near the door handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the door handle",
        },
    },
    "open_drawer": {
        "the robot's gripper is above the drawer handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down into the drawer handle",
        },
        "the robot's gripper is around the drawer handle": {
            "controller_coeff": 10.0,
            "grip_effort": 1.0,
            "target": "",
        },
        "the robot's gripper is not near the drawer handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the drawer handle",
        },
    },
    "pick_puck_and_hold_at_target": {
        "the robot is holding a puck": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "forward to the target",
        },
        "the robot's gripper is above the puck": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down into the puck",
        },
        "the robot's gripper is around the puck": {
            "controller_coeff": 10.0,
            "grip_effort": 1.0,
            "target": "",
        },
        "the robot's gripper is not near the puck": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the puck",
        },
    },
    "press_button_from_above": {
        "the robot's gripper is above the button": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down onto the button",
        },
        "the robot's gripper is not near the button": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the button",
        },
    },
    "slide_puck_to_target": {
        "the robot is holding a puck": {
            "controller_coeff": 50.0,
            "grip_effort": 0.0,
            "target": "forward to the target",
        },
        "the robot's gripper is above the puck": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "down into the puck",
        },
        "the robot's gripper is around the puck": {
            "controller_coeff": 10.0,
            "grip_effort": 1.0,
            "target": "",
        },
        "the robot's gripper is not near the puck": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "up above the puck",
        },
    },
    "slide_window_closed_right": {
        "the robot's gripper is left of the window handle": {
            "controller_coeff": 50.0,
            "grip_effort": 0.0,
            "target": "right to edge of window",
        },
        "the robot's gripper is not left of the window handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "left of the window handle",
        },
    },
    "slide_window_open_left": {
        "the robot's gripper is not right of the window handle": {
            "controller_coeff": 10.0,
            "grip_effort": 0.0,
            "target": "right of the window handle",
        },
        "the robot's gripper is right of the window handle": {
            "controller_coeff": 50.0,
            "grip_effort": 0.0,
            "target": "left to edge of window",
        },
    },
}
