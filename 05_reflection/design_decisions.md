# 🧩 Design Decisions

## 1. Modular Architecture
The project is divided into independent agent modules — `SearchAgent` and `AnalysisAgent` — promoting separation of concerns and reusability.

## 2. Model and Search Technology Selection
Two core technologies were deliberately chosen to balance autonomy and real-time intelligence:

- **Ollama** was selected as the **local inference engine**, replacing reliance on external APIs such as OpenAI’s ChatGPT.  
  This decision ensures:
  - Full **offline operation** and privacy of data.  
  - **Low latency** inference through local CPU/GPU execution.  
  - Flexibility to switch between models (e.g., `llama3`, `mistral`, `phi`) without code refactoring.  

- **Tavily Search** was adopted as the **web intelligence layer** powering the `SearchAgent`.  
  It provides curated, structured web search results ideal for extracting trends and insights, allowing the system to remain lightweight and avoid scraping complexity.

Together, these choices enable the system to perform **real-time, explainable market intelligence** tasks while maintaining **full deployment control** and **no dependency on proprietary APIs**.

