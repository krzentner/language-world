from functools import partial
import typing

import numpy as np

# import jax
# import jax.numpy as np

from metaworld_scripted_skills import parse_obs
from sample_utils import MT50_ENV_NAMES, str_project


class FixedDict(dict):
    def __setitem__(self, key, value):
        assert key in self, f"{key} not present in dict"
        return super().__setitem__(key, value)


COORDINATE_RELATIONS = [
    "near",
    "around",
    "left of",
    "right of",
    "behind",
    "in front of",
    "above",
    "below",
    "vertically aligned with",
    "almost vertically aligned with",
    "mostly below",
    "horizontally aligned with",
    "forward aligned with",
]


OBJECT_NAMES = {
    "drawer-open": {
        "obj1_pos": "drawer handle",
    },
    "drawer-close": {
        "obj1_pos": "drawer handle",
    },
    "peg-insert-side": {
        "obj1_pos": "peg",
        # The goal is weirdly offset, so it's hacked in below
    },
    "reach": {"goal_pos": "reach target"},
    "window-open": {
        "obj1_pos": "window handle",
    },
    "window-close": {
        "obj1_pos": "window handle",
    },
    "door-open": {"obj1_pos": "door handle"},
    "push": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "pick-place": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "button-press-topdown": {
        "obj1_pos": "button",
    },
    "sweep": {
        "obj1_pos": "cube",
        "goal_pos": "target location",
    },
    "assembly": {
        "obj1_pos": "wrench",
        "goal_pos": "peg",
    },
    "basketball": {
        "obj1_pos": "ball",
        "goal_pos": "hoop",
    },
    "bin-picking": {
        "obj1_pos": "cube",
    },
    "box-close": {
        "obj1_pos": "lid",
        "goal_pos": "box",
    },
    "button-press-topdown-wall": {
        "obj1_pos": "button",
    },
    "button-press": {
        "obj1_pos": "button",
    },
    "button-press-wall": {
        "obj1_pos": "button",
    },
    "coffee-button": {
        "obj1_pos": "button",
    },
    "coffee-pull": {
        "obj1_pos": "mug",
        "goal_pos": "target location",
    },
    "coffee-push": {
        "obj1_pos": "mug",
        "goal_pos": "target location",
    },
    "dial-turn": {
        "obj1_pos": "dial",
    },
    "disassemble": {
        "obj1_pos": "wrench",
        "goal_pos": "peg",
    },
    "door-close": {
        "obj1_pos": "door",
        "goal_pos": "target location",
    },
    "door-lock": {
        "obj1_pos": "door's lock",
    },
    "door-unlock": {
        "obj1_pos": "door's lock",
    },
    "faucet-close": {
        "obj1_pos": "faucet",
    },
    "faucet-open": {
        "obj1_pos": "faucet",
    },
    "hammer": {
        "obj1_pos": "hammer",
    },
    "hand-insert": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "handle-press-side": {
        "obj1_pos": "handle",
    },
    "handle-press": {
        "obj1_pos": "handle",
    },
    "handle-pull-side": {
        "obj1_pos": "handle",
    },
    "handle-pull": {
        "obj1_pos": "handle",
    },
    "lever-pull": {
        "obj1_pos": "lever",
    },
    "peg-unplug-side": {
        "obj1_pos": "peg",
    },
    "pick-out-of-hole": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "pick-place-wall": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "plate-slide-back-side": {
        "obj1_pos": "plate",
    },
    "plate-slide-back": {
        "obj1_pos": "plate",
    },
    "plate-slide-side": {
        "obj1_pos": "plate",
    },
    "plate-slide": {
        "obj1_pos": "plate",
        "goal_pos": "target location",
    },
    "push-back": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "push-wall": {
        "obj1_pos": "puck",
        "goal_pos": "target location",
    },
    "reach-wall": {
        "goal_pos": "target location",
    },
    "shelf-place": {
        "obj1_pos": "block",
        "goal_pos": "shelf",
    },
    "soccer": {
        "obj1_pos": "ball",
        "goal_pos": "goal",
    },
    "stick-pull": {
        "obj1_pos": "stick",
        "obj2_pos": "thermos",
        "goal_pos": "target location",
    },
    "stick-push": {
        "obj1_pos": "stick",
        "obj2_pos": "thermos",
        "goal_pos": "target location",
    },
    "sweep-into": {
        "obj1_pos": "cube",
        "goal_pos": "target location",
    },
    "sweep": {
        "obj1_pos": "cube",
        "goal_pos": "target location",
    },
}

