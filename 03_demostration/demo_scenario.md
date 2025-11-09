# Multi-Agent Demo Scenario: Global Consumer Trends 2025

## 🎯 Objective
Demonstrate how two cooperating agents — `SearchAgent` and `AnalysisAgent` — work together to gather and interpret real-world market intelligence.

The scenario showcases:
- Web data retrieval using the `SearchAgent`
- Analytical summarization using the `AnalysisAgent`
- Structured execution logging for traceability (`execution_log.txt`)

---

## 🏗️ System Overview

### **1. SearchAgent**
- Uses a web search tool (Tavily API)
- Fetches the most relevant documents and summaries for a given query  
- Logs retrieved sources and timing metrics  
- Outputs a concise overview of major findings

### **2. AnalysisAgent**
- Consumes the `SearchAgent` summary  
- Performs semantic analysis and highlights:
  - Key emerging consumer patterns  
  - Sector-specific innovations  
  - Regional differences  
  - Cross-year trend comparisons  
- Generates a structured insight summary.

### **3. Logging & System Info**
- The system logs are configured via `logging.basicConfig()`  
- Execution events are written both to console and `execution_log.txt`  
- Hardware and environment information are collected using:
  ```python
  import platform, psutil, pkg_resources
  ```
  to record system specs, Python version, and library dependencies.

---

## 📊 Example Output Summary (Excerpt)

```
Top 2025 Consumer Trends:
1. AI-driven personalization in retail experiences
2. Sustainable and circular consumption models
3. The rise of hybrid digital–physical shopping ecosystems
4. Growth in wellness and longevity-oriented products
5. Increased adoption of AR/VR commerce interfaces
```

---

## 💾 Files

| File | Description |
|------|--------------|
| `execution_log.txt` | Detailed execution trace with timestamps |
| `main.py` | Entry point orchestrating the agents |
| `agents/search_agent.py` | Web retrieval logic |
| `agents/analysis_agent.py` | Text summarization and insights |

---

