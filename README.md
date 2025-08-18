# In Memory Vector Search Demo

This is a demo project to query on a markdown file

- For now we just used DEVLOG.md as a sample file, this could be done better to add an endpoint to upload a file and index it.


## Get started
- uv sync 
- uvicorn main:app --reload 


## DSL

> A custom JSON as DSL

DSL Example

```json
{
  "action": "search",
  "query": ""
}
```