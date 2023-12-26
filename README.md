# to-requirements.txt | Automatically update requirements.txt 

[![PyPI release](https://img.shields.io/pypi/v/to-requirements.txt)](https://pypi.org/project/to-requirements.txt/)
[![Build status](https://github.com/VoIlAlex/requirements-txt/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/VoIlAlex/requirements-txt/actions/workflows/publish-to-pypi.yml/badge.svg)
[![Maintainability](https://img.shields.io/maintenance/yes/2023)](https://img.shields.io/maintenance/yes/2023)
[![License](https://img.shields.io/github/license/VoIlAlex/requirements-txt)](https://github.com/VoIlAlex/requirements-txt/blob/master/LICENSE.md)

[//]: # ([![Downloads]&#40;https://static.pepy.tech/personalized-badge/to-requirements.txt?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads&#41;]&#40;https://pepy.tech/project/appdata&#41;)

[//]: # ([![Linux]&#40;https://svgshare.com/i/Zhy.svg&#41;]&#40;https://svgshare.com/i/Zhy.svg&#41;)

[//]: # ([![Windows]&#40;https://svgshare.com/i/ZhY.svg&#41;]&#40;https://svgshare.com/i/ZhY.svg&#41;)

[//]: # ([![macOS]&#40;https://svgshare.com/i/ZjP.svg&#41;]&#40;https://svgshare.com/i/ZjP.svg&#41;)

**to-requirements.txt** allows to automatically manage dependencies in requirements.txt using **pip** as a package manager.


[![Demo](https://media.giphy.com/media/y9dUiCm2SwaU8qR0eD/giphy.gif)](https://media.giphy.com/media/y9dUiCm2SwaU8qR0eD/giphy.gif)


## Benefits

**Easy to setup.**
The installation process include only two steps: install the package using pip
and setup up it using script provided by the package. That's it.

**Setup in one command.**
You can set up VirtualEnv-based project in one command. It will create virtual environment.
And install *to-requirements.txt* automatically.

**Customizable.**
Customize it the way you like: use it only in git repositories, allow or disallow
automated requirements.txt file creation, enable or disable the package itself.

**Easy to use.**
After installing the package, running setup command and (optionally) customizing it
the package is ready. There is no additional conditions to use. Just install,
uninstall or upgrade packages using *pip* as you usually do.

**Always in sync.**
With *to-requirements.txt* the project's requirements.txt will always stay in sync
with packages that you install using *pip*.


## Installation


To install the package run the following command:

```shell
pip install to-requirements.txt
```
    

And after that run the command below to initialize the package:

```shell
requirements-txt install
```

It will update your current *pip* scripts to execute the functionality of
this package. Also, if you want to enable all the available functionality of
the package you should put the lines below to your .bashrc, .zshrc or other 
.*rc file:

```shell
alias rt=". rt"
alias requirements-txt=". requirements-txt"
```

Or simply use the cli command:

```shell
rt alias
```

It will enable sourced mode of the cli execution and the cli will be able 
to activate your virtual environment / deactivate it if required.

*The changes made to **pip** scripts will not affect ordinary *pip* workflow after
uninstalling **to-requirements.txt**.*

### Setup project

To set up VirtualEnv based project just type:
```shell
requirements-txt init
```

The same effect could be achieved much easier with aliases:
```shell
rt i
```

## Documentation

The detailed documentation is available on
[requirements-txt.readthedocs.io](https://requirements-txt.readthedocs.io/en/latest/index.html).

## Contributing

Visit the file [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Visit the file [MIT](LICENSE.md).
