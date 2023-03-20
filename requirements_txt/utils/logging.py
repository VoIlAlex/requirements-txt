import logging
import sys

from colored import attr, fg

from requirements_txt.utils.consts import ALL_DONE

logger = logging.getLogger("requirements-txt")
logger.setLevel(logging.INFO)
logger_handler = logging.StreamHandler(sys.stdout)
logger_formatter = logging.Formatter(
    f'{fg(15)}|===| %(message)s{attr(1)}{attr("reset")}'
)
logger_handler.setFormatter(logger_formatter)
logger_handler.terminator = ""
logger.addHandler(logger_handler)


def set_verbose(verbose: bool = False):
    """
    Set verbosity of logger.
    :param verbose: whether logger is verbose.
    """
    if verbose:
        logger_handler.terminator = "\n"
    else:
        logger_handler.terminator = ""


def show_all_done_message():
    """
    Print ALL_DONE message to the screen.
    """
    message = ALL_DONE
    final_message = ""
    for line in message.split("\n"):
        if line == "":
            final_message += "\n"
        else:
            final_message += f'{fg(15)}{line}{attr(1)}{attr("reset")}\n'

    final_message = final_message.replace(
        "The virtualenv project setup is complete.",
        f"{fg(129)}The virtualenv project setup is complete.{fg(15)}",
    )
    final_message = final_message.replace(
        "Happy codding!", f"{fg(129)}Happy codding!{fg(15)}"
    )
    print(final_message)


__all__ = [
    "logger",
    "set_verbose",
    "show_all_done_message",
]
