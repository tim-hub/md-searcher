# In Memory Vector Search Demo

> https://github.com/tim-hub/md-searcher

This is a demo project to query on a markdown file

- For now we just used [sample_text.md](adapters/driven/markdown_repository/sample_text.md) as a sample file, this could
  be done better to add an endpoint to upload a file and index it.

## Get started

- `uv sync`
- `uvicorn main:app --reload`
- visit http://127.0.0.1:8000/docs

## DSL

> We used a custom JSON as DSL, for simplicity and flexibility especially for vector search.
> This DSL is not a strict language, but rather a structured way to represent the query.
> 
> SQL like DSL is considered, but it may not work well with vector search, because vector search does not rely on exact
> matches, but rather on sentimental similarity scores.

DSL Example

From:
`Can you tell me what is magic from the source with no more than 5 results?`

To:

```json
{
  "action": "search",
  "query": "what is magic",
  "top_k": 5
}
```

> please note because the nature of LLM, this DSL result may not be exactly the same as above, but it should be similar.