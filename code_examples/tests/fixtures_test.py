import pytest

@pytest.fixture
def sample_data():
    return {"name": "Олексій", "role": "admin"}

def test_check_role(sample_data):
    assert sample_data["role"] == "admin"

def test_check_name(sample_data):
    assert sample_data["name"] == "Олексій"