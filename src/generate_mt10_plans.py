import os
import pickle
import re
from typing import Union
import optax
from os.path import expanduser
from collections import defaultdict
import shutil
from dataclasses import dataclass
from textwrap import indent, dedent
import clize
from pprint import pprint
import generate_metaworld_scene_dataset
from generate_metaworld_scene_dataset import eval_conditions
from sample_utils import (
    MT10_ENV_NAMES,
    MT50_ENV_NAMES,
    collect_noisy_episodes,
    sample_noisy_policy,
    make_env,
    DEFAULT_SEED,
    evaluate_policy,
)
from flax.training import train_state
import jax_utils
from run_utils import str_list
import metaworld_scripted_skills
from metaworld_scripted_skills import parse_obs, run_scripted_skill
from metaworld_universal_policy import SawyerUniversalV2Policy
import numpy as np
import random
import jax
import jax.numpy as jnp
from tqdm import tqdm
from render_policy import render_policy


MT10_PLANS = {
    "reach": {
        "reach target is mostly below the robot's gripper": "reach to goal",
        "reach target is not right of the robot's gripper": "reach to goal",
    },
    "push": {
        "puck is not below the robot's gripper": "put the gripper above the puck",
        "the robot's gripper is not above puck": "put the gripper above the puck",
        "puck is below the robot's gripper and puck is not near the robot's gripper": "push the gripper into the puck",
        "puck is below the robot's gripper and the robot's gripper is not near puck": "push the gripper into the puck",
        "puck is near the robot's gripper and puck is below the robot's gripper": "slide the puck to the goal",
        "puck is near the robot's gripper and the robot's gripper is above puck": "slide the puck to the goal",
    },
    "pick-place": {
        "puck is not below the robot's gripper": "place gripper above puck",
        "the robot's gripper is not above puck": "place gripper above puck",
        "puck is below the robot's gripper and gripper is open": "drop gripper around puck",
        "the robot's gripper is above puck and gripper is open": "drop gripper around puck",
        "puck is near the robot's gripper and gripper is open": "close gripper around puck",
        "the robot's gripper is near puck and gripper is open": "close gripper around puck",
        "puck is below the robot's gripper and gripper is closed": "place puck at goal",
        "the robot's gripper is above puck and gripper is closed": "place puck at goal",
    },
    "door-open": {
        "door handle is not almost vertically aligned with the robot's gripper": "put gripper above door handle",
        "the robot's gripper is not almost vertically aligned with door handle": "put gripper above door handle",
        "door handle is left of the robot's gripper and gripper is closed": "put gripper around door handle",
        "the robot's gripper is right of door handle and gripper is closed": "put gripper around door handle",
        "door handle is vertically aligned with the robot's gripper and door handle is not left of the robot's gripper": "push door closed",
        "door handle is vertically aligned with the robot's gripper and the robot's gripper is not right of door handle": "push door closed",
    },
    "drawer-open": {
        "drawer handle is not vertically aligned with the robot's gripper": "put gripper above drawer handle",
        "the robot's gripper is not vertically aligned with drawer handle": "put gripper above drawer handle",
        "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "the robot's gripper is around drawer handle": "pull away from drawer",
        "drawer handle is vertically aligned with the robot's gripper and the robot's gripper is around drawer handle": "pull away from drawer",
    },
    "drawer-close": {
        "gripper is open": "put the gripper in front of the drawer",
        "drawer handle is vertically aligned with the robot's gripper and gripper is open": "put the gripper in front of the drawer",
        "drawer handle is below the robot's gripper": "put the gripper above the drawer handle",
        "the robot's gripper is above drawer handle": "put the gripper above the drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and drawer handle is not forward aligned with the robot's gripper": "grab drawer handle",
        "drawer handle is not vertically aligned with the robot's gripper and the robot's gripper is not forward aligned with drawer handle": "grab drawer handle",
        "drawer handle is forward aligned with the robot's gripper": "push drawer closed",
        "the robot's gripper is forward aligned with drawer handle": "push drawer closed",
    },
    "button-press-topdown": {
        "button is not vertically aligned with the robot's gripper": "put gripper above button",
        "the robot's gripper is not vertically aligned with button": "put gripper above button",
        "button is vertically aligned with the robot's gripper": "push down on button",
        "the robot's gripper is vertically aligned with button": "push down on button",
    },
    "peg-insert-side": {
        "peg is left of the robot's gripper": "put gripper above peg",
        "the robot's gripper is right of peg": "put gripper above peg",
        "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper": "grab peg",
        "peg is not left of the robot's gripper and the robot's gripper is not forward aligned with peg": "grab peg",
        "peg is forward aligned with the robot's gripper and peg is not horizontally aligned with hole": "align peg to hole",
        "peg is forward aligned with the robot's gripper and hole is not horizontally aligned with peg": "align peg to hole",
        "peg is horizontally aligned with hole": "insert peg into hole",
        "hole is horizontally aligned with peg": "insert peg into hole",
    },
    "window-open": {
        "window handle is not vertically aligned with the robot's gripper and the robot's gripper is mostly below window handle": "move gripper to right of window handle",
        "the robot's gripper is mostly below window handle and window handle is not vertically aligned with the robot's gripper": "move gripper to right of window handle",
        "window handle is left of the robot's gripper and window handle is vertically aligned with the robot's gripper": "slide window left",
        "window handle is left of the robot's gripper and window handle is almost vertically aligned with the robot's gripper": "slide window left",
        "window handle is near the robot's gripper": "push window left harder",
        "window handle is behind the robot's gripper": "push window left harder",
    },
    "window-close": {
        "window handle is not vertically aligned with the robot's gripper": "move gripper to left of window handle",
        "the robot's gripper is not vertically aligned with window handle": "move gripper to left of window handle",
        "window handle is right of the robot's gripper": "slide window right",
        "the robot's gripper is left of window handle": "slide window right",
        "window handle is vertically aligned with the robot's gripper and window handle is not right of the robot's gripper": "push window right harder",
        "window handle is vertically aligned with the robot's gripper and the robot's gripper is not left of window handle": "push window right harder",
    },
}

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
        return dedent(
            f"""\
                    if check("{cond}"):
                        robot.{action.split(' ')[0]}("{' '.join(action.split(' ')[1:])}")"""
        )


