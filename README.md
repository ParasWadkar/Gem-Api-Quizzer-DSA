# Gem-Api-Quizzer-DSA

A command-line tool to create new DSA practice problems on the fly using the Google Gemini API and get AI-powered feedback on your answers.

## What it does

- Asks you to choose a DSA topic you want to practice
- Creates a new problem for you on the topic you chose using the Google Gemini API
- Asks you for your solution strategy
- Provides you with AI-powered feedback on whether your strategy is correct or not

## Tech used

- Python
- Google Gemini API
- `google-genai` API client
- `python-dotenv` for API keys

## How to use

### Step 1: Clone this repo

```bash
git clone https://github.com/ParasWadkar/Gem-Api-Quizzer-DSA.git
cd Gem-Api-Quizzer-DSA
```

### Step 2: Install the required packages

```bash
pip install google-genai python-dotenv
```

### Step 3: Configure your API key

Create a `.env` file in the project directory with the following content:

```
GEMINI_API_KEY=your_api_key
```

Get a free API key at [aistudio.google.com](https://aistudio.google.com/)

### 4. Run it

```bash
python main.py
```

## Project structure

```
Gem-Api-Quizzer-DSA/
├── main.py        # Main application
├── .env           # Your API key (never committed)
├── .gitignore     # Keeps .env off GitHub
└── README.md
```

## What led me to make this

This project was built on the idea of an **eigenskill**, a skill that has such an impact on the development of every other skill you have, that when you apply that eigenskills to every other one, they become better (or "amplified").

The challenge I gave to myself was to build something real by only reading the official Google Gemini API documentation. No tutorials, and no help from anyone else, just me trying to learn how to use the Google Gemini API by reading the documentation.

Here's what I learned during this project:
- How to read and navigate through the official API documentation.
- How to use Python to call an API and handle the real response you get from the API.
- How to store an API key in an environment variable and read it within your program.
- How to debug an error by reading what the error says.
- How to connect your `.env` file and a library to build a working program that includes your own custom code.

I decided to explore DSA as a subject, because I'm currently studying the subject, so this is a practical application that will help me learn more about DSA.
---

Built by [Paras Wadkar](https://github.com/ParasWadkar)