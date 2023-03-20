import os.path

from click.testing import CliRunner

from requirements_txt.commands import cli


class TestCommandShow:
    def test_command_show_1(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            requirements_txt_path = os.path.join(
                os.getcwd(),
                "requirements.txt"
            )

            with open(requirements_txt_path, 'w+') as f:
                f.writelines([
                    "appdata==1.0.0\n",
                    "something==2.3.1"
                ])

            result = runner.invoke(cli, ["show"])
            assert result.stdout == "appdata==1.0.0\nsomething==2.3.1\n"

    def test_command_show_2(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            requirements_txt_path = os.path.join(
                os.getcwd(),
                "requirements.txt"
            )

            with open(requirements_txt_path, 'w+') as f:
                ...

            result = runner.invoke(cli, ["show"])
            assert result.stdout == "\n"


class TestCommandS:
    def test_command_s_1(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            requirements_txt_path = os.path.join(
                os.getcwd(),
                "requirements.txt"
            )

            with open(requirements_txt_path, 'w+') as f:
                f.writelines([
                    "appdata==1.0.0\n",
                    "something==2.3.1"
                ])

            result = runner.invoke(cli, ["s"])
            assert result.stdout == "appdata==1.0.0\nsomething==2.3.1\n"

    def test_command_s_2(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            requirements_txt_path = os.path.join(
                os.getcwd(),
                "requirements.txt"
            )

            with open(requirements_txt_path, 'w+') as f:
                ...

            result = runner.invoke(cli, ["s"])
            assert result.stdout == "\n"
