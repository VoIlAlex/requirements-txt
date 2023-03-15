from unittest.mock import patch

from colored import attr, fg

from requirements_txt.utils.logging import set_verbose, logger_handler, show_all_done_message


class TestSetVerbose:
    def test_set_verbose_1(self):
        assert logger_handler.terminator == ""
        try:
            set_verbose(True)
            assert logger_handler.terminator == "\n"
        finally:
            logger_handler.terminator = ""

    def test_set_verbose_2(self):
        logger_handler.terminator = "\n"
        try:
            set_verbose(False)
            assert logger_handler.terminator == ""
        finally:
            logger_handler.terminator = ""


class TestShowAllDoneMessage:
    @patch("requirements_txt.utils.logging.ALL_DONE", "All done.")
    def test_show_all_done_message_1(self, capfd):
        show_all_done_message()
        out, err = capfd.readouterr()
        assert out == f'{fg(15)}All done.{attr(1)}{attr("reset")}\n\n'
