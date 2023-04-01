from dataclasses import dataclass
import metaworld_scripted_skills
import random
import sample_utils
import clize

SCRIPTED_SKILL_NAMES = list(metaworld_scripted_skills.SCRIPTED_SKILLS.keys())


@dataclass
class RandLangAgent:
    """Agent that selects a random language primitive every n timesteps"""

    env_name: str or None = None  # Ignored
    n_timesteps: int = 25
    current_scripted_skill: str or None = None
    timesteps_at_current_scripted_skill: int = 0

    def reset(self):
        self.current_scripted_skill = None
        self.timesteps_at_current_scripted_skill = 0

    def get_action(self, observation):
        if self.timesteps_at_current_scripted_skill % self.n_timesteps == 0:
            self.timesteps_at_current_scripted_skill = 0
            self.current_scripted_skill = random.choice(SCRIPTED_SKILL_NAMES)
        self.timesteps_at_current_scripted_skill += 1
        parsed_obs = metaworld_scripted_skills.parse_obs(observation)
        return (
            metaworld_scripted_skills.run_scripted_skill(
                self.current_scripted_skill, parsed_obs
            ),
            {"scripted_skill_name": self.current_scripted_skill},
        )


def evaluate(*, seed=random.randrange(1000), out_file):
    policy = RandLangAgent()
    evaluator = sample_utils.Evaluator(
        seed, env_names=sample_utils.MT50_ENV_NAMES, output_filename=out_file
    )
    evaluator.evaluate(policy)


if __name__ == "__main__":
    clize.run(evaluate)
