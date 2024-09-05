class SQLAlchemyErrorException(Exception):
    def __init__(self, sql_alchemy_error: str):
        self.sql_alchemy_error = sql_alchemy_error
        self.detail = f"An error occurred while executing SQL query: {sql_alchemy_error}"
        super().__init__(self.detail)