def plan_str(env_name, plan):
    header = dedent(
        f"""\
                  # {env_name}: {MT50_TASK_DESCRIPTIONS[env_name]}
                  def {env_name.replace('-', '_')}(robot):"""
    )
    clauses = [clause_str(cond, action) for (cond, action) in plan.items()]
    return "\n".join([header] + [indent(clause, " " * 4) for clause in clauses])


def print_plans():
    for (env_name, plan) in MT10_PLANS.items():
        print(plan_str(env_name, plan))
        print()
        print()


FN_NAME = re.compile(r"def ([a-zA-Z_]+)\(")
CLAUSES = re.compile(r'if check\("([^"]+)"\):\s+([^\n]+)', flags=re.MULTILINE)
VERB_DETAILS = re.compile(r'robot.([a-zA-Z_]+)\("([^"]+)"\)')
MOVE_GRIPPER = re.compile(f'robot.move_gripper\("([^"]+)"\)')
CLOSE_GRIPPER = re.compile(f'robot.move_gripper\("([^"]+)", close_gripper=True\)')
OPEN_GRIPPER = re.compile(f'robot.move_gripper\("([^"]+)", open_gripper=True\)')


def preprocess_location(action):
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


def load_and_parse_plans(filename="mt10_plans.py"):
    with open(filename, "r") as f:
        contents = f.read()
    without_comments = []
    for line in contents.split("\n"):
        if "#" in line:
            without_comments.append(line.split("#")[0])
        else:
            without_comments.append(line)
    contents = "\n".join(without_comments)
    print(contents)
    plans_parsed = {}
    for plan in contents.split("\n\n"):
        names = FN_NAME.findall(plan)
        if names:
            clause_map = {}
            for (cond, action) in CLAUSES.findall(plan):
                verb_details = VERB_DETAILS.findall(action)
                if verb_details and verb_details[0][0] != "move_gripper":
                    clause_map[cond] = " ".join(verb_details[0])
                close_gripper = CLOSE_GRIPPER.findall(action)
                if close_gripper:
                    loc = preprocess_location(close_gripper[0])
                    clause_map[cond] = f"{loc} and the robot's gripper is closed"
                open_gripper = OPEN_GRIPPER.findall(action)
                if open_gripper:
                    loc = preprocess_location(open_gripper[0])
                    clause_map[cond] = f"{loc} and the robot's gripper is open"
                    clause_map[cond] = (
                        f"the robot's gripper is {loc}"
                        " and the robot's gripper is open"
                    )
                move_gripper = MOVE_GRIPPER.findall(action)
                if move_gripper:
                    clause_map[cond] = preprocess_location(move_gripper[0])
            plans_parsed[names[0].replace("_", "-")] = clause_map
    return plans_parsed


