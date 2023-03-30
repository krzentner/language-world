import clize
import shutil
import tempfile
import numpy as np
from subprocess import run
from tqdm import tqdm
from PIL import Image

from metaworld_universal_policy import SawyerUniversalV2Policy
from sample_utils import MT50_ENV_NAMES, make_env
from gaussian_noise_process import GaussianNoiseProcess

FRAME_WIDTH = 1800
FRAME_HEIGHT = 1200

ORIGINAL_FRAME_WIDTH = 800
ORIGINAL_FRAME_HEIGHT = 600

ASPECT_RATIO = (4, 3)
ROW_HEIGHTS = [360, 330, 270, 240]
ROW_OFFSETS = [0, -40, -120, -180]
N_FRAMES_PER_EPISODE = 250
N_FRAMES = (N_FRAMES_PER_EPISODE) * 4


assert sum(ROW_HEIGHTS) >= FRAME_HEIGHT
assert sum(ROW_HEIGHTS[:-1]) <= FRAME_HEIGHT


def render_frame(env, large_frame, x, y, width, height):
    img = env.sim.render(
        ORIGINAL_FRAME_WIDTH, ORIGINAL_FRAME_HEIGHT, camera_name="corner4", depth=False
    )
    img = np.flip(img, axis=0)
    img = np.flip(img, axis=1)
    # img = env.render("rgb_array")
    # img_to_resize = Image.fromarray(img[:, :, [2, 1, 0]])
    img_to_resize = Image.fromarray(img[:, :, [0, 1, 2]])
    img_small = img_to_resize.resize((width, height), resample=Image.LANCZOS)
    large_frame.paste(img_small, (x, y))
    # img_small.save(f"{tmpdirname}/{frame:04d}.png")
    # cv2.imwrite(f'{tmpdirname}/{frame:04d}.png', img[:, :, [2, 1, 0]])
    # cv2.imwrite(f'{tmpdirname}/{frame:04d}.png', img[:, :, [2, 1, 0]])
    return img_small


def render_policy(
    env,
    policy,
    frames,
    x,
    y,
    width,
    height,
    noise_process=None,
    frame_skip=2,
    freeze_on_success=True,
    freeze_frames=5,
    freeze_lag=4,
    n_episodes=1,
):
    frame_i = 0
    success = False
    total_reward = 0
    last_img = None
    success_frame = None
    for episode in range(n_episodes):
        if noise_process is not None:
            noise_process.reset()
        observation = env.reset()
        for i in range(env.max_path_length):
            if i % frame_skip == 0:
                if (
                    freeze_on_success
                    and success_frame is not None
                    and frame_i > success_frame + freeze_lag
                ):
                    frame_i += 1
                    if frame_i < len(frames):
                        frames[frame_i].paste(last_img, (x, y))
                else:
                    frame_i += 1
                    if frame_i < len(frames):
                        last_img = render_frame(
                            env, frames[frame_i], x, y, width, height
                        )
            action, agent_info = policy.get_action(observation)
            if noise_process is not None:
                action_noisy = action + noise_process.simulate()
            else:
                action_noisy = action
            next_obs, reward, done, info = env.step(action_noisy)
            success = success | (info.get("success", 0) > 0)
            if success and success_frame is None:
                success_frame = frame_i
            total_reward += reward
            observation = next_obs
            if done:
                break
            if success_frame is not None and frame_i >= success_frame + freeze_frames:
                break
    return frame_i


def render_collage(*, seed=100, out_file):
    np.random.seed(seed)
    env_names = list(MT50_ENV_NAMES)
    np.random.shuffle(env_names)
    env_names_seq = []
    env_names_seq.append(list(env_names))
    frames = [Image.new("RGB", (FRAME_WIDTH, FRAME_HEIGHT)) for _ in range(N_FRAMES)]
    env_i = 0
    current_start_y = 2
    for row_i, row_height in enumerate(tqdm(ROW_HEIGHTS)):
        row_image_width = (row_height * ASPECT_RATIO[0]) // ASPECT_RATIO[1]
        current_start_x = ROW_OFFSETS[row_i]
        while current_start_x < FRAME_WIDTH:
            current_start_frame = 0
            env_j = 0
            while current_start_frame < N_FRAMES:
                while env_j >= len(env_names_seq):
                    np.random.shuffle(env_names)
                    env_names_seq.append(list(env_names))
                env_name = env_names_seq[env_j][env_i]
                env_j += 1
                env = make_env(env_name, seed=seed)
                policy = SawyerUniversalV2Policy(env_name)
                noise_process = GaussianNoiseProcess(dimensions=4)
                current_start_frame += render_policy(
                    env,
                    policy,
                    frames[current_start_frame:],
                    current_start_x,
                    current_start_y,
                    row_image_width,
                    row_height,
                    noise_process=noise_process,
                )
                env.close()
            env_i += 1
            current_start_x += row_image_width + 2
        current_start_y += row_height + 2

    with tempfile.TemporaryDirectory() as tmpdirname:
        for i, frame in enumerate(tqdm(frames)):
            frame.save(f"{tmpdirname}/{i:04d}.png")
        print("Rendering video...")
        run(
            [
                "ffmpeg",
                "-y",
                "-i",
                f"{tmpdirname}/%04d.png",
                "-filter_complex",
                "[0:v] fps=15,scale=w=200:h=-1",
                out_file.replace(".webm", ".gif"),
            ]
        )
        run(["ffmpeg", "-y", "-i", f"{tmpdirname}/%04d.png", out_file])
        print("Done rendering video")


if __name__ == "__main__":
    clize.run(render_collage)