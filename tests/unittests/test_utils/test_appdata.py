import os
from types import SimpleNamespace
from unittest.mock import patch, Mock, PropertyMock, MagicMock

from appdata import AppDataPaths, get_home_folder

from requirements_txt.utils.appdata import validate_app_data_decorator, validate_app_data, insert_app_paths, \
    get_app_paths


@patch(
    "requirements_txt.utils.appdata.AppDataPaths.require_setup",
    new_callable=PropertyMock
)
@patch("requirements_txt.utils.appdata.AppDataPaths.setup")
class TestValidateAppDataDecorator:
    def test_validate_app_data_decorator_1(
            self,
            app_paths_setup_mock: Mock,
            require_setup_mock: Mock
    ):
        require_setup_mock.return_value = True

        @validate_app_data_decorator
        def _f():
            ...

        _f()
        app_paths_setup_mock.assert_called_once()

    def test_validate_app_data_decorator_2(
            self,
            app_paths_setup_mock: Mock,
            require_setup_mock: Mock
    ):
        require_setup_mock.return_value = False

        @validate_app_data_decorator
        def _f():
            ...

        _f()
        app_paths_setup_mock.assert_not_called()


@patch("requirements_txt.utils.appdata.get_app_paths")
class TestValidateAppData:
    def test_validate_app_data_1(self, get_app_paths_mock: Mock):
        setup_mock = Mock(return_value=None)
        get_app_paths_mock.return_value = SimpleNamespace(
            require_setup=True,
            setup=setup_mock
        )
        validate_app_data(global_=False)
        get_app_paths_mock.assert_called_once_with(False)
        setup_mock.assert_called_once()

    def test_validate_app_data_2(self, get_app_paths_mock: Mock):
        setup_mock = Mock(return_value=None)
        get_app_paths_mock.return_value = SimpleNamespace(
            require_setup=False,
            setup=setup_mock
        )
        validate_app_data(global_=True)
        get_app_paths_mock.assert_called_once_with(True)
        setup_mock.assert_not_called()


class TestInsertAppPaths:
    def test_insert_app_paths_1(self):
        @insert_app_paths
        def _f(app_paths: AppDataPaths):
            assert isinstance(app_paths, AppDataPaths)
            assert app_paths.name == "to-requirements.txt"

        _f()


class TestGetAppPaths:
    def test_get_app_paths_1(self):
        app_paths = get_app_paths()
        assert app_paths.name == "to-requirements.txt"
        assert app_paths.home_folder_path == os.getcwd()

    def test_get_app_paths_2(self):
        app_paths = get_app_paths(global_=False)
        assert app_paths.name == "to-requirements.txt"
        assert app_paths.home_folder_path == os.getcwd()

    def test_get_app_paths_3(self):
        app_paths = get_app_paths(global_=True)
        assert app_paths.name == "to-requirements.txt"
        assert app_paths.home_folder_path == get_home_folder()