OBJECT_NAMES_TO_PARSE_NAME = {
    env_name: {v: k for (k, v) in env_map.items()}
    for (env_name, env_map) in OBJECT_NAMES.items()
}

assert len(OBJECT_NAMES) == 50
assert set(OBJECT_NAMES.keys()) == set(MT50_ENV_NAMES)

WALL_ENVS = {
    "reach-wall",
    "pick-place-wall",
    "push-wall",
    "button-press-wall",
    "button-press-topdown-wall",
}

MT50_TASK_DESCRIPTIONS = {
    "door-open": "Open the door",
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
    "push-back": "grab the puck and move it back to the target location",
    "push": "grab the puck and move it to the target location",
    "push-wall": "grab the puck and move it to the target location with a small wall in the way",
    "reach": "reach to the target location",
    "door-unlock": "turn the dial on the door",
    "reach-wall": "reach to the target location with a short wall in the way",
    "shelf-place": "pick up the block and place it at the target location",
    "soccer": "push the soccer ball into the target location",
    "stick-push": "use the stick to push the thermos to the target location",
    "stick-pull": "use the stick to pull the thermos to the target location",
    "sweep-into": "grab the cube and move it to the target location",
    "sweep": "grab the cube and move sideways it to the target location",
    "window-open": "Slide the window open",
    "window-close": "Slide the window closed",
    "hand-insert": "pick up the puck and move it to the target location",
    "door-close": "push the door closed to the target location",
}

assert set(MT50_TASK_DESCRIPTIONS.keys()) == set(MT50_ENV_NAMES)
assert len(MT50_TASK_DESCRIPTIONS) == 50


WALL_HEIGHT = 0.05
WALL_WIDTH = 0.1
WALL_DEPTH = 0.005


def describe_obs(env_name, obs):
    conds = enumerate_descriptors(env_name)
    return dict(zip(conds, eval_conditions(env_name, conds, obs)))


POSITIVE_RELATION_SUBSTR = [f" is {rel} " for rel in COORDINATE_RELATIONS]
NEGATIVE_RELATION_SUBSTR = [f" is not {rel} " for rel in COORDINATE_RELATIONS]

WALL_ENVS = {
    "reach-wall",
    "push-wall",
    "pick-place-wall",
    "button-press-wall",
    "button-press-topdown-wall",
}

# @partial(jax.jit, static_argnames=["env_name", "object_name", "fuzzy"])
def get_object_location(env_name: str, object_name: str, obs, fuzzy: bool = False):
    try:
        parse_name = OBJECT_NAMES_TO_PARSE_NAME[env_name][object_name]
    except KeyError as exc:
        if object_name == "the robot's gripper":
            parse_name = "hand_pos"
        elif object_name.startswith("the "):
            return get_object_location(
                env_name, object_name.split("the ")[1], obs, fuzzy=fuzzy
            )
        elif env_name == "peg-insert-side" and object_name == "hole":
            return np.array([-0.35, obs["goal_pos"][1], 0.16])
        elif env_name in WALL_ENVS and object_name == "wall":
            if (
                env_name == "reach-wall"
                or env_name == "push-wall"
                or env_name == "pick-place-wall"
            ):
                # TODO(zentner): Maybe sure the wall coordinates reflect the center of the
                # wall.
                return np.array([0.1, 0.75, 0.06])
            elif env_name == "button-press-wall":
                return np.array([0.1, 0.6, 0.0])
            elif env_name == "button-press-topdown-wall":
                return np.array([0.1, 0.7, 0.0])
        elif fuzzy:
            object_names = list(OBJECT_NAMES_TO_PARSE_NAME[env_name].keys())
            matches = str_project(object_name, object_names)
            parse_name = OBJECT_NAMES_TO_PARSE_NAME[env_name][matches[0]]
        else:
            raise exc
    # print(f'{object_name!r} (a.k.a. {parse_name!r}) is located at {obs[parse_name]}')
    return obs[parse_name]


