# Language-World

A language and robotics benchmark based on [Meta-World](https://github.com/Farama-Foundation/Metaworld).

Language-World is packaged as a set of small tools which process Meta-World observations.
Wrapping Meta-World environments directly is left up to the user.
To avoid confusion, please always use the goal-observable, randomized goal and initial state variation of Meta-World (MT50-rand), and always sample length 500 episodes.
If you choose not to, please prominently document what configuration you used instead.

Language-World can be installed via pypi:

```
pip install language-world==0.1.1
```

Or directly from the git repo
```
pip install git+https://github.com/krzentner/language-world.git@v0.1.1
```

You will also need to install a version of Meta-World. language-world should work will all versions of Meta-World with at least v2 environments.

Alternatively, copy [this file](./src/language_world/__init__.py) into your project.

Language-World consists of three main components:

First, a set of natural language task descriptions available as a dictionary: `language_world.TASK_DESCRIPTIONS: dict[str, str]`

Second, a set of "scripted skills," that can be used to solve MT10 (and also function in other tasks).

`language_world.SCRIPTED_SKILL_NAMES: list[str]` lists the names of all scripted skills.
`language_world.run_scripted_skill(skill_name: str, obs: np.ndarray) -> np.ndarray` produces an action given a skill name and observation.

Thirdly, a query answering function:

```
language_world.eval_queries(task_name: str, queries: List[str],
                            obs: np.ndarray, fuzzy: bool=False)
```

The query answering function can evaluate a large number of queries.
Enabling the `fuzzy` flag will map unsupported queries to the nearest supported queries using string edit distance.

`language_world.enumerate_base_queries(task_name: str) -> list[str]` provides a list of the "base" queries for a task (i.e. those that do not contain conjunctions).

`language_world.enumerate_all_queries(task_name: str) -> list[str]` provides a list of all queries for a task.
