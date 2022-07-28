import numpy as np
import re
from pprint import pprint
import pickle
import shutil
from os.path import expanduser
import dbm.gnu
from tqdm import tqdm
import tensorflow as tf

EMBEDDER = None # hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")


def get_embedder():
  global EMBEDDER
  if EMBEDDER is None:
    import tensorflow_hub as hub
    EMBEDDER = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
  return EMBEDDER


MT10_INSTRUCTIONS = """
def close_drawer(robot):
  # For a robot to close a drawer, it needs to push the drawer closed using the drawer handle.
  if check("the robot's gripper is around the drawer handle"):
    robot.push_gripper("forward into the drawer")
  # To push the drawer closed using the drawer handle, it needs to grip the drawer handle.
  if check("the robot's gripper is around the drawer handle"):
    robot.close_gripper()
  # To grip the drawer handle, it needs to put its gripper around the handle.
  # To put its gripper around the drawer handle, it needs to move the gripper down around the drawer handle from above.
  if check("the robot's gripper is above the drawer handle"):
    robot.move_gripper("down into the drawer handle")
  # To move the gripper down around the handle from above, the gripper needs to first be above the drawer handle.
  if check("the robot's gripper is not near the drawer handle"):
    robot.move_gripper("up above the drawer handle")

def open_drawer(robot):
  # For a robot to open a drawer, it needs to pull the drawer open using the drawer handle.
  if check("the robot's gripper is around the drawer handle"):
    robot.pull_gripper("forward out of the drawer")
  # To pull the drawer open using the drawer handle, it needs to grip the drawer handle.
  if check("the robot's gripper is around the drawer handle"):
    robot.close_gripper()
  # To grip the drawer handle, it needs to put its gripper around the handle.
  # To put its gripper around the drawer handle, it needs to move the gripper down around the drawer handle from above.
  if check("the robot's gripper is above the drawer handle"):
    robot.move_gripper("down into the drawer handle")
  # To move the gripper down around the handle from above, the gripper needs to first be above the drawer handle.
  if check("the robot's gripper is not near the drawer handle"):
    robot.move_gripper("up above the drawer handle")

def open_door(robot):
  # For a robot to open a door, it needs to push the door open using the door handle.
  if check("the robot's gripper is around the door handle"):
    robot.push_gripper("forward into the door")
  # To push the door open using the door handle, it needs to grip the door handle.
  if check("the robot's gripper is around the door handle"):
    robot.close_gripper()
  # To grip the door handle, it needs to put its gripper around the handle.
  # To put its gripper around the door handle, it needs to move the gripper down around the door handle from above.
  if check("the robot's gripper is above the door handle"):
    robot.move_gripper("down into the door handle")
  # To move the gripper down around the handle from above, the gripper needs to first be above the door handle.
  if check("the robot's gripper is not near the door handle"):
    robot.move_gripper("up above the door handle")

def pick_puck_and_hold_at_target(robot):
  # To hold a puck at a target, the robot needs to hold the puck in its gripper.
  if check("the robot is holding a puck"):
    robot.move_gripper("forward to the target")
  # To hold a puck in its gripper, it needs to grip the puck.
  if check("the robot's gripper is around the puck"):
    robot.close_gripper()
  # To grip the puck, it needs to put its gripper around the puck.
  # To put its gripper around the puck, it needs to move the gripper down around the puck from above.
  if check("the robot's gripper is above the puck"):
    robot.move_gripper("down into the puck")
  # To move the gripper down around the puck from above, the gripper needs to first be above the puck.
  if check("the robot's gripper is not near the puck"):
    robot.move_gripper("up above the puck")

def press_button_from_above(robot):
  # To press a button from above, the robot needs to push its gripper down onto the button.
  if check("the robot's gripper is above the button"):
    robot.move_gripper("down onto the button")
  # To push its gripper down onto the button, the gripper needs to first be above the button.
  if check("the robot's gripper is not near the button"):
    robot.move_gripper("up above the button")

def slide_puck_to_target(robot):
  # To slide a puck to a target, the robot needs to push the puck to the target.
  if check("the robot is holding a puck"):
    robot.push_gripper("forward to the target")
  # To push the puck to the target, it needs to grip the puck.
  if check("the robot's gripper is around the puck"):
    robot.close_gripper()
  # To grip the puck, it needs to put its gripper around the puck.
  # To put its gripper around the puck, it needs to move the gripper down around the puck from above.
  if check("the robot's gripper is above the puck"):
    robot.move_gripper("down into the puck")
  # To move the gripper down around the puck from above, the gripper needs to first be above the puck.
  if check("the robot's gripper is not near the puck"):
    robot.move_gripper("up above the puck")

def insert_peg_right_into_slot(robot):
  # To insert a peg into a slot, the robot needs to push the peg into the slot.
  if check("the robot is holding a peg"):
    robot.push_gripper("right into the slot")
  # To push the peg into the slot, it needs to grip the peg.
  if check("the robot's gripper is around the peg"):
    robot.close_gripper()
  # To grip the peg, it needs to put its gripper around the peg.
  # To put its gripper around the peg, it needs to move the gripper down around the peg from above.
  if check("the robot's gripper is above the peg"):
    robot.move_gripper("down into the peg")
  # To move the gripper down around the peg from above, the gripper needs to first be above the peg.
  if check("the robot's gripper is not near the peg"):
    robot.move_gripper("up above the peg")

def slide_window_open_left(robot):
  # To slide open a window that opens to the left, the robot needs to push the window handle left.
  # To push the window handle left, the robot's gripper needs to be right of the window handle.
  if check("the robot's gripper is right of the window handle"):
    robot.push_gripper("left to edge of window")
  # To put the gripper right of the window handle, the robot's gripper needs to be moved there.
  if check("the robot's gripper is not right of the window handle"):
    robot.move_gripper("right of the window handle")

def slide_window_closed_right(robot):
  # To slide close a window that opens to the right, the robot needs to push the window handle right.
  # To push the window handle right, the robot's gripper needs to be left of the window handle.
  if check("the robot's gripper is left of the window handle"):
    robot.push_gripper("right to edge of window")
  # To put the gripper left of the window handle, the robot's gripper needs to be moved there.
  if check("the robot's gripper is not left of the window handle"):
    robot.move_gripper("left of the window handle")

def reach_for_target(robot):
  # To reach for a target, the robot needs to move its gripper to the target.
  if check("the robot's gripper is not near the target"):
    robot.move_gripper("to the target")
"""