# @partial(jax.jit, static_argnames=["rel"])
def eval_relation(rel: str, xyz1: np.ndarray, xyz2: np.ndarray) -> bool:
    assert rel.strip() == rel
    if rel == "near":
        return np.linalg.norm(xyz1 - xyz2) < 0.04
    elif rel == "around":
        return np.linalg.norm(xyz1 - xyz2 + np.array([0, 0, 0.02])) < 0.03
    elif rel == "left of":
        return xyz1[0] - xyz2[0] > 0.04
    elif rel == "right of":
        return xyz1[0] - xyz2[0] < -0.04
    elif rel == "behind":
        return (xyz1[1] - xyz2[1] > 0.04) * (
            np.linalg.norm(np.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.04
        )
    elif rel == "in front of":
        return (xyz1[1] - xyz2[1] < -0.04) * (
            np.linalg.norm(np.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.04
        )
    elif rel == "above":
        return (np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02) * (xyz1[2] - xyz2[2] > 0.0)
    elif rel == "below":
        return (np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.02) * (xyz1[2] - xyz2[2] < 0)
    elif rel == "vertically aligned with":
        return np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.06
    elif rel == "almost vertically aligned with":
        return np.linalg.norm(xyz1[:2] - xyz2[:2]) < 0.12
    elif rel == "mostly below":
        return xyz1[2] < xyz2[2] + 0.23
    elif rel == "horizontally aligned with":
        return np.linalg.norm(xyz1[1:] - xyz2[1:]) < 0.03
    elif rel == "forward aligned with":
        return np.linalg.norm(np.array([xyz1[0] - xyz2[0], xyz1[2] - xyz2[2]])) < 0.03
    else:
        raise TypeError(f"Unknown coordinate relation {rel}")


# @partial(jax.jit, static_argnames=["env_name", "conds"])
def eval_conditions(env_name: str, conds: typing.Tuple[str], obs, fuzzy=False):
    if not isinstance(obs, dict):
        obs = parse_obs(obs)
    results = []
    for full_cond in conds:
        base_conds = full_cond.split(" and ")

        base_results = []
        for cond in base_conds:
            if cond == "the robot's gripper is open":
                base_results.append(obs["gripper_distance_apart"] > 0.75)
            elif cond == "the robot's gripper is closed":
                base_results.append(obs["gripper_distance_apart"] <= 0.75)
            elif cond.endswith(" is not touching the table"):
                object_name = cond.split(" is not touching the table")[0]
                xyz = get_object_location(env_name, object_name, obs, fuzzy)
                base_results.append(xyz[2] > 0.02)
            elif cond.endswith(" is touching the table"):
                object_name = cond.split(" is touching the table")[0]
                xyz = get_object_location(env_name, object_name, obs, fuzzy)
                base_results.append(xyz[2] <= 0.02)
            elif any(substr in cond for substr in NEGATIVE_RELATION_SUBSTR):
                neg_relations = [
                    rel for rel in COORDINATE_RELATIONS if f" is not {rel} " in cond
                ]
                assert len(neg_relations) >= 1
                rel = neg_relations[0]
                obj_name1, obj_name2 = cond.split(f" is not {rel} ")
                xyz1 = get_object_location(env_name, obj_name1, obs, fuzzy)
                xyz2 = get_object_location(env_name, obj_name2, obs, fuzzy)
                base_results.append(1 - eval_relation(rel, xyz1, xyz2))
            elif any(substr in cond for substr in POSITIVE_RELATION_SUBSTR):
                pos_relations = [
                    rel for rel in COORDINATE_RELATIONS if f" is {rel} " in cond
                ]
                assert len(pos_relations) >= 1
                rel = pos_relations[0]
                obj_name1, obj_name2 = cond.split(f" is {rel} ")
                xyz1 = get_object_location(env_name, obj_name1, obs, fuzzy)
                xyz2 = get_object_location(env_name, obj_name2, obs, fuzzy)
                base_results.append(eval_relation(rel, xyz1, xyz2))
            elif fuzzy:
                possible_conditions = enumerate_descriptors(env_name)
                matches = str_project(cond, possible_conditions)
                base_results.append(
                    eval_conditions(env_name, [matches[0]], obs, fuzzy=False)[0]
                )
            else:
                raise TypeError(f"Could not eval condition {cond}")
        results.append(np.all(np.array(base_results)))
    return np.array(results)


def enumerate_base_conds(env_name: str) -> [str]:
    object_names = ["robot's gripper"] + list(OBJECT_NAMES[env_name].values())
    object_names = ["the " + obj_name for obj_name in object_names]
    if env_name == "peg-insert-side":
        object_names.append("hole")
    elif (
        env_name == "reach-wall"
        or env_name == "push-wall"
        or env_name == "pick-place-wall"
        or env_name == "button-press-wall"
        or env_name == "button-press-topdown-wall"
    ):
        object_names.append("wall")
    descriptors = []
    for name1 in object_names:
        for name2 in object_names:
            if name1 == name2:
                continue
            for rel in COORDINATE_RELATIONS:
                if rel == "around" and name1 != "the robot's gripper":
                    continue
                descriptors.append(f"{name1} is {rel} {name2}")
                descriptors.append(f"{name1} is not {rel} {name2}")
    for (key, name) in OBJECT_NAMES[env_name].items():
        if key == "goal_pos":
            continue
        descriptors.append(f"{name} is touching the table")
        descriptors.append(f"{name} is not touching the table")

    descriptors.append("the robot's gripper is open")
    descriptors.append("the robot's gripper is closed")
    return descriptors


def enumerate_descriptors(env_name: str) -> [str]:
    descriptors = enumerate_base_conds(env_name)
    conjunction_descriptors = []
    for desc1 in descriptors:
        for desc2 in descriptors:
            conjunction_descriptors.append(f"{desc1} and {desc2}")
    all_descriptors = descriptors + conjunction_descriptors
    return all_descriptors


enumerate_conditions = enumerate_descriptors


def test_smoke():
    from sample_utils import make_env
    import metaworld_universal_policy
    from tqdm import tqdm

    seed = 100
    PATH_LEN = 10
    with tqdm(total=len(MT50_ENV_NAMES) * PATH_LEN) as pbar:
        for env_name in MT50_ENV_NAMES:
            env = make_env(env_name, seed)
            policy = metaworld_universal_policy.SawyerUniversalV2Policy(
                env_name=env_name
            )
            observation = env.reset()
            for i in range(PATH_LEN):
                action, _ = policy.get_action(observation)
                observation, r, done, info = env.step(action)
                describe_obs(env_name, observation)
                pbar.update(1)


def test_jax():
    from sample_utils import make_env
    import metaworld_universal_policy
    from tqdm import tqdm
    import jax
    import jax.numpy as jnp

    global np
    np = jnp

    eval_conditions_jit = jax.jit(
        eval_conditions, static_argnames=["env_name", "conds"]
    )

    seed = 100
    PATH_LEN = 500
    with tqdm(total=len(MT50_ENV_NAMES) * PATH_LEN) as pbar:
        for env_name in MT50_ENV_NAMES:
            # JIT time grows significantly in number of conds
            # 500 conds takes about ten minutes to JIT
            conds = tuple(enumerate_descriptors(env_name))[:500]
            env = make_env(env_name, seed)
            policy = metaworld_universal_policy.SawyerUniversalV2Policy(
                env_name=env_name
            )
            observation = env.reset()
            for i in range(PATH_LEN):
                action, _ = policy.get_action(observation)
                observation, r, done, info = env.step(action)
                eval_conditions_jit(env_name, conds, observation)
                pbar.update(1)


if __name__ == "__main__":
    # test_smoke()
    test_jax()
