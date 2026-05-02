# TravellerAI — Your Personal AI Travel Planner

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)
![Tavily](https://img.shields.io/badge/Tavily_Search-0EA5E9?style=for-the-badge&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Logfire](https://img.shields.io/badge/Logfire-6C47FF?style=for-the-badge&logoColor=white)
![DeepEval](https://img.shields.io/badge/DeepEval-00B4D8?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge)

An agentic AI application that generates detailed, personalised day-by-day travel itineraries using a **Groq-powered Llama 3.3 70B** model augmented with **real-time web search** via Tavily. Users provide their destination, trip duration, interests, travel style, pace, and preferred month — the agent handles the rest.

---

## Features

- **Real-time information** — the agent searches the web via Tavily before writing itineraries, ensuring up-to-date recommendations.
- **Fully personalised** — inputs for interests, travel style (Budget / Luxury / Adventure / Cultural / Relaxation), pace, and month of travel.
- **Day-by-day structure** — detailed schedule including places, dining, local customs, travel advisories, and budget estimates.
- **Observability** — Logfire integration tracks every LLM call; DeepEval support for offline evaluation.
- **Production-grade internals** — structured logging, custom exceptions with full traceback context, and clean config management.

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Groq — `llama-3.3-70b-versatile` |
| Orchestration | LangChain (langchain, langchain-core, langchain-community) |
| LLM Provider SDK | langchain-groq |
| Search | Tavily (langchain-tavily), Google Serper (standby) |
| UI | Streamlit |
| Config | python-dotenv |
| Validation | Pydantic |
| Observability | Logfire |
| Evaluation | DeepEval |
| Packaging | setuptools |

---

## Project Structure

```
TravellerAI/
│
├── app.py                        # Streamlit entry-point — renders the form UI, collects user inputs, and displays the generated itinerary
├── requirements.txt              # All Python dependencies
├── setup.py                      # Package metadata and install configuration
├── .env                          # API keys (GROQ, TAVILY, SERPER) — never committed
├── .gitignore                    # Ignores venvs, __pycache__, .env, Reports/, experiments/
├── LICENSE                       # Apache 2.0
│
├── src/                          # Core application package
│   ├── __init__.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   └── travel_agent.py       # Constructs the LangChain ReAct agent with Llama 3.3 70B on Groq and binds the Tavily search tool
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py             # Loads and exposes GROQ_API_KEY, TAVILY_API_KEY, and SERPER_API_KEY from the .env file
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── planner.py            # TravelPlanner class — builds the structured prompt, manages message history, invokes the agent, and returns the final itinerary string
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── tavily_tool.py        # Wraps Tavily Search API as a LangChain tool; returns up to 5 results per query
│   │   └── serper_tool.py        # Google Serper search wrapper (standby — not wired into the active agent)
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py             # Configures a daily rotating file logger writing to logs/log_YYYY-MM-DD.log
│       └── custom_exception.py   # CustomException that captures filename, line number, and traceback for structured error reporting
│
├── logs/
│   └── log_YYYY-MM-DD.log        # Auto-generated daily log files
│
├── experiments/
│   └── experiment.ipynb          # Jupyter notebook for exploratory development and prompt testing
│
└── Reports/
    ├── GITHUB LINK.txt
    ├── NOTES/
    │   ├── Notes.png
    │   └── travel_notes.excalidraw
    └── Project report/
        └── AI_Powered_Travel_Itinerary_Planner_Report.docx
```

---

## Architecture

```
User (Streamlit UI)
        │
        ▼
   app.py  ──────────────────────────────────────────────────────────┐
        │                                                             │
        ▼                                                             │
 TravelPlanner.create_itinerary()                                     │
   (src/core/planner.py)                                              │
        │  builds prompt + message history                            │
        ▼                                                             │
 travel_agent  (LangChain ReAct Agent)                                │
   (src/agents/travel_agent.py)                                       │
        │  Groq — llama-3.3-70b-versatile                            │
        │                                                             │
        ├──── Tool call ──────────────────────────────────────────┐  │
        │                                                          │  │
        ▼                                                          ▼  │
 tavily_search_tool()                                    Logfire Observability
   (src/tools/tavily_tool.py)                                         │
   Real-time web results                                              │
        │                                                             │
        └──────────── Response assembled ─────────────────────────►  │
                                                                      │
                                                    Itinerary rendered│
                                                    in Streamlit UI ◄─┘
```

---

## Getting Started

### 1. Clone & install

```bash
git clone https://github.com/Sir-Sloth-The-Lazy/TravellerAI.git
cd TravellerAI
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API keys

Create a `.env` file in the project root:

```env
GROQ_API_KEY   = "your_groq_api_key"
TAVILY_API_KEY = "your_tavily_api_key"
SERPER_API_KEY = ""          # optional, not active
```

Get your keys:
- Groq — https://console.groq.com
- Tavily — https://app.tavily.com

### 3. Run

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Configuration

All runtime configuration is managed through environment variables loaded by [src/config/config.py](src/config/config.py):

| Variable | Required | Description |
|---|---|---|
| `GROQ_API_KEY` | Yes | API key for the Groq LLM endpoint |
| `TAVILY_API_KEY` | Yes | API key for Tavily web search |
| `SERPER_API_KEY` | No | Google Serper key (standby tool) |

---

## Key Modules

### [`src/core/planner.py`](src/core/planner.py)
`TravelPlanner` is the orchestration layer. It assembles a structured natural-language prompt from all user parameters, maintains a `HumanMessage`/`AIMessage` conversation history, invokes the agent, and returns the final itinerary text.

### [`src/agents/travel_agent.py`](src/agents/travel_agent.py)
Builds a LangChain ReAct agent using `create_react_agent`. The system prompt instructs the model to always call the search tool for destination-specific information before writing, and to include day-by-day breakdowns with dining, budget ranges, local customs, and advisories.

### [`src/tools/tavily_tool.py`](src/tools/tavily_tool.py)
A thin LangChain tool wrapper around `TavilySearch`. Configured with `max_results=5` and `topic="general"`. This is the agent's only active tool.

### [`src/utils/logger.py`](src/utils/logger.py)
Creates `logs/` if absent, then returns a named logger configured to write `INFO`-level lines in `asctime - levelname - message` format to a date-stamped file.

### [`src/utils/custom_exception.py`](src/utils/custom_exception.py)
`CustomException` enriches any caught exception with the source filename and line number extracted from `sys.exc_info()`, making log entries self-contained without needing a full traceback dump.

---

## License

Distributed under the [Apache License 2.0](LICENSE).
