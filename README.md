# Ansible Role Janus

[![Build Status](https://travis-ci.org/ctorgalson/ansible-role-janus.svg?branch=master)](https://travis-ci.org/ctorgalson/ansible-role-janus)

This role uses Ansible to install the [Janus Vim distribution](https://github.com/carlhuda/janus)
for one or more users on macOS or Ubuntu, replacing Janus' [automatic installer](https://github.com/carlhuda/janus/blob/master/bootstrap.sh).

## Role Variables

| Variable name  | Default value | Description |
|----------------|---------------|-------------|
| `janus_home_dir`            | `/home`                           | Path to home directory--e.g. `/home` on Linux, `/Users` on macOS. |
| `janus_users`               | `[]`                              | A list of users and their groups. Janus will be installed for each user. See `defaults/main.yml`. |
| `janus_backup_files`        | `[ ".vim", ".vimrc", ".gvimrc" ]` | A list of Vim related files to backup on installation. |
| `janus_vim_plugins`         | `[]`                              | A list of Vim plugins including a name and git url for each--see `defaults/main.yml`. |
| `janus_vim_plugins_update`  | `yes`                             | Whether or not to update installed Vim plugins when a playbook including this role runs. |
| `janus_created_directories` | `[ ".janus", ".vim" ]`            | Directories created by this role whose permissions should be changed for each user when other operations are completed. |
| `janus_always_run_rake`     | `yes`                             | Whether or not to run rake in the `.vim` directory (runs git commands) when playbook runs. |
| `janus_rake_dir`            | `/usr/bin`                        | Directory in which `rake` should be found. |

## License

MIT
