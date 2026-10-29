# BrainForge Inference Plugin: RAG

Request step that retrieves documents for selected RAG providers, and a
response step that rewrites the generated answer with citations. Both steps
ship together because citations read `request_step_context["brainforge.rag"]` and
share `apply_citation_markup`.

| Pipeline | Entry point group | Step id | Class |
| --- | --- | --- | --- |
| Request | `brainforge.inference.request_steps` | `brainforge.rag` | `RagStep` |
| Response | `brainforge.inference.response_steps` | `brainforge.citations` | `ResponseParser` |

```yaml
pipeline:
  request:
    - id: brainforge.rag
      config:
        mcp_url: https://mcp.neonaiservices2.com/mcp
        top_k: 10
  response:
    - id: brainforge.citations
      config:
        mcp_url: https://mcp.neonaiservices2.com/mcp
        openai_url: https://hana.example/brainforge/openai/chat/completions
```
