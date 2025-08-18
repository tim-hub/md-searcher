
## Initial Design

- FastAPI for building the API endpoints.
- LangChain Structure Output (+ LLM) for Nature Language to DSL.
- sentence-transformers for embeddings markdown files. (or TF-IDF to make it simpler)


Input
- Markdown File
- Nature Language Query


Output
- Source Text


Port Adapter

- Driving (Inbound) Adapter  (A Query Controller provide API endpoint following the INPUT)
- Driven (Outbound) Adapter (A repository to handle markdown content splitting, embedding and matching )


### Structure

- domain
  - services (inbound)
    - query_service.py
  - outbound port
    - source_repository_interface.py
- adapters
  - inbound
    - query_controller.py
  - outbound
    - markdown_repository.py
