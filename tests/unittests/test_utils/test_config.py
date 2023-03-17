from unittest.mock import patch, Mock, call

from requirements_txt.utils.config import get_config_value
from pytest import raises


@patch("requirements_txt.utils.config.read_config")
class TestGetConfigValue:
    def test_get_config_value_defaults_1(self, read_config_mock: Mock):
        read_config_mock.return_value = {
            "DEFAULT": {}
        }
        assert get_config_value("only_git") is False
        assert get_config_value("allow_create", True) is False
        assert get_config_value("disable", False) is False

        read_config_mock.assert_has_calls([
            call(global_=None),
            call(global_=True),
            call(global_=False)
        ])

    def test_get_config_value_only_git_1(self, read_config_mock: Mock):
        read_config_mock.return_value = {
            "DEFAULT": {
                "only_git": "1"
            }
        }
        assert get_config_value("only_git") is True

    def test_get_config_value_allow_create_2(self, read_config_mock: Mock):
        read_config_mock.return_value = {
            "DEFAULT": {
                "allow_create": "1"
            }
        }
        assert get_config_value("allow_create") is True

    def test_get_config_value_disable_3(self, read_config_mock: Mock):
        read_config_mock.return_value = {
            "DEFAULT": {
                "disable": "1"
            }
        }
        assert get_config_value("disable") is True

    def test_get_config_value_not_exists(self, read_config_mock: Mock):
        read_config_mock.return_value = {
            "DEFAULT": {
                "disable": "1"
            }
        }
        with raises(RuntimeError, match='Wrong key.'):
            get_config_value("not-existing-key")
