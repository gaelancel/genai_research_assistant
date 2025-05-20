import os, openai

from openai import OpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def generate_ideas(problem_description: str, n: int = 3) -> list[str]:
    """
    Uses the OpenAI client to generate a list of research ideas
    for the given problem.
    """
    # Use of AI for description
    prompt = (
        f"Please brainstorm exactly {n} distinct research ideas to address the following problem:\n"
        f"\"{problem_description}\"\n\n"
        "Number them 1 to {n}, and give each a one-sentence description."
    )
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )
    content = resp.choices[0].message.content.strip()
    lines = content.splitlines()
    ideas = [line.lstrip("0123456789. - ").strip() for line in lines if line.strip()]
    return ideas


def assess_novelty(idea: str) -> str:
    """
    Uses the OpenAI client to assess the novelty of a research idea.
    Returns a brief assessment indicating whether the idea is highly novel,
    somewhat novel, or overlaps with existing work.
    """
    # Use of AI for description
    prompt = (
        f"Assess the novelty of the following research idea:\n\n"
        f"\"{idea}\"\n\n"
        "Based on your knowledge of existing literature up to today (visit websites like arXiv), "
        "indicate whether this idea is:\n"
        "- Highly novel (unlikely to have been explored before)\n"
        "- Somewhat novel (related work exists but this extends it)\n"
        "- Overlaps with existing work (well-studied area)\n\n"
        "Provide a one- or two-sentence justification for your assessment."
    ) # Use of AI for prompt engineering
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()


def suggest_experiment(idea: str, n: int = 3) -> str:
    """
    Uses OpenAI API to suggest a potential experiment or validation for the idea.
    """
    # Use of AI for description
    prompt = (f"The idea is: \"{idea}\"\nSuggest {n} concrete experiments or studies to test this idea's viability.")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def display_results(results: list):
    """
    Prints the ideas with their novelty assessment and experiment suggestion in a formatted manner.
    """
    # Use of AI for description
    for idx, (idea, novelty, experiments) in enumerate(results, start=1):
        print(f"\n\n**Idea {idx}:** {idea}")
        print(f"\n- **Novelty:** {novelty}")
        print(f"\n- **Experiment:** {experiments}\n\n")
