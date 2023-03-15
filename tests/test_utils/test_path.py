from unittest.mock import patch, Mock, call

from requirements_txt.utils.path import get_pip_path, get_python_path


@patch("requirements_txt.utils.path.get_destination_command")
@patch("requirements_txt.utils.path._execute_command")
class TestGetPipPath:
    def test_get_pip_path_1(
            self,
            execute_command_mock: Mock,
            get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "/home/user/requirements-txt/venv/bin/pip",
            "pip 23.0.1 from /home/user/requirements-txt/venv"
            "/lib/python3.10/site-packages/pip (python 3.10)"
        ]
        pip_path, python_name = get_pip_path("pip")
        assert pip_path == "/home/user/requirements-txt/venv/bin/pip"
        assert python_name == "python3.10"
        get_destination_command_mock.assert_called()
        execute_command_mock.assert_has_calls([
            call(["which-where", "pip"]),
            call(["pip", "--version"])
        ])

    def test_get_pip_path_2(
            self,
            execute_command_mock: Mock,
            get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "/home/user/requirements-txt/venv/bin/pip",
            "pip 23.0.1 from /home/user/requirements-txt/venv"
            "/lib/python3.11/site-packages/pip (python 3.11)"
        ]
        pip_path, python_name = get_pip_path("pip3")
        assert pip_path == "/home/user/requirements-txt/venv/bin/pip"
        assert python_name == "python3.11"
        get_destination_command_mock.assert_called()
        execute_command_mock.assert_has_calls([
            call(["which-where", "pip3"]),
            call(["pip3", "--version"])
        ])

    def test_get_pip_path_3(
            self,
            execute_command_mock: Mock,
            get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "/home/user/requirements-txt/venv/bin/pip",
            "pip 23.0.1 from /home/user/requirements-txt/venv"
            "/lib/python3.10/site-packages/pip (python 3.10)",
            "/home/user/requirements-txt/venv2/bin/pip",
            "pip 23.0.1 from /home/user/requirements-txt/venv2"
            "/lib/python3.10/site-packages/pip (python 3.10)"
        ]
        pip_path, python_name = get_pip_path()
        assert pip_path == "/home/user/requirements-txt/venv/bin/pip"
        assert python_name == "python3.10"
        get_destination_command_mock.assert_called()
        execute_command_mock.assert_has_calls([
            call(["which-where", "pip"]),
            call(["pip", "--version"])
        ])

    def test_get_pip_path_4(
            self,
            execute_command_mock: Mock,
            get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "pip",
            "/home/user/requirements-txt/venv2/bin/pip",
            "pip 23.0.1 from /home/user/requirements-txt/venv2"
            "/lib/python3.10/site-packages/pip (python 3.10)"
        ]
        pip_path, python_name = get_pip_path()
        assert pip_path == "/home/user/requirements-txt/venv2/bin/pip"
        assert python_name == "python3.10"
        get_destination_command_mock.assert_called()
        execute_command_mock.assert_has_calls([
            call(["which-where", "pip"]),
            call(["which-where", "pip3"]),
            call(["pip3", "--version"])
        ])


@patch("requirements_txt.utils.path.get_destination_command")
@patch("requirements_txt.utils.path._execute_command")
class TestGetPythonPath:
    def test_get_python_path_1(
        self,
        execute_command_mock: Mock,
        get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "/home/user/requirements-txt/venv/bin/python",
        ]
        python_path = get_python_path("python")
        assert python_path == "/home/user/requirements-txt/venv/bin/python"
        execute_command_mock.assert_has_calls([
            call(["which-where", "python"])
        ])

    def test_get_python_path_2(
        self,
        execute_command_mock: Mock,
        get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "/home/user/requirements-txt/venv2/bin/python",
        ]
        python_path = get_python_path("python")
        assert python_path == "/home/user/requirements-txt/venv2/bin/python"
        execute_command_mock.assert_has_calls([
            call(["which-where", "python"])
        ])

    def test_get_python_path_3(
        self,
        execute_command_mock: Mock,
        get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "/home/user/requirements-txt/venv/bin/python",
        ]
        python_path = get_python_path("python3")
        assert python_path == "/home/user/requirements-txt/venv/bin/python"
        execute_command_mock.assert_has_calls([
            call(["which-where", "python3"])
        ])

    def test_get_python_path_4(
        self,
        execute_command_mock: Mock,
        get_destination_command_mock: Mock
    ):
        get_destination_command_mock.return_value = "which-where"
        execute_command_mock.side_effect = [
            "python3",
            "/home/user/requirements-txt/venv/bin/python"
        ]
        python_path = get_python_path()
        assert python_path == "/home/user/requirements-txt/venv/bin/python"
        execute_command_mock.assert_has_calls([
            call(["which-where", "python3"]),
            call(["which-where", "python"])
        ])
