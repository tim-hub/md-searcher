from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from domain.ports.dls_converter_port import DSLConverterPort, DSLStructure

load_dotenv()


class LLMDSLConverter(DSLConverterPort):
    """
    Converts LLM DSL to a format suitable for the LLM.
    Using Langchain StructuredOutput
    """

    def __init__(self):
        self.model = init_chat_model("gemini-2.5-flash-lite", model_provider="google_genai").with_structured_output(
            DSLStructure)

    async def convert(self, query: str) -> DSLStructure:
        try:
            return await self.model.ainvoke(query, structured_output=True)
        except Exception as e:
            print(f"Error during conversion: {e}. Try again in 2 seconds.")
            import asyncio
            await asyncio.sleep(2)
            return await self.model.ainvoke(query, structured_output=True)


if __name__ == "__main__":
    import asyncio

    converter = LLMDSLConverter()
    query = "Can you tell me whether dog or cat or mouse is cuter? Give me top 5 results."
    result = asyncio.run(converter.convert(query))
    print(result)
