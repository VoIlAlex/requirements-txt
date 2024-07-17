# to-requirements.txt | Automatically Update requirements.txt

[![PyPI Release](https://img.shields.io/pypi/v/to-requirements.txt)](https://pypi.org/project/to-requirements.txt/)
[![Build Status](https://github.com/VoIlAlex/requirements-txt/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/VoIlAlex/requirements-txt/actions/workflows/publish-to-pypi.yml)
[![Maintainability](https://img.shields.io/maintenance/yes/2024)](https://img.shields.io/maintenance/yes/2024)
[![License](https://img.shields.io/github/license/VoIlAlex/requirements-txt)](https://github.com/VoIlAlex/requirements-txt/blob/master/LICENSE.md)

**to-requirements.txt** allows for the automatic management of dependencies in `requirements.txt` using **pip** as a package manager.

[![Demo](https://media.giphy.com/media/y9dUiCm2SwaU8qR0eD/giphy.gif)](https://media.giphy.com/media/y9dUiCm2SwaU8qR0eD/giphy.gif)

## Benefits

- **Easy Setup**: The installation process involves just two steps: installing the package using pip and setting it up using the provided script. That's it.
  
- **One-Command Setup**: Set up a VirtualEnv-based project in a single command. It creates a virtual environment and installs *to-requirements.txt* automatically.

- **Customizable**: Customize it as you prefer: use it only in Git repositories, allow or disallow automated `requirements.txt` file creation, enable or disable the package itself.

- **User-Friendly**: After installation and setup, there are no additional conditions to use. Simply install, uninstall, or upgrade packages using *pip* as usual.

- **Always in Sync**: With *to-requirements.txt*, the project's `requirements.txt` will always stay in sync with packages installed via *pip*.

## Installation

To install the package, run the following command:

```shell
pip install to-requirements.txt
```

Then, initialize the package with:

```shell
requirements-txt install
```

To enable all available functionality, add the following lines to your `.bashrc`, `.zshrc`, or other `.*rc` file:

```shell
alias rt=". rt"
alias requirements-txt=". requirements-txt"
```

Or, use the CLI command:

```shell
rt alias
```

This enables sourced mode of the CLI execution and allows the CLI to activate or deactivate your virtual environment if required.

*Note: The changes made to **pip** scripts will not affect the ordinary *pip* workflow after uninstalling **to-requirements.txt*.**

### Setup Project

To set up a VirtualEnv-based project, simply type:

```shell
requirements-txt init
```

Or, achieve the same effect more easily with aliases:

```shell
rt i
```

## Documentation

For detailed documentation, visit [requirements-txt.readthedocs.io](https://requirements-txt.readthedocs.io/en/latest/index.html).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

This project is licensed under the [MIT License](LICENSE.md).
