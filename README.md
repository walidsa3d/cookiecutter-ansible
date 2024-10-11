# Cookiecutter-Ansible

This Cookiecutter template helps you create an Ansible role with Molecule tests.

## Table of Contents

- [Cookiecutter-Ansible](#cookiecutter-ansible)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Variables](#variables)
  - [License](#license)

## Features

- Creates a new Ansible role with a custom name, description, author, and galaxy tags.
- Supports multiple Molecule drivers: Vagrant, Docker, Podman.
- Supports multiple Molecule verifiers: Ansible, Testinfra.
- Generates `README.md` with role details and usage instructions.

## Requirements

- Cookiecutter >= 1.7.2
- Python >= 3.6

## Installation

To install Cookiecutter, use pip:

```sh
pip install cookiecutter
pip install git+https://github.com/cookiecutter/cookiecutter.git
```
## Usage
```
cookiecutter gh:walidsa3d/cookicutter-ansible
```

## Variables
The following variables can be customized in cookiecutter.json:

| Variable | Description |
|:----------|:----------|	
`role_name` |	Name of the Ansible role
`author_name`	| Author of the role
`github_username`	| Github Username of the Author
`role_description` |	Description of the role
`molecule_driver` | Molecule driver (vagrant, docker, podman)
`molecule_verifier` |	Molecule verifier (ansible, testinfra)
`platform` | List of supported platforms

## License
MIT