def load_and_parse_plans_as_list(filename="mt10_plans.py"):
    with open(filename, "r") as f:
        contents = f.read()
    without_comments = []
    for line in contents.split("\n"):
        if "#" in line:
            without_comments.append(line.split("#")[0])
        else:
            without_comments.append(line)
    contents = "\n".join(without_comments)
    print(contents)
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


@dataclass
class DescriptorPolicy:
    descriptor_to_scripted_skill: dict
    env_name: str
    scripted_skill_choice_prob: float = 1.0
    base_weight: Union[float, None] = None

    def get_action(self, observation):
        tree = metaworld_scripted_skills.DECISION_TREES[self.env_name]["function"]
        obs = parse_obs(observation)
        candidate_scripted_skills = [
            con
            for (desc, con) in self.descriptor_to_scripted_skill.items()
            if eval_conditions(self.env_name, [desc], obs)[0]
        ]
        if (
            candidate_scripted_skills
            and np.random.uniform() < self.scripted_skill_choice_prob
        ):
            scripted_skill_name = random.choice(candidate_scripted_skills)
        else:
            scripted_skill_name = random.choice(
                list(self.descriptor_to_scripted_skill.values())
            )
        ground_truth_scripted_skill_name = tree(obs)
        info = {}
        info["scripted_skill_name"] = scripted_skill_name
        info["candidate_scripted_skills"] = list(set(candidate_scripted_skills))
        if self.base_weight:
            descriptors = list(self.descriptor_to_scripted_skill.keys())
            weights = np.array(
                [
                    1.0
                    if eval_conditions(self.env_name, [desc], obs)[0]
                    else self.base_weight
                    for desc in descriptors
                ]
            )
            weights /= weights.sum()
            actions = np.array(
                [
                    run_scripted_skill(self.descriptor_to_scripted_skill[desc], obs)
                    for desc in descriptors
                ]
            )
            weighted_action = np.einsum("i,ik->k", weights, actions)
            return weighted_action, info
        else:
            return run_scripted_skill(scripted_skill_name, obs), info


def eval_plans(
    *,
    filename="mt10_plans.py",
    seed=DEFAULT_SEED,
    env_names: str_list = None,
    noise_scale: float = 0.05,
):
    generate_metaworld_scene_dataset.jnp = np
    success_rates = {}
    plans = load_and_parse_plans(filename)
    # print(plans)
    if env_names is None:
        env_names = list(plans.keys())
    for env_name in env_names:
        plan = plans[env_name]
        pprint(list(plan.items()))
        policy = DescriptorPolicy(plan, env_name=env_name)
        env = make_env(env_name, seed)
        success = generate_metaworld_scene_dataset.evaluate_policy(
            env_name,
            (sample_noisy_policy(env, policy, noise_scale) for _ in tqdm(range(20)))
            # collect_noisy_episodes(
            # 50 * [env_name], policy, seed=seed, n_episodes=100,
            # noise_scale=noise_scale
            # ),
        )
        success_rates[env_name] = success
    print(success_rates)
    return success_rates


def load_best_cond_agent_params():
    with open(expanduser("~/data/best_cond_agent.pkl"), "rb") as f:
        cond_eval_state = pickle.load(f)
    return cond_eval_state


