from database import db_session, init_db

from graphql_server import (HttpQueryError, default_format_error,
                            encode_execution_results, json_encode, load_json_body, run_http_query)


class App():
    def __init__(self):
        init_db()

    def query(self, request):
        return {"TODO": "add grapql logic here.."}
