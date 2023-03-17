from unittest.mock import patch

from requirements_txt.utils.crossplatform import get_destination_command


class TestGetDestinationCommand:
    @patch("sys.platform", "win32")
    def test_get_destination_command_windows_1(self):
        assert get_destination_command() == "where"

    @patch("sys.platform", "cygwin")
    def test_get_destination_command_windows_2(self):
        assert get_destination_command() == "where"

    @patch("sys.platform", "linux")
    def test_get_destination_command_linux_1(self):
        assert get_destination_command() == "which"

    @patch("sys.platform", "darwin")
    def test_get_destination_command_mac_1(self):
        assert get_destination_command() == "which"