def run_cond_agent_mt50(
    *, seed=jax_utils.DEFAULT_SEED, env_names: str_list = MT50_ENV_NAMES
):
    import embed_prompt

    embedded_plans = {}
    parsed_plans = load_and_parse_plans("mt50_plans.py")
    print("Embedding plans...")
    for (plan_name, plan) in parsed_plans.items():
        conds = list(plan.keys())
        conds_embed = jnp.stack(
            [np.array(embed_prompt.embed_condition(cond)) for cond in conds]
        )
        actions_embed = jnp.stack(
            [np.array(embed_prompt.embed_action(plan[cond])) for cond in conds]
        )
        embedded_plans[plan_name] = {
            # 'conds': self.param(f'{plan_name}.conds', lambda _: conds_embed),
            # 'actions': self.param(f'{plan_name}.actions', lambda _: actions_embed),
            "conds": conds_embed,
            "actions": actions_embed,
            "conds_str": conds,
            "actions_str": [plan[cond] for cond in conds],
        }
    # embed_prompt.save_cache()
    print("Done embedding plans")

    from evaluator_agent import CondAgent

    cond_agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=True,
        use_learned_scripted_skill=True,
        plans=embedded_plans,
    )

    batch_size = 4
    rng = jax.random.PRNGKey(seed)
    rng, init_rng = jax.random.split(rng)
    params = load_best_cond_agent_params()
    print(params)
    # params = cond_agent.init(init_rng,
    # ["drawer-close", "pick-place"] * int(batch_size / 2),
    # jnp.ones([batch_size, 39]))
    # params = params.copy({"params": {"cond_evaluator": load_best_evaluator_params()}})
    learning_rate = 1e-5
    momentum = 0.99
    tx = optax.sgd(learning_rate, momentum)
    tstate = train_state.TrainState.create(
        apply_fn=cond_agent.apply, params=params, tx=tx
    )

    success_rates = {}
    rewards = {}
    for env_name in parsed_plans:
        print(env_name)
        policy = cond_agent.as_policy(env_name, tstate)
        env = make_env(env_name, seed)
        success, rew = evaluate_policy(
            env_name,
            # [sample_noisy_policy(env, policy, 0.05) for _ in tqdm(range(20))]
            collect_noisy_episodes(
                20 * [env_name], policy, seed=seed, n_episodes=100, noise_scale=0.05
            ),
        )
        success_rates[env_name] = success
        rewards[env_name] = rew
        for i in range(20):
            render_success, _ = render_policy(
                env, policy, expanduser(f"~/data/{env_name}-cond-agent.mp4")
            )
            if render_success:
                shutil.copy(
                    expanduser(f"~/data/{env_name}-cond-agent.mp4"),
                    expanduser(f"~/data/{env_name}-cond-agent-success.mp4"),
                )
                print(f"Rendered successful episode for {env_name}")
                break
            elif success == 0:
                print(f"Skipping additional renders of {env_name}")
                break
            elif i == 19:
                print(f"Could not render successful episode for {env_name}")

    print(success_rates)
    print(rewards)

    results = {
        "door-open": 1.0,
        "drawer-open": 1.0,
        "assembly": 0.0,
        "basketball": 0.0,
        "button-press-topdown": 1.0,
        "button-press-topdown-wall": 1.0,
        "button-press": 0.0,
        "button-press-wall": 0.1,
        "coffee-button": 1.0,
        "coffee-pull": 0.1,
        "coffee-push": 0.2,
        "bin-picking": 0.0,
        "dial-turn": 0.0,
        "disassemble": 0.0,
        "drawer-close": 1.0,
        "faucet-open": 0.0,
        "faucet-close": 0.6,
        "hammer": 0.0,
        "box-close": 0.0,
        "handle-press-side": 1.0,
        "handle-press": 0.8,
        "handle-pull-side": 0.0,
        "handle-pull": 0.0,
        "lever-pull": 0.0,
        "peg-insert-side": 0.0,
        "peg-unplug-side": 0.0,
        "pick-out-of-hole": 0.0,
        "pick-place": 0.0,
        "door-lock": 1.0,
        "pick-place-wall": 0.8,
        "plate-slide": 0.0,
        "plate-slide-side": 0.0,
        "plate-slide-back": 0.0,
        "plate-slide-back-side": 0.1,
        "push-back": 0.0,
        "push": 0.0,
        "push-wall": 0.1,
        "reach": 0.0,
        "door-unlock": 0.7,
        "reach-wall": 0.0,
        "shelf-place": 0.0,
        "soccer": 0.0,
        "stick-push": 0.0,
        "stick-pull": 0.0,
        "sweep-into": 1.0,
        "sweep": 0.0,
        "window-open": 1.0,
        "window-close": 1.0,
        "hand-insert": 0.0,
        "door-close": 0.5,
    }


