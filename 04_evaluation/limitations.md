# ⚠️ Limitations

## Current Constraints
1. **Network Dependency** — The `SearchAgent` requires live internet access; no offline mode.  
2. **Limited Context Retention** — Each run is independent; previous search histories aren’t reused.  
3. **Basic Error Handling** — Failures in API or web calls may stop execution.  
4. **No Parallelism** — Agents execute sequentially, limiting throughput.  
5. **Surface-Level Analysis** — The `AnalysisAgent` produces summaries but not quantitative analytics.

## Technical Boundaries
- Single-threaded Python execution  
- Non-persistent data cache  
- Dependent on third-party web APIs for trend data
