def format_prompt(prompt: {str: [str]}) -> str:
    return '\n'.join(prompt['Task'] + prompt['Context'] + prompt.get('Response', []))

def format_request(base_promts: [{str: [str]}], target_prompt: {str: [str]}):
    target_prompt_no_reponse = {key: val for (key, val) in target_prompt.items()
                                if key != 'Response'}
    return '\n\n'.join([format_prompt(prompt)
                        for prompt in base_promts + [target_prompt_no_reponse]])
