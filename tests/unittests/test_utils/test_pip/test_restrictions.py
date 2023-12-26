import os
from unittest.mock import patch, Mock

from requirements_txt.utils.pip.restrictions import check_git_only_restriction, get_requirements_txt_path


@patch("requirements_txt.utils.pip.restrictions.os.path.exists")
@patch("requirements_txt.utils.pip.restrictions.get_config_value")
class TestCheckGitOnlyRestriction:
    def test_check_git_only_restriction_1(
            self,
            get_config_value_mock: Mock,
            os_path_exists_mock: Mock,
    ):
        get_config_value_mock.return_value = False
        result = check_git_only_restriction()
        assert result is True
        get_config_value_mock.assert_called_once_with("only_git")
        os_path_exists_mock.assert_not_called()

    def test_check_git_only_restriction_2(
            self,
            get_config_value_mock: Mock,
            os_path_exists_mock: Mock,
    ):
        get_config_value_mock.return_value = True
        os_path_exists_mock.return_value = True
        result = check_git_only_restriction()
        assert result is True
        git_path = os.path.join(
            os.getcwd(),
            '.git'
        )
        get_config_value_mock.assert_called_once_with("only_git")
        os_path_exists_mock.assert_called_once_with(git_path)

    def test_check_git_only_restriction_3(
            self,
            get_config_value_mock: Mock,
            os_path_exists_mock: Mock,
    ):
        get_config_value_mock.return_value = True
        os_path_exists_mock.return_value = False
        result = check_git_only_restriction()
        assert result is False
        git_path = os.path.join(
            os.getcwd(),
            '.git'
        )
        get_config_value_mock.assert_called_once_with("only_git")
        os_path_exists_mock.assert_called_once_with(git_path)


@patch("requirements_txt.utils.pip.restrictions.get_config_value")
class TestGetRequirementsTxtPath:
    def test_get_requirements_txt_path_1(self, _: Mock, temp_dir):
        requirements_txt_path_exp = os.path.join(
            os.getcwd(),
            'requirements.txt'
        )
        assert not os.path.exists(requirements_txt_path_exp)
        requirements_txt_path, created = get_requirements_txt_path(try_create=False)
        assert requirements_txt_path is None
        assert created is False

    def test_get_requirements_txt_path_2(self, _: Mock, temp_dir):
        requirements_txt_path_exp = os.path.join(
            os.getcwd(),
            'requirements.txt'
        )
        with open(requirements_txt_path_exp, 'w+'):
            ...

        requirements_txt_path, created = get_requirements_txt_path(try_create=False)
        assert requirements_txt_path == requirements_txt_path_exp
        assert created is False

    def test_get_requirements_txt_path_3(self, get_config_value: Mock, temp_dir):
        requirements_txt_path_exp = os.path.join(
            os.getcwd(),
            'requirements.txt'
        )
        get_config_value.return_value = False
        assert not os.path.exists(requirements_txt_path_exp)
        requirements_txt_path, created = get_requirements_txt_path(try_create=True)
        assert requirements_txt_path is None
        assert created is False

    def test_get_requirements_txt_path_4(self, get_config_value: Mock, temp_dir):
        requirements_txt_path_exp = os.path.join(
            os.getcwd(),
            'requirements.txt'
        )
        get_config_value.return_value = True
        assert not os.path.exists(requirements_txt_path_exp)
        requirements_txt_path, created = get_requirements_txt_path(try_create=True)
        assert requirements_txt_path == requirements_txt_path_exp
        assert created is True
