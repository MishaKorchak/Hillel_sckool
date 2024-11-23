import unittest
from unittest.mock import MagicMock
import logging
from homework_10_1 import log_event  # Замініть `your_module_name` на ім'я файлу з функцією

class TestLogEvent(unittest.TestCase):
    def setUp(self):

        self.mock_logger = MagicMock()
        logging.getLogger = MagicMock(return_value=self.mock_logger)

    def test_success_status(self):
        log_event("user1", "success")
        self.mock_logger.info.assert_called_once_with("Login event - Username: user1, Status: success")

    def test_expired_status(self):
        log_event("user2", "expired")
        self.mock_logger.warning.assert_called_once_with("Login event - Username: user2, Status: expired")

    def test_failed_status(self):
        log_event("user3", "failed")
        self.mock_logger.error.assert_called_once_with("Login event - Username: user3, Status: failed")

if __name__ == "__main__":
    unittest.main()
