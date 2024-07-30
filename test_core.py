# tests/test_core.py
import pytest
from unittest.mock import patch
from your_application import core_logic

@patch('your_application.dependencies.some_external_service')
def test_some_function(mock_service):
    mock_service.return_value = 'mocked_value'
    result = core_logic.some_function()
    assert result == 'expected_value'
