import os

import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "lorem",
    "ipsum",
])
@pytest.mark.parametrize("file", [
    ".vimrc",
])
def test_backup_files(host, name, file):
    n = host.run("find . -type f -name '{}.*' | wc -l".format(file))

    assert int(float(n.stdout)) > 0


@pytest.mark.parametrize("name", [
    "lorem",
    "ipsum",
])
def test_janus_install(host, name):
    d = host.file("/home/{0}/.vim/janus/vim/".format(name))

    assert d.exists
    assert d.user == name
    assert d.group == name


@pytest.mark.parametrize("name", [
    "lorem",
    "ipsum",
])
@pytest.mark.parametrize("plugin", [
    "lightline.vim",
    "vim-surround",
])
def test_plugin_install(host, name, plugin):
    d = host.file("/home/{0}/.janus/{1}".format(name, plugin))

    assert d.exists
    assert d.user == name
    assert d.group == name
