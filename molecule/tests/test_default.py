"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_packages(host):
    """Test that the appropriate packages were installed."""
    pkgs = None
    if (
        (
            host.system_info.distribution == "debian"
            and host.system_info.codename != "stretch"
        )
        or host.system_info.distribution == "fedora"
        or host.system_info.distribution == "kali"
        or host.system_info.distribution == "ubuntu"
    ):
        pkgs = ["curl", "python3-lxml"]
    elif (
        host.system_info.distribution == "debian"
        and host.system_info.codename == "stretch"
    ):
        pkgs = ["curl", "python-lxml"]
    else:
        # This is an unknown OS, so force the test to fail
        assert False

    for pkg in pkgs:
        assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "f",
    [
        "/etc/xdg/autostart/cool-data-shortcut.desktop",
        "/usr/share/backgrounds/cool/cisa_cool_retro_0.png",
        "/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml",
        "/etc/xdg/qterminal.org/qterminal.ini",
    ],
)
def test_files_exist(host, f):
    """Test that the appropriate files were copied over or already existed."""
    assert host.file(f).exists
