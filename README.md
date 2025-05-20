# GenAI Research Assistant

A lightweight AI assistant for research and development. Given a natural-language problem description, it:

* Generates research ideas via OpenAI’s GPT.
* Assesses each idea’s novelty using the model’s knowledge.
* Suggests experiments to validate each idea.

---

## Setup & Installation

1. **Install `pip-tools` (once):**

   ```bash
   pip install pip-tools
   ```

2. **Compile dependencies:**

   From the project root directory (where `requirements.in` lives), run:

   ```bash
   pip-compile requirements.in
   ```

   This produces a `requirements.txt` with resolved, lock-file versions.

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key:**

   Create a `.env` file in the project root and add:

   ```bash
   OPENAI_API_KEY=sk-<your-key-here>
   ```

---

## Usage

### Command-line Interface

Run the main entrypoint and enter your research problem when prompted:

```bash
python main.py
```

**Example:**

```bash
$ python main.py
Enter your research problem description: Develop a method to improve battery life in IoT devices using machine learning.

Idea 1: Adaptive power-management model...
  • Novelty: Somewhat novel (related work exists)...
  • Experiment: Simulate an IoT network...

...etc.
```

---

Enjoy brainstorming and validating new research ideas with this GenAI-powered assistant!
