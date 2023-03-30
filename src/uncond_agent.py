from dataclasses import dataclass
import metaworld_controllers
import random
import sample_utils
import clize
from generate_mt10_plans import load_and_parse_plans_as_list
from sample_utils import str_project

PRIMITIVE_NAMES = list(metaworld_controllers.CONTROLLERS.keys())
PROJ_CACHE = {}


@dataclass
class UncondAgent:
    """Agent that runs each language primitive in sequence"""

    plans: dict
    env_name: str or None = None
    n_timesteps: int = 50
    current_timestep: int = 0

    def reset(self):
        self.current_timestep = 0

    def get_action(self, observation):
        self.current_timestep = self.current_timestep % 500
        controller_number = int(self.current_timestep / self.n_timesteps)
        controller_idx = controller_number % len(self.plans[self.env_name])
        controller_name = self.plans[self.env_name][controller_idx][1]
        if controller_name not in PROJ_CACHE:
            PROJ_CACHE[controller_name] = str_project(controller_name, PRIMITIVE_NAMES)[
                0
            ]
        chosen_controller = PROJ_CACHE[controller_name]
        parsed_obs = metaworld_controllers.parse_obs(observation)
        return (
            metaworld_controllers.run_controller(chosen_controller, parsed_obs),
            {"controller_name": controller_name},
        )


def evaluate(*, seed=random.randrange(1000), plan_file="mt50_plans_v1.py", out_file):
    parsed_plans = load_and_parse_plans_as_list(plan_file)
    policy = UncondAgent(plans=parsed_plans)
    evaluator = sample_utils.Evaluator(
        seed, env_names=sample_utils.MT50_ENV_NAMES, output_filename=out_file
    )
    evaluator.evaluate(policy)


if __name__ == "__main__":
    clize.run(evaluate)
