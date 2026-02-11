import pytest

@pytest.fixture
def sample_data():
    print("pre_setup connection to db")
    yield {"role":"pass some connection to db", "name":"Alosha"}
    print("close connection to db")

def test_check_role(sample_data):
    print(sample_data)
    assert sample_data["role"] == "pass some connection to db"

def test_check_name(sample_data):
    print(sample_data)
    assert sample_data["name"] == "Alosha"