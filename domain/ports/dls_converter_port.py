from abc import ABC, abstractmethod

from typing_extensions import Annotated, TypedDict


class DSLStructure(TypedDict):
    action: Annotated[
        str, ..., "Action to do for now, just return search by default"]  # this could be extended based on different requirements
    query: Annotated[
        str, ..., 'The key query to search for, e.g., Can you tell me whether dog or cat is more friendly? It will be shorten to Is dog or cat more friendly?']  # the main query to search
    top_n: Annotated[int, ..., 'How many results to return, return 1 by default if not mentioned.']  # number of top results to return


class DSLConverterPort(ABC):
    @abstractmethod
    async def convert(self, query: str) -> DSLStructure:
        """
        Convert a DSL query to another format.
        :param query: The DSL query to convert.
        :return: The converted query.
        """
        pass
