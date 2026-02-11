import pytest

@pytest.fixture(params=["Chrome", "Firefox", "Safari"])
def browser(request):
    return request.param

def test_website_on_different_browsers(browser):
    print(f"Тестуємо на {browser}...")
    assert browser in ["Chrome", "Firefox", "Safari"]