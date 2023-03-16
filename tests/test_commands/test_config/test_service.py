from types import SimpleNamespace
from unittest.mock import patch, Mock, call, mock_open

from requirements_txt.commands.config.service import get_allowed_types, read_config, save_config


class TestGetAllowedTypes:
    def test_get_allowed_types_1(self):
        types = get_allowed_types(None)
        assert len(types) == 2
        assert type(None) in types
        assert bool in types

    def test_get_allowed_types_2(self):
        types = get_allowed_types("")
        assert len(types) == 1
        assert str in types

    def test_get_allowed_types_3(self):
        types = get_allowed_types("1")
        assert len(types) == 4
        assert str in types
        assert int in types
        assert float in types
        assert bool in types

    def test_get_allowed_types_4(self):
        types = get_allowed_types("0")
        assert len(types) == 4
        assert str in types
        assert int in types
        assert float in types
        assert bool in types

    def test_get_allowed_types_5(self):
        types = get_allowed_types("1.12")
        assert len(types) == 2
        assert str in types
        assert float in types


@patch("requirements_txt.commands.config.service.os.path.exists")
@patch("requirements_txt.commands.config.service.configparser.ConfigParser.read")
@patch("requirements_txt.commands.config.service.get_app_paths")
class TestReadConfig:
    def test_read_config_1(
        self,
        get_app_paths_mock: Mock,
        config_read_mock: Mock,
        path_exists_mock: Mock
    ):
        path_exists_mock.return_value = True
        get_app_paths_mock.side_effect = \
            lambda global_: SimpleNamespace(
                config_path="path_global"
            ) if global_ else SimpleNamespace(
                config_path="path_local"
            )
        read_config(None)
        path_exists_mock.assert_called_with("path_global")
        get_app_paths_mock.assert_has_calls([
            call(False),
            call(True)
        ])
        config_read_mock.assert_called_once_with(
            ["path_local", "path_global"]
        )

    def test_read_config_2(
        self,
        get_app_paths_mock: Mock,
        config_read_mock: Mock,
        path_exists_mock: Mock
    ):
        path_exists_mock.return_value = True
        get_app_paths_mock.side_effect = \
            lambda global_: SimpleNamespace(
                config_path="path_global"
            ) if global_ else SimpleNamespace(
                config_path="path_local"
            )
        read_config(True)
        path_exists_mock.assert_not_called()
        get_app_paths_mock.assert_called_once_with(True)
        config_read_mock.assert_called_once_with(
            ["path_global"]
        )

    def test_read_config_3(
        self,
        get_app_paths_mock: Mock,
        config_read_mock: Mock,
        path_exists_mock: Mock
    ):
        path_exists_mock.return_value = True
        get_app_paths_mock.side_effect = \
            lambda global_: SimpleNamespace(
                config_path="path_global"
            ) if global_ else SimpleNamespace(
                config_path="path_local"
            )
        read_config(False)
        path_exists_mock.assert_not_called()
        get_app_paths_mock.assert_called_once_with(False)
        config_read_mock.assert_called_once_with(
            ["path_local"]
        )


@patch("builtins.open", new_callable=mock_open)
@patch("requirements_txt.commands.config.service.get_app_paths")
class TestSaveConfig:
    def test_save_config_1(self, get_app_paths_mock: Mock, open_mock: Mock):
        config_mock = SimpleNamespace(
            write=Mock()
        )
        get_app_paths_mock.return_value = SimpleNamespace(
            config_path="config-path"
        )
        save_config(config_mock)
        get_app_paths_mock.assert_called_once_with(False)
        open_mock.assert_called_once_with("config-path", "w+")
        config_mock.write.assert_called_once_with(open_mock.return_value)

    def test_save_config_2(self, get_app_paths_mock: Mock, open_mock: Mock):
        config_mock = SimpleNamespace(
            write=Mock()
        )
        get_app_paths_mock.return_value = SimpleNamespace(
            config_path="config-path-2"
        )
        save_config(config_mock, True)
        get_app_paths_mock.assert_called_once_with(True)
        open_mock.assert_called_once_with("config-path-2", "w+")
        config_mock.write.assert_called_once_with(open_mock.return_value)

    def test_save_config_3(self, get_app_paths_mock: Mock, open_mock: Mock):
        config_mock = SimpleNamespace(
            write=Mock()
        )
        get_app_paths_mock.return_value = SimpleNamespace(
            config_path="config-path-3"
        )
        save_config(config_mock, global_=True)
        get_app_paths_mock.assert_called_once_with(True)
        open_mock.assert_called_once_with("config-path-3", "w+")
        config_mock.write.assert_called_once_with(open_mock.return_value)
