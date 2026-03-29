# Gem-Api-Quizzer-DSA

A command-line tool that generates fresh DSA practice problems on demand using the Google Gemini API — and evaluates your answers with AI feedback.

## What it does

- Asks you which DSA topic you want to practice (arrays, graphs, trees, etc.)
- Generates a unique problem on that topic using Gemini
- Takes your solution approach as input
- Gives you AI feedback on whether your approach is correct and why

## Tech stack

- Python
- Google Gemini API (`google-genai`)
- `python-dotenv` for API key management

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/ParasWadkar/Gem-Api-Quizzer-DSA.git
cd Gem-Api-Quizzer-DSA
```

### 2. Install dependencies

```bash
pip install google-genai python-dotenv
```

### 3. Set up your API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

Get a free API key at [ai.google.dev](https://ai.google.dev)

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

## Why I built this

A personal learning project to practice the eigenskill of reading documentation and building with unfamiliar APIs — while also making DSA prep more interactive. Built as part of my CS self-learning roadmap.

---

Built by [Paras Wadkar](https://github.com/ParasWadkar)