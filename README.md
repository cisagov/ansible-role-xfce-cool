# ansible-role-xfce-cool #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-xfce-cool/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-xfce-cool/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-xfce-cool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-xfce-cool/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-xfce-cool.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-xfce-cool/context:python)

An Ansible role for installing the [Xfce](https://www.xfce.org/) desktop
environment and configuring it for use in the COOL.  This role is not meant to
be generally useful to the community as it has COOL-specific customizations.
Please see [ansible-role-xfce](https://github.com/cisagov/ansible-role-xfce) if
you are in need of a more general Xfce role.

Currently this role only supports [Kali Linux](https://www.kali.org/) as it
makes changes  about the desktop configuration that only exists in the Kali
distribution.

## What this role does ##

- Install COOL [desktop
  images](https://github.com/cisagov/cool-system/tree/develop/assets/desktops)
  from the [cool-system](https://github.com/cisagov/cool-system) repository.
- Create a desktop shortcut to the shared
  [`/data`](https://github.com/cisagov/ansible-role-amazon-efs-utils)
  mountpoint.
- Install and set the terminal font to
  [JetBrains Mono](https://www.jetbrains.com/lp/mono/).
- Configure the clock panel to show the time in
  [UTC](https://www.timeanddate.com/worldclock/timezone/utc).

## Requirements ##

None.

## Role Variables ##

- `jetbrainsmono_version` - the version of the JetBrainsMono font to
  download from JetBrains/JetBrainsMono.  Defaults to "2.241".

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - xfce
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Mark Feldhousen - <mark.feldhousen@trio.dhs.gov>
