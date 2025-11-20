# -*- coding: utf-8 -*-


def colored(text: str, color_code: str) -> str:
    """Wrap a text string with ANSI escape codes to display it in a given color.

    Parameters
    ----------
    text : str
        The text to be colored.
    color_code : str
        The ANSI color code as a string.

    Returns
    -------
    str
        The colored text string.
    """
    return f"\033[{color_code}m{text}\033[0m"
