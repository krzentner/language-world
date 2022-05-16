import hashlib
import random
import os

ENGINE_SYNONYMS = {
    'gpt3': 'text-davinci-002',
}


def hash_str(s: str) -> str:
    return hashlib.sha1(s.encode('utf-8')).digest().hex()


def get_prompt_cache_dir(*, engine: str, prompt: str) -> str:
    h = hash_str(prompt)
    try:
        cache_engines = os.listdir('cache')
    except FileNotFoundError as e:
        raise Exception('Must be run from project root directory') from e
    if engine not in cache_engines:
        raise Exception(f'Engine {engine!r} not found in cache')
    return f'cache/{engine}/{h}/'

def cache_lookup(*, engine: str, prompt: str) -> [str]:
    cache_dir = get_prompt_cache_dir(engine=engine, prompt=prompt)
    try:
        filesnames = os.listdir(cache_dir)
    except FileNotFoundError:
        return []
    results = []
    for filename in filesnames:
        if filename.endswith('out.txt'):
            with open(f'{cache_dir}/{filename}') as f:
                results.append(f.read())
    return results


def cache_write(*, engine: str, prompt: str, response: str):
    cache_dir = get_prompt_cache_dir(engine=engine, prompt=prompt)
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
        with open(f'{cache_dir}/in.txt', 'w') as f:
            f.write(prompt)
    response_h = hash_str(response)
    with open(f'{cache_dir}/{response_h}.out.txt', 'w') as f:
        f.write(response)


def run_prompt(prompt: str, engine: str = 'gpt3',
               skip_cache: bool = False) -> str:
    if not prompt.endswith('\n'):
        prompt = prompt + '\n'
    engine = ENGINE_SYNONYMS.get(engine, engine)

    if not skip_cache:
        results = cache_lookup(engine=engine, prompt=prompt)
        if results:
            return random.choice(results)

    if engine == 'text-davinci-002':
        import gpt3
        response = gpt3.run_prompt(prompt)
    else:
        raise Exception(f'Unknown engine {engine}')

    cache_write(engine=engine, prompt=prompt, response=response)
    return response


def past_tense_to_capability(past_tense: str, **kwargs):
    cap_lines = []
    for line in past_tense.split('\n'):
        assert '\n' not in line
        cap_lines.append(run_prompt(
            'Past tense:\nI opened a jar.\n'
            'Skill:\nI can open a jar.\n'
            'Past tense:\n' + line + '\n'
            'Skill:\n'))
    return cap_lines
