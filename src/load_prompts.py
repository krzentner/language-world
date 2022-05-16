import os

def parse_prompt(prompt: str) -> {str: [str]}:
    output = {}
    sections = [section.split('\n') for section in prompt.split('#')]
    return {lines[0].strip(): [line.strip() for line in lines[1:] if line]
            for lines in sections if lines[0].strip()}

def prompts() -> {int: {str: [str]}}:
    results = {}
    for filename in os.listdir('prompts'):
        assert filename.endswith('.md')
        index = int(filename.split('.')[0])
        with open(f'prompts/{filename}') as f:
            results[index] = parse_prompt(f.read())
    return results