FN_NAME = re.compile(r'def ([a-zA-Z_]+)\(')
CONDITIONS_CONSEQUENCES = re.compile(r'if check\("([^"]+)"\):\s+robot.([^\n]+)\s+', flags=re.MULTILINE)

def embed_mt10():
  MT10_PROMPTS = re.compile("(?=def)").split(MT10_INSTRUCTIONS)

  mt10_embedded = {}
  for prompt in MT10_PROMPTS:
    names = FN_NAME.findall(prompt)
    if names:
      name = names[0]
      conds_consequences = CONDITIONS_CONSEQUENCES.findall(prompt)
      cond_actions = parse_condition_consequences(conds_consequences)
      pprint(cond_actions)
      cond_action_embeds = []
      for (cond, action) in cond_actions:
        cond_embed = np.asarray(get_embedder()([cond]))
        action_embed = np.asarray(get_embedder()([action]))
        cond_action_embeds.append({
            'cond': cond,
            'action': action,
            'action_embed': action_embed,
            'cond_embed': cond_embed,
        })
      mt10_embedded[name] = cond_action_embeds
  return mt10_embedded


MOVE_GRIPPER = re.compile(r'move_gripper\("([^"]+)"\)')
PUSH_GRIPPER = re.compile(r'push_gripper\("([^"]+)"\)')

def preprocess_condition(cond):
  return cond
  # return f"Is it true that {cond}?"

def parse_condition_consequences(con_con):
  conditional_actions = []
  for (condition, consequence) in con_con:
    action = ""
    if consequence == 'close_gripper()':
      action = "Close the robot's gripper."
    if consequence == 'open_gripper()':
      action = "Open the robot's gripper."
    move_targets = MOVE_GRIPPER.findall(consequence)
    if move_targets:
      action = f"Move the robot's gripper {move_targets[0]}."
    push_targets = PUSH_GRIPPER.findall(consequence)
    if push_targets:
      action = f"Push the robot's gripper {push_targets[0]}."
    conditional_actions.append((preprocess_condition(condition), action))
  return conditional_actions


# try:
  # EMBEDDING_DB = dbm.open(expanduser('~/data/embedding_cache'), 'c')
# except Exception:
  # EMBEDDING_DB = {}

# print('Initializing embedding_db')
# for (k, v) in tqdm(EMBEDDING_CACHE.items()):
  # EMBEDDING_DB[k] = pickle.dumps(v)
# print('Initializing embedding_db')

EMBEDDING_CACHE = {}
UNFLUSHED_VALUES = []

def load_cache():
  print('Loading embedding cache')
  embedding_db = dbm.gnu.open(expanduser('~/data/embedding_cache.db'), 'c')
  key = embedding_db.firstkey()
  while key is not None:
    value = pickle.loads(embedding_db[key])
    if isinstance(value, np.ndarray):
      EMBEDDING_CACHE[key.decode('utf-8')] = value
    key = embedding_db.nextkey(key)
  print('Done loading embedding cache')

load_cache()

def save_cache():
  print('Saving cache')
  with open(expanduser('~/data/embedding_cache.pkl.tmp'), 'wb') as f:
    pickle.dump(EMBEDDING_CACHE, f)
  shutil.move(expanduser('~/data/embedding_cache.pkl.tmp'),
              expanduser('~/data/embedding_cache.pkl'))
  embedding_db = dbm.open(expanduser('~/data/embedding_cache.db'), 'c')
  global UNFLUSHED_VALUES
  UNFLUSHED_VALUES, need_write = [], UNFLUSHED_VALUES
  for (key, value) in need_write:
    embedding_db[key] = pickle.dumps(value)

print('Loading embedding cache')
try:
  with open(expanduser('~/data/embedding_cache.pkl'), 'rb') as f:
    EMBEDDING_CACHE = pickle.load(f)
except FileNotFoundError:
  print("Could not load embedding cache")
print('Done loading embedding cache')


def embed_condition(cond):
  if cond in EMBEDDING_CACHE:
    return EMBEDDING_CACHE[cond]
  else:
    embed = np.array(get_embedder()([preprocess_condition(cond)])[0])
    EMBEDDING_CACHE[cond] = embed
    UNFLUSHED_VALUES.append((cond, pickle.dumps(embed)))
    if len(UNFLUSHED_VALUES) > 100000:
      save_cache()
    return embed

def embed_action(action):
  if action in EMBEDDING_CACHE:
    return EMBEDDING_CACHE[action]
  else:
    print('cache miss')
    embed = np.array(get_embedder()([action])[0])
    EMBEDDING_CACHE[action] = embed
    UNFLUSHED_VALUES.append((action, pickle.dumps(embed)))
    if len(UNFLUSHED_VALUES) > 100000:
      save_cache()
    return embed

if __name__ == '__main__':
  import pickle
  embedded = embed_mt10()
  pprint(embedded)
  with open('data/embedded_mt10.pkl', 'wb') as f:
    pickle.dump(embedded, f)
