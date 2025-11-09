# 🧗 Challenges Overcome

## Lack of ChatGPT API Access
Initially, the system design relied on direct access to the OpenAI ChatGPT API for natural language understanding and summarization. However, API access was not available in the target environment, which blocked integration and made it impossible to call GPT-based models directly.

**Solution:**  
The limitation was resolved by switching to **Ollama**, an open-source local LLM runtime that supports running models like `llama3`, `mistral`, and `phi`. This approach allowed the project to:
- Run **entirely offline**, without depending on external APIs or network latency.  
- Maintain **fast inference** speeds due to local GPU/CPU execution.  
- Provide **consistent model availability** regardless of rate limits or service outages.  
- Enable **modular integration**, since Ollama exposes a simple local HTTP API that can replace OpenAI endpoints with minimal code changes.

This workaround ensured the system could continue functioning autonomously while preserving the intended architecture of agentic collaboration between the `SearchAgent` and `AnalysisAgent`.