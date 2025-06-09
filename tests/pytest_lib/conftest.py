import pytest
import source.shapes as shapes

# pytest -m slow - run tests marked as slow
# pytest -s test_circle.py - run and show print messages
# clear - clear terminal

@pytest.fixture  # can be done only Not in class-based tests
def my_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)