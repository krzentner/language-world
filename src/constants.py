# No imports here >:)

MT50_ENV_NAMES = [
    "assembly",
    "basketball",
    "bin-picking",
    "box-close",
    "button-press-topdown",
    "button-press-topdown-wall",
    "button-press",
    "button-press-wall",
    "coffee-button",
    "coffee-pull",
    "coffee-push",
    "dial-turn",
    "disassemble",
    "door-close",
    "door-lock",
    "door-open",
    "door-unlock",
    "hand-insert",
    "drawer-close",
    "drawer-open",
    "faucet-open",
    "faucet-close",
    "hammer",
    "handle-press-side",
    "handle-press",
    "handle-pull-side",
    "handle-pull",
    "lever-pull",
    "peg-insert-side",
    "pick-place-wall",
    "pick-out-of-hole",
    "reach",
    "push-back",
    "push",
    "pick-place",
    "plate-slide",
    "plate-slide-side",
    "plate-slide-back",
    "plate-slide-back-side",
    "peg-unplug-side",
    "soccer",
    "stick-push",
    "stick-pull",
    "push-wall",
    "reach-wall",
    "shelf-place",
    "sweep-into",
    "sweep",
    "window-open",
    "window-close",
]

MT10_ENV_NAMES = [
    "reach",
    "push",
    "pick-place",
    "door-open",
    "drawer-open",
    "drawer-close",
    "button-press-topdown",
    "peg-insert-side",
    "window-open",
    "window-close",
]

MT40_ENV_NAMES = []
for env_name in MT50_ENV_NAMES:
    if env_name not in MT10_ENV_NAMES:
        MT40_ENV_NAMES.append(env_name)

GPT3_ENGINES = [
    # "text-babbage-001",
    # "text-curie-001",
    "text-davinci-003",
]

GPT_CHAT_MODELS = [
    # "gpt-4",
    "gpt-3.5-turbo"
]

PLAN_ENCODINGS = [
    "basic_py",
    "chain_py",
    "goal_py",
    "basic_py_md",
    "chain_py_md",
    "goal_py_md",
    "basic_md",
    "chain_md",
    "goal_md",
]

LLM_ATTEMPTS = 5

MODEL_SHORT_NAMES = {
    "text-davinci-003": "GPT 3",
    "gpt-3.5-turbo": "GPT 3.5",
    "ulm340b": "PaLM 2",
    "codepoet24b": "PaLM Code",
}

GOOGLE_LLMS = [
    "ulm340b",
    "codepoet24b",
]
