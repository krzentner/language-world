from dataclasses import dataclass
import metaworld_controllers
import random
import sample_utils
import clize

CONTROLLER_NAMES = list(metaworld_controllers.CONTROLLERS.keys())


@dataclass
class RandLangAgent:
    """Agent that selects a random language primitive every n timesteps"""

    env_name: str or None = None  # Ignored
    n_timesteps: int = 25
    current_controller: str or None = None
    timesteps_at_current_controller: int = 0

    def reset(self):
        self.current_controller = None
        self.timesteps_at_current_controller = 0

    def get_action(self, observation):
        if self.timesteps_at_current_controller % self.n_timesteps == 0:
            self.timesteps_at_current_controller = 0
            self.current_controller = random.choice(CONTROLLER_NAMES)
        self.timesteps_at_current_controller += 1
        parsed_obs = metaworld_controllers.parse_obs(observation)
        return (
            metaworld_controllers.run_controller(self.current_controller, parsed_obs),
            {"controller_name": self.current_controller},
        )


def evaluate(*, seed=random.randrange(1000), out_file):
    policy = RandLangAgent()
    evaluator = sample_utils.Evaluator(
        seed, env_names=sample_utils.MT50_ENV_NAMES, output_filename=out_file
    )
    evaluator.evaluate(policy)


if __name__ == "__main__":
    clize.run(evaluate)
