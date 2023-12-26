import os
from unittest.mock import patch

from appdata import AppDataPaths
from click.testing import CliRunner
from requirements_txt.commands import cli


class TestCommandConfig:
    def test_command_config_only_git(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "only_git"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\nonly_git = 1\n\n"

    def test_command_config_only_git_0(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "only_git", "0"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\nonly_git = 0\n\n"

    def test_command_config_only_git_1(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "only_git", "1"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\nonly_git = 1\n\n"

    def test_command_config_only_git_bad(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "only_git", "bad"])
            assert result.exit_code == 1
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == ""

    def test_command_config_allow_create(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "allow_create"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\nallow_create = 1\n\n"

    def test_command_config_allow_create_0(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "allow_create", "0"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\nallow_create = 0\n\n"

    def test_command_config_allow_create_1(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "allow_create", "1"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\nallow_create = 1\n\n"

    def test_command_config_allow_create_bad(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "allow_create", "bad"])
            assert result.exit_code == 1
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == ""

    def test_command_config_disable(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "disable"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\ndisable = 1\n\n"

    def test_command_config_disable_0(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "disable", "0"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\ndisable = 0\n\n"

    def test_command_config_disable_1(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "disable", "1"])
            assert result.exit_code == 0
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == "[DEFAULT]\ndisable = 1\n\n"

    def test_command_config_bad_key(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["config", "bad_key", "1"])
            assert result.exit_code == 1
            config_path = os.path.join(
                os.getcwd(),
                ".to-requirements.txt",
                "default.ini"
            )
            assert os.path.exists(config_path)
            with open(config_path) as f:
                data = f.read()
                assert data == ""

    def test_command_config_global_1(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            global_path = os.path.join(
                os.getcwd(),
                "test-global-path"
            )
            os.makedirs(global_path)
            with patch("requirements_txt.commands.config.command.get_app_paths") as get_app_paths_1_mock:
                with patch("requirements_txt.utils.config.get_app_paths") as get_app_paths_2_mock:
                    with patch("requirements_txt.utils.appdata.get_app_paths") as get_app_paths_3_mock:
                        def new_get_app_paths(global_):
                            if global_:
                                return AppDataPaths(
                                    "to-requirements.txt",
                                    home_folder_path=global_path
                                )
                            assert False, "Called not global."
                        get_app_paths_1_mock.side_effect = new_get_app_paths
                        get_app_paths_2_mock.side_effect = new_get_app_paths
                        get_app_paths_3_mock.side_effect = new_get_app_paths

                        result = runner.invoke(cli, ["config", "--global", "disable", "1"])
                        assert result.exit_code == 0

                        config_path = os.path.join(
                            global_path,
                            ".to-requirements.txt",
                            "default.ini"
                        )
                        with open(config_path) as f:
                            data = f.read()
                            assert data == "[DEFAULT]\ndisable = 1\n\n"





