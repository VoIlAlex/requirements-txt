#!{python_path}
# -*- coding: utf-8 -*-
import re
import sys
from pip._internal.cli.main import main
from pip._internal.cli.main_parser import parse_command

requirements_handler = False
try:
    from requirements_txt.update import add_installed_packages_to_requirements_txt, \
    remove_uninstalled_packages_from_requirements_txt
    from requirements_txt.config import get_config_value
    requirements_handler = True
except Exception as e:
    pass

if __name__ == '__main__':
    command, args = parse_command(sys.argv[1:])
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    res = main()
    if requirements_handler and res == 0:
        disable = get_config_value('disable')
        if not disable:
            if command == 'install':
                add_installed_packages_to_requirements_txt(args)
            if command == 'uninstall':
                remove_uninstalled_packages_from_requirements_txt(args)
    sys.exit(res)
