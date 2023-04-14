import re
from textwrap import indent, dedent
import json
from typing import Dict, List, Optional, Tuple
import os

import generate_metaworld_scene_dataset
from generate_metaworld_scene_dataset import eval_conditions

from sample_utils import MT10_ENV_NAMES, MT50_ENV_NAMES


def load_plan_file(
    filename: str, encoding: Optional[str] = None
) -> Dict[str, List[Tuple[str, str]]]:
    if encoding is None:
        _, encoding = filename.rsplit(".", maxsplit=1)
    with open(filename, "r") as f:
        contents = f.read()
    return decode_plans(contents, encoding)


def decode_plans(contents: str, encoding: str) -> Dict[str, List[Tuple[str, str]]]:
    if encoding in ("py", "naive-py-if"):
        return decode_plans_py(contents)
    elif encoding in ("json"):
        return json.loads(contents)
    else:
        raise ValueError(f"Uknown encoding {encoding!r}")


def encode_plans(plans: Dict[str, List[Tuple[str, str]]], encoding: str) -> str:
    if encoding in ("py", "naive-py-if"):
        return encode_plans_py(plans)
    elif encoding in ("json"):
        return json.dumps(plans, indent=True)
    else:
        raise ValueError(f"Uknown encoding {encoding!r}")


def decode_plans_py(contents: str) -> Dict[str, List[Tuple[str, str]]]:
    without_comments = []
    for line in contents.split("\n"):
        if "#" in line:
            without_comments.append(line.split("#")[0])
        else:
            without_comments.append(line)
    contents = "\n".join(without_comments)
    plans_parsed = {}
    for plan in contents.split("\n\n"):
        names = FN_NAME.findall(plan)
        if names:
            clause_map = []
            for (cond, action) in CLAUSES.findall(plan):
                verb_details = VERB_DETAILS.findall(action)
                if verb_details and verb_details[0][0] != "move_gripper":
                    clause_map.append((cond, " ".join(verb_details[0])))
                close_gripper = CLOSE_GRIPPER.findall(action)
                if close_gripper:
                    loc = preprocess_location(close_gripper[0])
                    clause_map.append(
                        (cond, f"{loc} and the robot's gripper is closed")
                    )
                open_gripper = OPEN_GRIPPER.findall(action)
                if open_gripper:
                    loc = preprocess_location(open_gripper[0])
                    clause_map.append((cond, f"{loc} and the robot's gripper is open"))
                    clause_map.append(
                        (
                            cond,
                            f"the robot's gripper is {loc}"
                            " and the robot's gripper is open",
                        )
                    )
                move_gripper = MOVE_GRIPPER.findall(action)
                if move_gripper:
                    clause_map.append((cond, preprocess_location(move_gripper[0])))
            plans_parsed[names[0].replace("_", "-")] = clause_map
    return plans_parsed


def encode_plan_json(plan: Dict[str, List[Tuple[str, str]]]) -> str:
    return json.dumps(plan, indent=True)


def preprocess_location(action: str) -> str:
    locs = action.split(" and ")
    goals = []
    for loc in locs:
        found_relation = False
        if "touching " in loc:
            found_relation = True
        for rel in generate_metaworld_scene_dataset.COORDINATE_RELATIONS:
            if found_relation:
                break
            if f"{rel} " in loc:
                found_relation = True
        if not found_relation:
            goals.append(f"the robot's gripper is near {loc}")
        else:
            goals.append(f"the robot's gripper is {loc}")
    return " and ".join(goals)

def wrap_in_markdown(contents, task):
    return dedent("""
        Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

        Here's some code that demonstrates how the robot can do a variety of tasks:

        ```
        {contents}
        ```

        Please write a program to do the last task, `{task}`.
        """).format(contents=contents, task=task)


FN_NAME = re.compile(r"def ([a-zA-Z_]+)\(")
CLAUSES = re.compile(r'if check\("([^"]+)"\):\s+([^\n]+)', flags=re.MULTILINE)
VERB_DETAILS = re.compile(r'robot.([a-zA-Z_]+)\("([^"]+)"\)')
MOVE_GRIPPER = re.compile(f'robot.move_gripper\("([^"]+)"\)')
CLOSE_GRIPPER = re.compile(f'robot.move_gripper\("([^"]+)", close_gripper=True\)')
OPEN_GRIPPER = re.compile(f'robot.move_gripper\("([^"]+)", open_gripper=True\)')

