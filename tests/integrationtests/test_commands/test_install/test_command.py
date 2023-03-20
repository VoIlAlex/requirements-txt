import os.path
from unittest.mock import patch, Mock

from click.testing import CliRunner

from requirements_txt.commands import cli


class TestCommandInstall:
    @patch("requirements_txt.commands.install.service.get_pip_path")
    @patch("requirements_txt.commands.install.service.get_python_path")
    def test_command_init(self, get_python_path_mock: Mock, get_pip_path_mock: Mock, temp_dir):
        runner = CliRunner()
        with runner.isolated_filesystem():
            pip_path = os.path.join(
                os.getcwd(),
                "pip"
            )
            with open(pip_path, 'w+'):
                ...
            get_pip_path_mock.side_effect = [
                (pip_path, "python"),
                (None, None)
            ]

            python_path = os.path.join(
                os.getcwd(),
                "python"
            )
            get_python_path_mock.return_value = python_path

            result = runner.invoke(cli, ["install"])
            assert result.exit_code == 0
            assert os.path.exists(pip_path)

            with open(pip_path) as f:
                first_line = f.readline()
                assert first_line == f"#!{python_path}\n"
