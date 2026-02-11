import pytest
import sys

@pytest.mark.skip(reason="Цей тест ще в розробці")
def test_unfinished_feature():
    assert False

@pytest.mark.skipif(sys.platform == "win32", reason="Не працює на Windows")
def test_linux_only_feature():
    assert True

@pytest.mark.xfail(reason="Відомий баг з округленням")
def test_precision():
    assert 0.1 + 0.2 == 0.3  # В Python це дасть 0.30000000000000004


@pytest.mark.smoke
def test_login_page():
    assert True

@pytest.mark.regression
def test_complex_data_processing():
    assert True