def encode_py(env_name, plan, chain_of_thought=False):
    contents = []
    for base_task, steps in plan.items():
        contents.append(plan_str_py(base_task, steps, chain_of_thought=chain_of_thought))
    contents.append(plan_str_py(env_name, []))
    return '\n\n'.join(contents)

def plan_str_py(env_name, steps, chain_of_thought=False):
    header = dedent(
        f"""\
        # {env_name}: {MT50_TASK_DESCRIPTIONS[env_name]}
        # def {env_name.replace('-', '_')}(robot):"""
    )
    clauses = [clause_str(cond, action) for (cond, action) in steps]
    if chain_of_thought:
        new_clauses = [dedent(MT10_STEPS[env_name]).strip()]
        for step_i in range(len(clauses)):
            new_clauses.append(dedent(MT10_STEP_REASONS[env_name][step_i]).strip())
            new_clauses.append(clauses[step_i])
        clauses = new_clauses
    return "\n".join([header] + [indent(clause, " " * 4) for clause in clauses])

def clause_str(cond, action):
    if action.startswith("the robot's gripper is "):
        gripper_state = None
        if action.endswith(" and the robot's gripper is open"):
            gripper_state = "open"
            action = action.split(" and ")[0]
        elif action.endswith(" and the robot's gripper is closed"):
            gripper_state = "close"
            action = action.split(" and ")[0]
        target = action.split("the robot's gripper is ", 1)[1]
        if gripper_state is None:
            return dedent(
                f"""\
                if check("{cond}"):
                    robot.move_gripper("{target}")"""
            )
        elif gripper_state == "open":
            return dedent(
                f"""\
                if check("{cond}"):
                    robot.move_gripper("{target}", open_gripper=True)"""
            )
        elif gripper_state == "close":
            return dedent(
                f"""\
                if check("{cond}"):
                    robot.move_gripper("{target}", close_gripper=True)"""
            )
        else:
            raise AssertionError()
    else:
        return dedent(
            f"""\
            if check("{cond}"):
                robot.{action.split(' ')[0]}("{' '.join(action.split(' ')[1:])}")"""
        )


MT50_TASK_DESCRIPTIONS = {
    "door-open": "open the door",
    "drawer-open": "open the drawer",
    "assembly": "put the wrench around the peg",
    "basketball": "put the ball into into the hoop",
    "button-press-topdown": "push the button down from above",
    "button-press-topdown-wall": "push the button down from above with a short wall in the way",
    "button-press": "push the button from the front",
    "button-press-wall": "push the button from the front with a short wall in the way",
    "coffee-button": "push the button on the coffee machine",
    "coffee-pull": "grab the mug and pull it to the target location",
    "coffee-push": "grab the mug and move it to the target location",
    "bin-picking": "pick up the cube and place it in the target bin",
    "dial-turn": "turn the dial",
    "disassemble": "pull the wrench off the peg",
    "door-open": "pull the door open",
    "drawer-close": "push the drawer close",
    "drawer-open": "pull the drawer open",
    "faucet-open": "turn the faucet left",
    "faucet-close": "turn the faucet right",
    "hammer": "hit the nail with the hammer",
    "box-close": "pick up the box lid and place it on the box",
    "handle-press-side": "push down the handle from the side",
    "handle-press": "push down the handle",
    "handle-pull-side": "pull up the handle from the side",
    "handle-pull": "pull up the handle",
    "lever-pull": "rotate the lever up",
    "peg-insert-side": "insert the peg into the hole from the side",
    "peg-unplug-side": "pull the peg out from the side",
    "pick-out-of-hole": "pick up the peg out of the hole and hold it at the target location",
    "pick-place": "pick up the puck and hold it at the target location",
    "door-lock": "turn the dial on the door",
    "pick-place-wall": "pick up the puck and hold it at the target location with a short wall in the way",
    "plate-slide": "slide the plate into the target location",
    "plate-slide-side": "slide the plate sideways into the target location",
    "plate-slide-back": "slide the plate back into the target location",
    "plate-slide-back-side": "slide the plate back sideways into the target location",
    "push-back": "slide the puck backwards to the target location",
    "push": "slide the puck to the target location",
    "push-wall": "slide the puck to the target location with a small wall in the way",
    "reach": "reach to the target location",
    "door-unlock": "turn the dial on the door",
    "reach-wall": "reach to the target location with a short wall in the way",
    "shelf-place": "pick up the block and place it at the target location",
    "soccer": "push the soccer ball into the target location",
    "stick-push": "use the stick to push the thermos to the target location",
    "stick-pull": "use the stick to pull the thermos to the target location",
    "sweep-into": "grab the cube and move it to the target location",
    "sweep": "grab the cube and move sideways it to the target location",
    "window-open": "slide the window open to the left",
    "window-close": "slide the window closed to the right",
    "hand-insert": "pick up the puck and move it to the target location",
    "door-close": "push the door closed to the target location",
}

