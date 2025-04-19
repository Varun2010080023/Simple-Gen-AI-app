# 🧠 Simple Ollama GenAI Project

Run powerful open-source LLMs locally using **Ollama**. This project demonstrates how to install Ollama, pull models, and generate responses using a simple Python script.

---

## ⚙️ Setup Instructions

### ✅ Step 1: Install Ollama

Download and install from the official site:

```bash
https://ollama.com/download
Follow the instructions for your OS (macOS, Windows, or Linux).

✅ Step 2: Pull a Model
Choose and pull a model:

bash
Copy
Edit
ollama pull llama2
Other options:

bash
Copy
Edit
ollama pull mistral
ollama pull gemma
ollama pull codellama
ollama pull orca-mini
✅ Step 3: Run the Model in CLI
bash
Copy
Edit
ollama run llama2
Once it loads, type your prompt:

text
Copy
Edit
> Explain quantum computing in simple terms.
✅ Step 4: Generate Responses with Python
Install Required Package:
bash
Copy
Edit
pip install requests
main.py:
python
Copy
Edit
# main.py

import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama2",
        "prompt": "Write a short story about a robot who wants to learn music."
    }
)

print(response.json()["response"])
requirements.txt:
txt
Copy
Edit
requests
🔍 Ollama Model Highlights

Model	Description	Use Case
llama2	Meta's open-source LLM with strong performance	General purpose tasks
mistral	Lightweight and fast with competitive output	Chat, summaries, Q&A
gemma	Google's open LLM with great reasoning	Technical answers
codellama	Fine-tuned for code generation and completion	Programming assistant
orca-mini	Small instruction-following model	Simple AI assistant
🧰 Common Ollama Commands
bash
Copy
Edit
# Pull a new model
ollama pull mistral

# Run a model interactively
ollama run mistral

# Show installed models
ollama list

# Delete a model
ollama delete gemma
📂 Project Structure
plaintext
Copy
Edit
ollama-genai-project/
├── main.py
├── requirements.txt
└── README.md
✅ Example Output
Running the main.py script might return:

text
Copy
Edit
Once upon a time, in a quiet lab, a curious robot named Echo discovered an old piano...
📄 License
MIT License

🙌 Credits
Made with 💡 using Ollama and open-source LLMs.

vbnet
Copy
Edit

Let me know if you want this exported as a file or turned into a GitHub-ready project template too!







