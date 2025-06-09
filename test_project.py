import pytest
from unittest.mock import patch
from project import (
    inventory,
    found_items,
    check_desk,
    check_books,
    check_safe,
    use_cog_on_safe,
    use_combination_code_on_safe,
    use_emblem_on_lock_box,
    use_key_on_door,
    check_inventory,
)

@patch('project.slow_print', lambda text, delay=0.03: print(text))  # Mock slow_print for faster tests
def setup_function():
    # Reset inventory and found_items for each test
    inventory.clear()
    for key in found_items:
        found_items[key] = False

@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_check_desk():
    # Test that emblem is added to inventory when checking the desk for the first time
    result = check_desk()
    assert "emblem" in inventory
    assert "You keep it on your inventory" in result

@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_check_books():
    # Test that cog is added to inventory when checking the books for the first time
    result = check_books()
    assert "cog" in inventory
    assert "You keep it on your inventory" in result

@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_check_safe():
    # Test checking the safe under different inventory conditions
    inventory.append("cog")
    inventory.append("combination code")
    check_safe()
    assert "lock box" in inventory
    assert found_items["lock_box"] is True


@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_use_combination_code_on_safe():
    inventory.append("cog")
    inventory.append("combination code")
    use_combination_code_on_safe()
    assert found_items["lock_box"] is True

@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_use_emblem_on_lock_box():
    # Test using emblem on lock box to obtain the key
    inventory.append("lock box")
    inventory.append("emblem")
    use_emblem_on_lock_box()
    assert "key" in inventory
    assert found_items["key"] is True

@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_use_key_on_door():
    # Test using the key on the door to escape
    inventory.append("key")
    assert use_key_on_door() is True

@patch('project.slow_print', lambda text, delay=0.03: print(text))
def test_check_inventory():
    # Test displaying inventory when it's empty and when it contains items
    check_inventory()
    inventory.append("key")
    check_inventory()