MT10_STEPS = {
    "reach": """
    # Steps:
    #  1. Reach towards the target
    """,
    "push": """
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    """,
    "pick-place": """
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    """,
    "door-open": """
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    """,
    "drawer-open": """
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    """,
    "drawer-close": """
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    """,
    "button-press-topdown": """
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    """,
    "peg-insert-side": """
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    """,
    "window-open": """
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    """,
    "window-close": """
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    """,
}

MT10_STEP_REASONS: dict[str, list[str]] = {
    "reach": ['''
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    ''',],
    "push": ['''
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    ''',
             '''
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    ''',
             '''
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    '''],
    "pick-place": [
        '''
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    ''',
        '''
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    ''',
        '''
    # We closed the gripper, and the puck is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the puck to the goal.
    # If we didn't grab it, we'll just go back to an earlier step.
    '''
    ],
    'door-open': [
        '''
    # First, put the gripper mostly above the door handle.
    ''',
        '''
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    ''',
        '''
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    ''',
    ],
    "drawer-open": [
        '''
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    ''',
        '''
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    ''',
        '''
    # Once the gripper is around the drawer handle, we can just pull the drawer
    # open.
    '''
    ],
    'drawer-close': [
        '''
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
        ''',
        '''
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
        '''
    ],
    'button-press-topdown': [
        '''
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    ''',
        '''
    # Now that the gripper is lined up, just push down on the button.
        '''
    ],
    'peg-insert-side': [
        '''
    # First, put the gripper above the peg.
    ''',
        '''
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    ''',
        '''
    # As long the gripper is still mostly around the peg and the peg isn't lined
    # up with the hole, line up the peg with the hole.
    ''',
        '''
    # If the peg is lined up with the hole to the side, insert it.
    ''',
    ],
    'window-open': [
        '''
    # If the robot's gripper is not vertically lined up with the window handle,
    # we should move the gripper near the window handle to start pushing
    ''',
        '''
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    ''',
        '''
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    '''
    ],
    'window-close': [
        '''
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    ''',
        '''
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    ''',
        '''
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    ''',
    ]
}


def save(plan_str: str, filename: str):
    assert '\n' not in filename
    if '/' in filename:
        os.makedirs(filename.rsplit('/', maxsplit=1)[0], exist_ok=True)
    with open(filename, 'w') as f:
        f.write(plan_str)


def convert(filename: str, *, encoding: str = "guess", out_encoding: str = "json", out_file: str):
    if encoding == "guess":
        plans = load_plan_file(filename)
    else:
        plans = load_plan_file(filename, encoding)
    encoded = encode_plans(plans, encoding=out_encoding)
    print(encoded)
    if out_file is not None:
        save(encoded, out_file)

def generate_all_plans():
    mt10_basic = load_plan_file('plans/mt10_basic.json')
    mt10_goal = load_plan_file('plans/mt10_goal.json')
    for task in MT50_ENV_NAMES:
        basic_py = encode_py(task, mt10_basic)
        save(basic_py, f'data/basic_py/{task}.py')
        chain_py = encode_py(task, mt10_goal, chain_of_thought=True)
        save(chain_py, f'data/chain_py/{task}.py')
        goal_py = encode_py(task, mt10_goal, chain_of_thought=True)
        save(goal_py, f'data/goal_py/{task}.py')
        save(wrap_in_markdown(basic_py, task), f'data/basic_py_md/{task}.py.md')
        save(wrap_in_markdown(chain_py, task), f'data/chain_py_md/{task}.py.md')
        save(wrap_in_markdown(goal_py, task), f'data/goal_py_md/{task}.py.md')


if __name__ == "__main__":
    import clize

    clize.run(convert, generate_all_plans)
