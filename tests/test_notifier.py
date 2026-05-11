import pytest, sys, os
from unittest.mock import Mock
from notifications.notifier import StudentNotifier

def _make_notifier(send_result: bool = True):
    mock_client = Mock()
    mock_client.send.return_value = send_result
    return StudentNotifier(mock_client), mock_client

def test_notify_request_created_calls_send():
    notifier, mock = _make_notifier()
    result = notifier.notify_request_created("S123", 42)
    assert result is True
    mock.send.assert_called_once_with("S123", "Your request #42 has been created")

def test_notify_duplicate_calls_send():
    notifier, mock = _make_notifier()
    result = notifier.notify_duplicate("S123", "password_reset")
    assert result is True
    mock.send.assert_called_once_with("S123", "Duplicate request on topic 'password_reset'")