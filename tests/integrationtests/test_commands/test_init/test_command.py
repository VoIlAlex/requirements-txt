from click.testing import CliRunner

from requirements_txt.commands import cli


class TestCommandInit:
    def test_command_init(self, temp_dir):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["init"])
            assert result.exit_code == 0


class TestCommandI:
    def test_command_i(self, temp_dir):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli, ["i"])
            assert result.exit_code == 0
