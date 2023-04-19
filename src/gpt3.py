import os
import openai
from dotenv import load_dotenv
import clize

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def run_prompt(prompt: str, engine: str = "text-davinci-002") -> str:
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.7,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0.01,
        presence_penalty=0.01,
    )
    return response.choices[0].text


def main(infile: str, outfile: str, *, engine: str = "text-davinci-002"):
    print("Using engine:", engine)
    with open(infile) as f:
        prompt = f.read()
    result = run_prompt(prompt, engine=engine)
    print(result)
    print("writing to", repr(outfile))
    with open(outfile, "w") as f:
        f.write(result)


if __name__ == "__main__":
    clize.run(main)
