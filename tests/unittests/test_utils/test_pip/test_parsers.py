import os.path
from types import SimpleNamespace
from unittest.mock import patch, Mock

from requirements_txt.utils.pip.parsers import get_package_name, get_package_version, get_packages_info, \
    parse_packages_names, parse_requirements_txt


class TestGetPackageName:
    def test_get_package_name_obj(self):
        package_name = get_package_name(SimpleNamespace(
            name="some-name"
        ))
        assert package_name == "some-name"

    def test_get_package_name_dict(self):
        package_name = get_package_name({
            "name": "some-name"
        })
        assert package_name == "some-name"


class TestGetPackageVersion:
    def test_get_package_version_obj(self):
        package_version = get_package_version(SimpleNamespace(
            version="1.0.0"
        ))
        assert package_version == "1.0.0"

    def test_get_package_version_dict(self):
        package_version = get_package_version({
            "version": "1.0.0"
        })
        assert package_version == "1.0.0"


class TestGetPackagesInfo:
    @patch("requirements_txt.utils.pip.parsers.search_packages_info")
    @patch("requirements_txt.utils.pip.parsers._initialize_master_working_set")
    def test_get_packages_info_1(self, init_pip_mock: Mock, search_packages_info_mock: Mock):
        search_packages_info_mock.return_value = [SimpleNamespace(
            name="appdata",
            version="1.0.0"
        )]
        packages_info = get_packages_info(["appdata"])
        init_pip_mock.assert_called_once_with()
        assert len(packages_info) == 1
        assert packages_info["appdata"] == "1.0.0"


class TestParsePackagesNames:
    def test_parse_packages_names_1(self):
        args = ["appdata==1.0.0", "-r", "requirements.txt"]
        packages_names = parse_packages_names(args)
        # requirements.txt will be filtered while searching installed package
        assert packages_names == ["appdata", "requirements.txt"]

    def test_parse_packages_names_2(self):
        args = ["."]
        packages_names = parse_packages_names(args)
        # requirements.txt will be filtered while searching installed package
        assert packages_names == []

    def test_parse_packages_names_3(self):
        args = ["appdata==12.3.2", "other_module", "another==5.2.1"]
        packages_names = parse_packages_names(args)
        # requirements.txt will be filtered while searching installed package
        assert packages_names == ["appdata", "other_module", "another"]


class TestParseRequirementsTxt:
    def test_parse_requirements_txt_1(self, temp_dir: str):
        requirements_txt_path = os.path.join(
            temp_dir,
            "requirements.txt-temp"
        )
        with open(requirements_txt_path, "w+") as f:
            f.writelines([
                "appdata==1.0.2\n",
            ])
        requirements_txt_data = parse_requirements_txt(requirements_txt_path)
        assert len(requirements_txt_data) == 1
        assert requirements_txt_data["appdata"] == "1.0.2"

    def test_parse_requirements_txt_2(self, temp_dir: str):
        requirements_txt_path = os.path.join(
            temp_dir,
            "requirements.txt-temp"
        )
        with open(requirements_txt_path, "w+") as f:
            f.writelines([
                "appdata\n",
            ])
        requirements_txt_data = parse_requirements_txt(requirements_txt_path)
        assert len(requirements_txt_data) == 1
        assert requirements_txt_data["appdata"] is None

    def test_parse_requirements_txt_3(self, temp_dir: str):
        requirements_txt_path = os.path.join(
            temp_dir,
            "requirements.txt-temp"
        )
        with open(requirements_txt_path, "w+") as f:
            f.writelines([
                "appdata",
            ])
        requirements_txt_data = parse_requirements_txt(requirements_txt_path)
        assert len(requirements_txt_data) == 1
        assert requirements_txt_data["appdata"] is None

    def test_parse_requirements_txt_4(self, temp_dir: str):
        requirements_txt_path = os.path.join(
            temp_dir,
            "requirements.txt-temp"
        )
        with open(requirements_txt_path, "w+") as f:
            f.writelines([
                "# some comment\n",
                "appdata==1.0.2\n",
                "another_module\n"
            ])
        requirements_txt_data = parse_requirements_txt(requirements_txt_path)
        assert len(requirements_txt_data) == 2
        assert requirements_txt_data["appdata"] == "1.0.2"
        assert requirements_txt_data["another_module"] is None
