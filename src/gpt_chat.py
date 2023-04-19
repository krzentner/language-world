import os
import openai
from dotenv import load_dotenv
import clize

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def run_prompt(prompt: str, model: str = "gpt-3.5-turbo", *, n_outputs):
    messages = [
        {"role": "system", "content": "You are a helpful and creative assistant."},
        {"role": "user", "content": prompt},
    ]
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1.0,
        n=n_outputs,
    )
    return [choice.message["content"] for choice in completion.choices]


def main(
    infile: str, outfile_template: str, *, model: str = "gpt-3.5-turbo", n_outputs: int
):
    print("Using model:", model)
    with open(infile) as f:
        prompt = f.read()
    results = run_prompt(prompt, model=model, n_outputs=n_outputs)
    for i, result in enumerate(results):
        print(result)
        with open(outfile_template.format(i=i), "w") as f:
            f.write(result)


if __name__ == "__main__":
    clize.run(main)