COND_AGENT_MT50_SUCCESS_RATES = {
    "door-open": 1.0,
    "drawer-open": 1.0,
    "assembly": 0.0,
    "basketball": 0.0,
    "button-press-topdown": 1.0,
    "button-press-topdown-wall": 1.0,
    "button-press": 0.0,
    "button-press-wall": 0.0,
    "coffee-button": 1.0,
    "coffee-pull": 0.0,
    "coffee-push": 0.3277310924369748,
    "bin-picking": 0.0,
    "dial-turn": 0.0,
    "disassemble": 0.0,
    "drawer-close": 1.0,
    "faucet-open": 0.0,
    "faucet-close": 1.0,
    "hammer": 0.0,
    "box-close": 0.0,
    "handle-press-side": 1.0,
    "handle-press": 1.0,
    "handle-pull-side": 0.0,
    "handle-pull": 0.0,
    "lever-pull": 0.0,
    "peg-insert-side": 0.0,
    "peg-unplug-side": 0.0,
    "pick-out-of-hole": 0.0,
    "pick-place": 0.33613445378151263,
    "door-lock": 0.8,
    "pick-place-wall": 0.8,
    "plate-slide": 0.0,
    "plate-slide-side": 0.0,
    "plate-slide-back": 0.0,
    "plate-slide-back-side": 0.2,
    "push-back": 0.0,
    "push": 0.0,
    "push-wall": 0.0,
    "reach": 0.0,
    "door-unlock": 1.0,
    "reach-wall": 0.0,
    "shelf-place": 0.0,
    "soccer": 0.3277310924369748,
    "stick-push": 0.0,
    "stick-pull": 0.0,
    "sweep-into": 0.0,
    "sweep": 0.0,
    "window-open": 1.0,
    "window-close": 1.0,
    "hand-insert": 0.33613445378151263,
    "door-close": 0.0,
}

COND_AGENT_MT50_AVG_REWARDS = {
    "door-open": 4.832744201843733,
    "drawer-open": 6.779472281802684,
    "assembly": 0.7907047011704622,
    "basketball": 0.0401335967003641,
    "button-press-topdown": 2.4320281451598453,
    "button-press-topdown-wall": 2.441310434666451,
    "button-press": 1.5928397279317537,
    "button-press-wall": 2.8740240780375403,
    "coffee-button": 0.5136896228296887,
    "coffee-pull": 0.06349058447050131,
    "coffee-push": 0.820363037195592,
    "bin-picking": 0.07365367959845744,
    "dial-turn": 0.0,
    "disassemble": 0.6137373790736731,
    "drawer-close": 8.348006787275224,
    "faucet-open": 3.841867310857751,
    "faucet-close": 6.691619706861348,
    "hammer": 1.0582331282664468,
    "box-close": 0.43441998485522654,
    "handle-press-side": 3.9988713529666113,
    "handle-press": 2.2629697429159092,
    "handle-pull-side": 0.07622844454659186,
    "handle-pull": 0.23800977606830284,
    "lever-pull": 0.9280958338825261,
    "peg-insert-side": 0.5194617376342479,
    "peg-unplug-side": 0.15540857405352307,
    "pick-out-of-hole": 0.023711271930740317,
    "pick-place": 1.4731109759624283,
    "door-lock": 4.58277408416355,
    "pick-place-wall": 5.3571015128856265,
    "plate-slide": 1.0241282704846115,
    "plate-slide-side": 1.201046600160031,
    "plate-slide-back": 0.48291988084651083,
    "plate-slide-back-side": 4.321487126648609,
    "push-back": 0.08368613756830115,
    "push": 0.6620759860499941,
    "push-wall": 0.44768513549580186,
    "reach": 1.2659688701020806,
    "door-unlock": 2.7314037777263964,
    "reach-wall": 2.152393212263986,
    "shelf-place": 0.010100094436881632,
    "soccer": 2.007491770131034,
    "stick-push": 0.11808060771539967,
    "stick-pull": 0.051553445307199845,
    "sweep-into": 1.4271523935437664,
    "sweep": 0.2690005521563934,
    "window-open": 3.78505119299706,
    "window-close": 7.455605275749486,
    "hand-insert": 1.6011996255374634,
    "door-close": 0.6176600280161432,
}


