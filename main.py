import os
from dotenv import load_dotenv
load_dotenv()
from research_assistant import generate_ideas, assess_novelty, suggest_experiment, display_results


def main():
    problem = input("Enter your research problem description: ")
    # Current image generation models often struggle with accurately generating hands. How could I go about improving these models to fix this?
    # Current high-performance chips for running AI models i.e. GPUs, TPUs consume a large amount of power. What are some potential research ideas for building chips with similar computational capability but lower power consumption?
    # Develop a method to improve battery life in IoT devices using machine learning.
    ideas = generate_ideas(problem, n=3)

    results = []
    for idea in ideas:
        novelty = assess_novelty(idea)
        experiment = suggest_experiment(idea)
        results.append((idea, novelty, experiment))

    display_results(results)

if __name__ == "__main__":
    main()
