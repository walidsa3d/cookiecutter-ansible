# {{ cookiecutter.role_name }}

{{ cookiecutter.role_description }}

## Table of Contents

- [Requirements](#requirements)
- [Role Variables](#role-variables)
- [Dependencies](#dependencies)
- [Example Playbook](#example-playbook)
- [Contributing](#contributing)
- [License](#license)

## Install
```
ansible-galaxy role install {{cookiecutter.github_username}}.{{cookiecutter.role_name}}

```

## Requirements

- Ansible >= 2.9
- Supported platforms:
  - {{ cookiecutter.platform }}


## Role Variables

The variables used in this role are defined in `defaults/main.yml` and can be customized as per your requirements. Here are some of the main variables:

| Variable           | Default Value           | Description                          |
|--------------------|-------------------------|--------------------------------------|
| `molecule_driver`  | `vagrant`               | Molecule driver (vagrant, docker, podman) |
| `molecule_verifier`| `ansible`               | Molecule verifier (ansible, testinfra) |

## Dependencies

This role has no external dependencies.

## Example Playbook

Here is an example of how to use this role in a playbook:

```yaml
---
- name: Use your role
  hosts: all
  become: true
  roles:
    - role: {{ cookiecutter.role_name }}
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.