def eval_universal_agent(
    *, seed=jax_utils.DEFAULT_SEED, env_names: str_list = MT50_ENV_NAMES
):
    policy = SawyerUniversalV2Policy()
    policy_name = "universal"
    success_rates = {}
    rewards = {}
    for env_name in env_names:
        print(env_name)
        policy.env_name = env_name
        env = make_env(env_name, seed)
        success, rew = evaluate_policy(
            env_name,
            # [sample_noisy_policy(env, policy, 0.05) for _ in tqdm(range(20))]
            collect_noisy_episodes(
                20 * [env_name], policy, seed=seed, n_episodes=100, noise_scale=0.05
            ),
        )
        success_rates[env_name] = success
        rewards[env_name] = rew
        for i in range(20):
            render_success, _ = render_policy(
                env, policy, expanduser(f"~/data/{env_name}-{policy_name}-{i}.mp4")
            )
            if render_success:
                shutil.copy(
                    expanduser(f"~/data/{env_name}-{policy_name}-{i}.mp4"),
                    expanduser(f"~/data/{env_name}-{policy_name}-success.mp4"),
                )
                print(f"Rendered successful episode for {env_name}")
                break
            elif success == 0:
                print(f"Skipping additional renders of {env_name}")
                break
            elif i == 19:
                print(f"Could not render successful episode for {env_name}")

    print(success_rates)
    print(rewards)


UNIVERSAL_POLICY_MT50_SUCCESS_RATES = {
    "assembly": 1.0,
    "basketball": 1.0,
    "bin-picking": 1.0,
    "box-close": 1.0,
    "button-press-topdown": 1.0,
    "button-press-topdown-wall": 1.0,
    "button-press": 1.0,
    "button-press-wall": 1.0,
    "coffee-button": 1.0,
    "coffee-pull": 1.0,
    "coffee-push": 1.0,
    "dial-turn": 1.0,
    "disassemble": 1.0,
    "door-close": 1.0,
    "door-lock": 1.0,
    "door-open": 1.0,
    "door-unlock": 1.0,
    "hand-insert": 1.0,
    "drawer-close": 1.0,
    "drawer-open": 1.0,
    "faucet-open": 1.0,
    "faucet-close": 1.0,
    "hammer": 1.0,
    "handle-press-side": 1.0,
    "handle-press": 1.0,
    "handle-pull-side": 1.0,
    "handle-pull": 1.0,
    "lever-pull": 1.0,
    "peg-insert-side": 1.0,
    "pick-place-wall": 1.0,
    "pick-out-of-hole": 1.0,
    "reach": 1.0,
    "push-back": 1.0,
    "push": 1.0,
    "pick-place": 1.0,
    "plate-slide": 1.0,
    "plate-slide-side": 1.0,
    "plate-slide-back": 1.0,
    "plate-slide-back-side": 1.0,
    "peg-unplug-side": 0.8,
    "soccer": 1.0,
    "stick-push": 1.0,
    "stick-pull": 0.8,
    "push-wall": 1.0,
    "reach-wall": 1.0,
    "shelf-place": 1.0,
    "sweep-into": 1.0,
    "sweep": 1.0,
    "window-open": 1.0,
    "window-close": 1.0,
}
UNIVERSAL_POLICY_MT50_REWARDS = {
    "assembly": 8.620974144625707,
    "basketball": 8.159030897938049,
    "bin-picking": 7.453498761291571,
    "box-close": 8.453067703058407,
    "button-press-topdown": 7.736315817279586,
    "button-press-topdown-wall": 8.65356303178741e-06,
    "button-press": 1.097237480197445,
    "button-press-wall": 5.845410150045204,
    "coffee-button": 0.9624949603100298,
    "coffee-pull": 8.503358317797748,
    "coffee-push": 3.8273922479312805,
    "dial-turn": 7.495605806924134,
    "disassemble": 7.659915153746863,
    "door-close": 9.107683490781367,
    "door-lock": 6.432786935405873,
    "door-open": 8.453754381783037,
    "door-unlock": 6.888390002210485,
    "hand-insert": 6.290221035449021,
    "drawer-close": 8.531454424993694,
    "drawer-open": 8.174588208421888,
    "faucet-open": 8.121981431700094,
    "faucet-close": 7.9366850919474325,
    "hammer": 2.5449725444010745,
    "handle-press-side": 1.9644419855294364,
    "handle-press": 2.6710785493120937,
    "handle-pull-side": 6.3400635227936,
    "handle-pull": 7.91908899932046,
    "lever-pull": 1.031074870256094,
    "peg-insert-side": 7.913621924377314,
    "pick-place-wall": 8.60096018377793,
    "pick-out-of-hole": 7.315644046473473,
    "reach": 9.659844960150942,
    "push-back": 0.9078517909425513,
    "push": 7.458508614112852,
    "pick-place": 8.939628841218017,
    "plate-slide": 8.554776024364273,
    "plate-slide-side": 6.881260839968695,
    "plate-slide-back": 2.389051096658791,
    "plate-slide-back-side": 1.5955390795186486,
    "peg-unplug-side": 1.7760022692123942,
    "soccer": 5.381428840546107,
    "stick-push": 1.976047113043637,
    "stick-pull": 0.9242958863561005,
    "push-wall": 8.258202024683364,
    "reach-wall": 9.665049295469473,
    "shelf-place": 6.558495178959657,
    "sweep-into": 2.1009095626808523,
    "sweep": 8.648997454469987,
    "window-open": 3.366995077637805,
    "window-close": 6.739395638308984,
}

