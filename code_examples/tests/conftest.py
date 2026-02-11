import pytest

@pytest.fixture
def db_connection():
    conn = {"status": "connected", "user": "root"}
    yield conn
    conn["status"] = "closed"