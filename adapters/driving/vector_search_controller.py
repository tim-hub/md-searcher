from fastapi import APIRouter

from adapters.driven.llm_dsl_converter import LLMDSLConverter
from adapters.driven.markdown_repository import MarkdownRepository
from domain.services.dsl_service import DSLService
from domain.services.search_service import SearchService

router = APIRouter()

# initialize the repositories and converters
markdown_repo = MarkdownRepository()
dls_converter = LLMDSLConverter()

# register the services
dls_service = DSLService(dls_converter)
search_service = SearchService(markdown_repo)

from pydantic import BaseModel


class UserQuery(BaseModel):
    question: str


@router.post("/query")
async def query(user_query: UserQuery):
    question = user_query.question.strip() if user_query.question else None
    if not question:
        return {"error": "question is required"}

    try:
        # convert the query to DSL
        dsl_query = await dls_service.convert_query(question)
    except Exception as e:
        return {"error": f"Failed to convert query to DSL: {str(e)}"}

    try:
        # perform the search using the DSL query
        results = await search_service.search(dsl_query)
    except Exception as e:
        return {"error": f"Failed to perform search: {str(e)}"}

    return {
        "dsl_query": dsl_query,
        "data": results
    }
