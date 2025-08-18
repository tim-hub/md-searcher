from domain.ports.dls_converter_port import DSLConverterPort, DSLStructure


class DSLService:

    def __init__(self, dsl_converter: DSLConverterPort):
        self.dsl_converter = dsl_converter

    async def convert_query(self, query: str) -> DSLStructure:
        """
        Convert a Naturel Language query to a custom DSL format.
        :param query: The Naturel Language query to convert.
        :return: The converted DSL query.
        """
        return await self.dsl_converter.convert(query)
