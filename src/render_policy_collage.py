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

FRAME_WIDTH = 1600
FRAME_HEIGHT = 1600

ORIGINAL_FRAME_WIDTH = 800
ORIGINAL_FRAME_HEIGHT = 600

ASPECT_RATIO = (4, 3)
ROW_HEIGHTS = [640, 480, 240, 200, 160, 120, 100, 80, 40]
N_FRAMES = (500 // 2) * 4

assert sum(ROW_HEIGHTS) >= FRAME_HEIGHT


def render_frame(env, large_frame, x, y, width, height):
    img = env.sim.render(
        ORIGINAL_FRAME_WIDTH, ORIGINAL_FRAME_HEIGHT, camera_name="corner4", depth=False
    )
    img = np.flip(img, axis=0)
    img = np.flip(img, axis=1)
    # img = env.render("rgb_array")
    img_to_resize = Image.fromarray(img[:, :, [2, 1, 0]])
    # img_to_resize = Image.fromarray(img[:, :, [0, 1, 2]])
    img_small = img_to_resize.resize((width, height), resample=Image.LANCZOS)
    large_frame.paste(img_small, (x, y))
    # img_small.save(f"{tmpdirname}/{frame:04d}.png")
    # cv2.imwrite(f'{tmpdirname}/{frame:04d}.png', img[:, :, [2, 1, 0]])
    # cv2.imwrite(f'{tmpdirname}/{frame:04d}.png', img[:, :, [2, 1, 0]])
    return frame + 1


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
    freeze_on_success=False,
    n_episodes=1,
):
    frame_i = 0
    success = False
    total_reward = 0
    for episode in range(n_episodes):
        if noise_process is not None:
            noise_process.reset()
        observation = env.reset()
        for i in tqdm(range(env.max_path_length)):
            if i % frame_skip == 0:
                if freeze_on_success and success:
                    raise NotImplementedError()
                    frame_i += 1
                else:
                    frame_i = render_frame(env, frames[frame_i], x, y, width, height)
            action, agent_info = policy.get_action(observation)
            if noise_process is not None:
                action_noisy = action + noise_process.simulate()
            else:
                action_noisy = action
            next_obs, reward, done, info = env.step(action_noisy)
            success = success | (info.get("success", 0) > 0)
            total_reward += reward
            observation = next_obs
            if done:
                break
    return success, total_reward


def render_successful_episode(
    env_name,
    policy_name,
    render_output_dir,
    env,
    policy,
    *,
    noise_process=None,
    frame_skip=2,
    freeze_on_success=False,
    retries=20,
):
    for i in range(retries):
        render_success, _ = render_policy(
            env,
            policy,
            f"{render_output_dir}/{env_name}-{policy_name}-{i}.webm",
            noise_process=noise_process,
            frame_skip=frame_skip,
            freeze_on_success=freeze_on_success,
        )
        if render_success:
            shutil.copy(
                f"{render_output_dir}/{env_name}-{policy_name}-{i}.webm",
                f"{render_output_dir}//{env_name}-{policy_name}-success.webm",
            )
            print(f"Rendered successful episode for {env_name}")
            break
        elif success == 0:
            print(f"Skipping additional renders of {env_name}")
            break
        elif i == 19:
            print(f"Could not render successful episode for {env_name}")


def base():
    agent = CarGoalPController()
    context_sampler = RoundRobinSampler(
        [
            CORNERS["top-left"],
            CORNERS["bottom-left"],
            CORNERS["bottom-right"],
        ]
    )
    env = ContextSamplingEnv(
        CarGoal(
            randomize_starting_angle=True,
            randomize_starting_position=True,
            action_type="raw",
        ),
        sampler=context_sampler,
    )
    render_policy(env, agent, "car-goal-corner_base.webm", n_episodes=4 * 3)


def target():
    agent = CarGoalPController()
    context_sampler = RoundRobinSampler(
        [
            CORNERS["top-right"],
        ]
    )
    env = ContextSamplingEnv(
        CarGoal(
            randomize_starting_angle=False,
            randomize_starting_position=False,
            action_type="raw",
        ),
        sampler=context_sampler,
    )
    render_policy(env, agent, "car-goal-corner_target.webm", n_episodes=1)


def generalization():
    agent = CarGoalPController()
    context_sampler = RoundRobinSampler(
        [
            CORNERS["top-right"],
        ]
    )
    env = ContextSamplingEnv(
        CarGoal(
            randomize_starting_angle=True,
            randomize_starting_position=True,
            action_type="raw",
        ),
        sampler=context_sampler,
    )
    render_policy(env, agent, "car-goal-corner_generalization.webm", n_episodes=12)


def render_collage(*, seed=100, out_file):
    np.random.seed(seed)
    env_names = list(MT50_ENV_NAMES)
    np.random.shuffle(env_names)
    frames = [Image.new("RGB", (FRAME_WIDTH, FRAME_HEIGHT)) for _ in range(N_FRAMES)]
    env_i = 0
    current_start_frame = 0
    while current_start_frame < N_FRAMES:
        current_start_y = 0
        for row_i, row_height in tqdm(enumerate(ROW_HEIGHTS)):
            row_image_width = (row_height * ASPECT_RATIO[0]) // ASPECT_RATIO[1]
            if row_i % 2 == 0:
                current_start_x = 0
            else:
                current_start_x = row_image_width // 2
            while current_start_x < FRAME_WIDTH:
                env_name = env_names[env_i]
                env_i += 1
                print("Creating env")
                env = make_env(env_name, seed=seed)
                policy = SawyerUniversalV2Policy(env_name)
                noise_process = GaussianNoiseProcess(dimensions=4)
                render_policy(
                    env,
                    policy,
                    frames[current_start_frame:],
                    current_start_x,
                    current_start_y,
                    row_image_width,
                    row_height,
                    noise_process=noise_process,
                )
                current_start_x += row_image_width
                print("Closing env")
                env.close()
        current_start_frame += 250
        print("Done with frames up to ", current_start_frame)

    with tempfile.TemporaryDirectory() as tmpdirname:
        for i, frame in enumerate(frames):
            frame.save(f"{tmpdirname}/{i:04d}.png")
        print("Rendering video...")
        run(["ffmpeg", "-y", "-i", f"{tmpdirname}/%04d.png", out_file])
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
        print("Done rendering video")


if __name__ == "__main__":
    clize.run(render_collage)
