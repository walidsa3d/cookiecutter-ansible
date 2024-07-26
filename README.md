# Cookiecutter-Ansible

This Cookiecutter template helps you create an Ansible role with Molecule testing. It supports various drivers (Vagrant, Docker, Podman) and verifiers (Ansible, Testinfra).

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Variables](#variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create a new Ansible role with a customizable name, description, author, and tags.
- Support for multiple Molecule drivers: Vagrant, Docker, Podman.
- Support for multiple Molecule verifiers: Ansible, Testinfra.
- Generate `meta/main.yml` with supported platforms.
- Generate `README.md` with role details and usage instructions.

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
`role_description` |	Description of the role
`galaxy_tags`	| Tags for Ansible Galaxy
`molecule_driver` | Molecule driver (vagrant, docker, podman)
`molecule_verifier` |	Molecule verifier (ansible, testinfra)
`supported_platforms` | List of supported platforms (name and versions)