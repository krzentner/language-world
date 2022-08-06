import clize
from sample_utils import make_env
from metaworld_universal_policy import SawyerUniversalV2Policy
from os.path import expanduser
import tempfile
import cv2
import numpy as np
from subprocess import run
from tqdm import tqdm

from gaussian_noise_process import GaussianNoiseProcess

FRAME_WIDTH = 800
FRAME_HEIGHT = 600


def render_frame(env, tmpdirname, frame):
  img = env.sim.render(FRAME_WIDTH, FRAME_HEIGHT, camera_name='corner4',
                         depth=False)
  img = np.flip(img, axis=0)
  cv2.imwrite(f'{tmpdirname}/{frame:04d}.png', img[:, :, [2, 1, 0]])
  return frame + 1


def render_policy(env, policy, filename, noise_process=None, frame_skip=2,
                  freeze_on_success=False):
  if noise_process is None:
    noise_process = GaussianNoiseProcess(dimensions=4, noise_scale=0.05)
  frame = 0
  success = False
  total_reward = 0
  with tempfile.TemporaryDirectory() as tmpdirname:
    noise_process.reset()
    observation = env.reset()
    for i in tqdm(range(env.max_episode_length)):
      if i % frame_skip == 0:
        if freeze_on_success and success:
          shutil.copy(f'{tmpdirname}/{frame:04d}.png',
                      f'{tmpdirname}/{frame + 1:04d}.png')
          frame += 1
        else:
          frame = render_frame(env, tmpdirname, frame)
      action, agent_info = policy.get_action(observation)
      action_noisy = action + noise_process.simulate()
      next_obs, reward, done, info = env.step(action_noisy)
      success = success | (info['success'] > 0)
      total_reward += reward
      observation = next_obs
    print('Rendering video...')
    run(['ffmpeg', '-y', '-pattern_type', 'glob', '-i', f'{tmpdirname}/*.png', filename])
    print('Done rendering video')
  return success, total_reward


def test_smoke(env_name='pick-place'):
  env = make_env(env_name, 100)
  policy = SawyerUniversalV2Policy(env_name)
  noise_process = GaussianNoiseProcess(dimensions=4)
  render_policy(env, policy,
                expanduser(f'~/data/{env_name}-universal-policy.mp4'),
                noise_process)


if __name__ == '__main__':
  clize.run(test_smoke)