mt10_plans = {
    "reach": {"the robot's gripper is not near reach target": "reach to goal"},
    "push": {
        "the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck": "put the gripper above the puck",
        "the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck": "push the gripper into the puck",
        "the robot's gripper is near the puck and the puck is below the robot's gripper": "slide the puck to the goal",
    },
    "pick-place": {
        "the robot's gripper is not above the puck": "place gripper above puck",
        "the robot's gripper is not around puck and the robot's gripper is open": "drop gripper around puck",
        "the robot's gripper is near puck and the robot's gripper is open": "close gripper around puck",
        "the robot's gripper is above puck and the robot's gripper is closed": "place puck at goal",
    },
    "door-open": {
        "the robot's gripper is not almost vertically aligned with door handle": "put gripper above door handle",
        "the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open": "put gripper around door handle",
        "the robot's gripper is vertically aligned with the door handle": "pull door open",
    },
    "drawer-open": {
        "the robot's gripper is not vertically aligned with drawer handle": "put gripper above drawer handle",
        "the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle": "put gripper around drawer handle",
        "the robot's gripper is around drawer handle": "pull away from drawer",
    },
    "drawer-close": {
        "the robot's gripper is not near the drawer handle": "grab drawer handle",
        "the robot's gripper is forward aligned with drawer handle": "push drawer closed",
    },
    "button-press-topdown": {
        "the robot's gripper is not vertically aligned with button": "put gripper above button",
        "the robot's gripper is vertically aligned with button": "push down on button",
    },
    "peg-insert-side": {
        "the robot's gripper is not vertically aligned with the peg": "put gripper above peg",
        "peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper": "grab peg",
        "the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole": "align peg to hole",
        "peg is horizontally aligned with hole": "insert peg into hole",
    },
    "window-open": {
        "the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle": "move gripper to right of window handle",
        "the robot's gripper is near the window handle": "slide window left",
        "the robot's gripper is in front of the window handle": "push window left harder",
    },
    "window-close": {
        "the window handle is right of the robot's gripper and the robot's gripper is not near the window handle": "move gripper to left of window handle",
        "the robot's gripper is near the window handle": "slide window right",
        "the robot's gripper is in front of the window handle": "push window right harder",
    },
}

if __name__ == "__main__":
    # clize.run(eval_plans)
    # print(load_mt10_plans())
    # print(load_and_parse_plans('mt50_plans.py'))
    print(load_and_parse_plans("mt10_plans.py"))
    # clize.run(run_cond_agent_mt50)
    # clize.run(eval_universal_agent)
    # print('Environment Name, Zero-Shot Success Rate, Reward Percentage')
    # for env_name in MT50_ENV_NAMES:
    # if env_name in MT10_ENV_NAMES:
    # continue
    # print(env_name, "{}%".format(int(100 * COND_AGENT_MT50_SUCCESS_RATES[env_name])),
    # "{}%".format(int(100 * COND_AGENT_MT50_AVG_REWARDS[env_name] /
    # UNIVERSAL_POLICY_MT50_REWARDS[env_name])), sep=',')
