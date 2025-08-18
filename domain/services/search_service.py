import logging

from domain.ports.dls_converter_port import DSLStructure
from domain.ports.source_repository_port import SourceRepositoryPort


class SearchService:
    def __init__(self, search_repository: SourceRepositoryPort):
        self.search_repository = search_repository

    async def search(self, dsl: DSLStructure):
        """
        Perform a search using the provided query.

        :param dsl: DSLStructure containing the query and parameters.
        :return: Search results.
        """

        action = dsl.get('action', 'search').lower()
        query = dsl.get('query', '').strip()
        top_n = int(dsl.get('top_n', 3))

        if action != "search":
            raise ValueError("Invalid DSL action. Expected 'search'.")

        if not query:
            raise ValueError("Query is required for search action.")

        logging.info(f"Performing action: {action} with query: {query}")
        results = self.search_repository.query_on_source(query)

        filtered_results = [result for result in results if result[0] > 0]

        return filtered_results[:top_n] if filtered_results else []
