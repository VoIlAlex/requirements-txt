import os
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock, Mock, call, file_spec

from requirements_txt.utils.override import override_pip


class TestOverridePip:
    @patch("builtins.open", new_callable=mock_open)
    def test_override_pip_1(self, mock_open: Mock):
        mock_open.return_value = MagicMock(spec=file_spec)
        override_pip("/path/to/pip", "/path/to/python")
        new_pip_path = os.path.join(
            Path(__file__).parents[3].absolute(),
            "requirements_txt",
            'static',
            'new_pip.py'
        )
        mock_open.assert_has_calls([
            call("/path/to/pip", "w+"),
            call(new_pip_path)
        ], any_order=True)

        mock_open.return_value.__enter__.return_value.write.assert_called_once_with(
            mock_open.return_value.__enter__.return_value.read.return_value.format.return_value
        )
