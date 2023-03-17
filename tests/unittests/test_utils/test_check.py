from requirements_txt.utils.check import is_pip_name


class TestIsPipName:
    def test_is_pip_name_1(self):
        assert is_pip_name("pip") is True

    def test_is_pip_name_2(self):
        assert is_pip_name("pip3") is True

    def test_is_pip_name_3(self):
        assert is_pip_name("pip2") is True

    def test_is_pip_name_4(self):
        assert is_pip_name("pip3.8") is True

    def test_is_pip_name_negative_1(self):
        assert is_pip_name("some-pip") is False

    def test_is_pip_name_negative_2(self):
        assert is_pip_name("python") is False
