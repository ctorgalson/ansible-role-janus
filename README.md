# Ansible Role Janus

[![Build Status](https://travis-ci.org/ctorgalson/ansible-role-janus.svg?branch=master)](https://travis-ci.org/ctorgalson/ansible-role-janus)

This role uses Ansible to install the [Janus Vim distribution](https://github.com/carlhuda/janus)
for one or more users on macOS or Ubuntu, replacing Janus' [automatic installer](https://github.com/carlhuda/janus/blob/master/bootstrap.sh).

## Role Variables

| Variable name  | Default value | Description |
|----------------|---------------|-------------|
| `janus_required_packages` | `[]` | List of packages to install (uses [the `package` module](http://docs.ansible.com/ansible/latest/modules/package_module.html#package-module) on Linux, i[the `homebrew` module](http://docs.ansible.com/ansible/latest/modules/homebrew_module.html#homebrew-module) on marcsOS). Janus requires `rake` and `vim` to work, so this might need to be e.g. `['rake', 'vim']`. |
| `janus_git_repo` | `https://github.com/carlhuda/janus.git` | The
repository to clone Janus from. Should seldome need changing. |
| `janus_version` | `HEAD` | The git version of Janus to clone. Passed directly to the `version` property of [the Git module](http://docs.ansible.com/ansible/latest/modules/git_module.html#git-module). |
| `janus_git_force` | `false` | Whether or not to force clone Janus every time the playbook runs. Passed directly to the `force` property of the Git module. |
| `janus_user` | `[]` | The user to install Janus for. Should include both `name` and `group` properties. |
| `janus_user.name` | `-` | The name of the user to install Janus for. |
| `janus_user.group` | `-` | The group of the user to install Janus for. |
| `janus_backup_files` | `[]` | A list of Vim-related files in the user's home directory that should be backed up when the playbook runs. Might include e.g. `.vim`, `.vimrc` etc. |
| `janus_vim_plugins` | `[]` | A list of Vim plugins to install from Github. Each should include properties for `name`, `url`, and `version`. |
| `janus_vim_plugins[n].name` | `-` | The name of the plugin to install. Used for the `dest` parameter of the Git module when cloning. |
| `janus_vim_plugins[n].url` | `-` | The url of the plugin to install. Used for the `repo` parameter of the Git module when cloning. |
| `janus_vim_plugins[n].version` | `HEAD` | The version of the plugin to install. Used for the `version` parameter of the Git module when cloning. |
| `janus_vim_plugins[n]force` | `false` | Whether or not to force-clone the plugin. Used for the `force` parameter of the Git module when cloning. |
| `janus_vim_plugins[n]updaterepo` | `true` | Whether or not to update the plugin repo. Used for the `update` parameter of the Git module when cloning. |

## Role task fileso

### `main.yml`: task coordination

This file includes files that perform specific subsets of tasks.

#### Variables used

- `janus_required_packages`
- `janus_backup_files`
- `janus_vim_plugins`

### `preinstall.yml`

This task pre-installs any packages required by the role.

#### Variables used

- `janus_required_packages`

### `backup.yml`

This task backs up defined Vim-related files and directories (e.g.
`.vim`, `.vimrc`, etc).

#### Variables used

- `janus_user`

### `install.yml`

This task installs Janus.

#### Variables used

- `janus_git_repo`
- `janus_version`
- `janus_git_force`
- `janus_user`

### `plugins.yml`

This task installs any defined modules into the appropriate directory
(`~/user/.janus`).

#### Variables used

- `janus_user`
- `janus_vim_plugins`

## Sample playbook

    ---
    - name: Playbook
      hosts: all
      vars:
        users:
          - name: "lorem"
            group: "lorem"
          - name: "ipsum"
            group: "ipsum"
        janus_vim_plugins:
          - name: "lightline.vim"
            url: "https://github.com/itchyny/lightline.vim"
            updaterepo: false
          - name: "vim-surround"
            url: "https://github.com/tpope/vim-surround.git"
            updaterepo: true
        janus_backup_files:
          - ".vimrc"
      tasks:
        - name: Install Janus for users.
          include_role:
            name: "ansible-role-janus"
          vars:
            janus_user: "{{ user }}"
          with_items: "{{ users }}"
          loop_control:
            loop_var: user

## License

MIT
