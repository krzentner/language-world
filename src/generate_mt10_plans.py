import os
import pickle
import re
import optax
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
)
from flax.training import train_state
import jax_utils
from run_utils import str_list
import metaworld_controllers
from metaworld_controllers import SawyerUniversalV2Policy, parse_obs, run_controller
import numpy as np
import random
import embed_prompt
import jax
import jax.numpy as jnp
from evaluator_agent import CondAgent
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
    "window-open": "slide the window open",
    "window-close": "slide the window closed",
    "hand-insert": "pick up the puck and move it to the target location",
    "door-close": "push the door closed to the target location",
}


def plan_str(env_name, plan):
    header = dedent(
        f"""\
                  # {env_name}: {MT50_TASK_DESCRIPTIONS[env_name]}
                  def {env_name.replace('-', '_')}(robot):"""
    )
    clauses = [
        dedent(
            f"""\
                    if check("{cond}"):
                        robot.{action.split(' ')[0]}("{' '.join(action.split(' ')[1:])}")"""
        )
        for (cond, action) in plan.items()
    ]
    return "\n".join([header] + [indent(clause, " " * 4) for clause in clauses])


def print_plans():
    for (env_name, plan) in MT10_PLANS.items():
        print(plan_str(env_name, plan))
        print()
        print()


FN_NAME = re.compile(r"def ([a-zA-Z_]+)\(")
CLAUSES = re.compile(r'if check\("([^"]+)"\):\s+([^\n]+)', flags=re.MULTILINE)
VERB_DETAILS = re.compile(r'robot.([a-zA-Z_]+)\("([^"]+)"\)')


def load_and_parse_plans(filename="mt10_plans.py"):
    with open(filename, "r") as f:
        contents = f.read()
    without_comments = []
    for line in contents.split('\n'):
        if '#' in line:
            without_comments.append(line.split('#')[0])
        else:
            without_comments.append(line)
    contents = '\n'.join(without_comments)
    print(contents)
    plans_parsed = {
        FN_NAME.findall(plan)[0].replace("_", "-"): {
            cond: " ".join(VERB_DETAILS.findall(action)[0])
            for (cond, action) in CLAUSES.findall(plan)
        }
        for plan in contents.split("\n\n")
        if FN_NAME.findall(plan)
    }
    return plans_parsed


@dataclass
class DescriptorPolicy:
    descriptor_to_controller: dict
    env_name: str
    controller_choice_prob: float = 1.0
    base_weight: float or None = None

    def get_action(self, observation):
        tree = metaworld_controllers.DECISION_TREES[self.env_name]["function"]
        obs = parse_obs(observation)
        candidate_controllers = [
            con
            for (desc, con) in self.descriptor_to_controller.items()
            if eval_conditions(self.env_name, [desc], obs)[0]
        ]
        if candidate_controllers and np.random.uniform() < self.controller_choice_prob:
            controller_name = random.choice(candidate_controllers)
        else:
            controller_name = random.choice(
                list(self.descriptor_to_controller.values())
            )
        ground_truth_controller_name = tree(obs)
        info = {}
        info["controller_name"] = controller_name
        info["candidate_controllers"] = list(set(candidate_controllers))
        if self.base_weight:
            descriptors = list(self.descriptor_to_controller.keys())
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
                    run_controller(self.descriptor_to_controller[desc], obs)
                    for desc in descriptors
                ]
            )
            weighted_action = np.einsum("i,ik->k", weights, actions)
            return weighted_action, info
        else:
            return run_controller(controller_name, obs), info


def eval_plans(
    *, filename="mt10_plans.py", seed=jax_utils.DEFAULT_SEED, env_names:
    str_list = None, noise_scale: float = 0.05
):
    success_rates = {}
    plans = load_and_parse_plans(filename)
    print(plans)
    if env_names is None:
        env_names = list(plans.keys())
    for env_name in env_names:
        plan = plans[env_name]
        policy = DescriptorPolicy(plan, env_name=env_name)
        env = make_env(env_name, seed)
        success = generate_metaworld_scene_dataset.evaluate_policy(
            env_name,
            (sample_noisy_policy(env, policy, noise_scale) for _ in tqdm(range(10)))
            # collect_noisy_episodes(
                # 50 * [env_name], policy, seed=seed, n_episodes=100,
                   # noise_scale=noise_scale
            # ),
        )
        success_rates[env_name] = success
    print(success_rates)
    return success_rates


def load_best_cond_agent_params():
    with open(os.path.expanduser("~/data/best_cond_agent.pkl"), "rb") as f:
        cond_eval_state = pickle.load(f)
    return cond_eval_state


def run_cond_agent_mt50(
    *, seed=jax_utils.DEFAULT_SEED, env_names: str_list = MT50_ENV_NAMES
):
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

    cond_agent = CondAgent(
        use_learned_evaluator=False,
        mix_in_language_space=True,
        use_learned_controller=True,
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
    for env_name in parsed_plans:
        print(env_name)
        policy = cond_agent.as_policy(env_name, tstate)
        env = make_env(env_name, seed)
        success = generate_metaworld_scene_dataset.evaluate_policy(
            env_name,
            [sample_noisy_policy(env, policy, 0.05) for _ in tqdm(range(10))]
            # collect_noisy_episodes(
            # 20 * [env_name], desc_policy, seed=seed, n_episodes=100, noise_scale=0.1
            # ),
        )
        success_rates[env_name] = success
        render_policy(env, policy,
                      os.path.expanduser(f'~/data/{env_name}-cond-agent.mp4'))

    print(success_rates)
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


if __name__ == "__main__":
    # clize.run(eval_plans)
    # print(load_mt10_plans())
    # print(load_and_parse_plans())
    clize.run(run_cond_agent_mt50)
