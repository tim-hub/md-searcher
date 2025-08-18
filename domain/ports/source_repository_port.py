from abc import ABC, abstractmethod
from typing import List, Tuple


class SourceRepositoryPort(ABC):

    @abstractmethod
    def query_on_source(self, query: str) -> List[Tuple[float, str]]:
        """
        Retrieve a source by its ID.
        :param dsl: The DSL structure containing the query and parameters.
        :return: The retrieved source object.
        """
        pass
