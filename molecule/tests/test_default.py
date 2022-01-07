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
        "/etc/systemd/user/create-fileshare-symlink.service",
        "/usr/share/backgrounds/cool/cisa_cool_retro_0.png",
        "/etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml",
        "/etc/xdg/qterminal.org/qterminal.ini",
    ],
)
def test_files_exist(host, f):
    """Test that the appropriate files were copied over or already existed."""
    assert host.file(f).exists


@pytest.mark.parametrize(
    "d,count",
    [
        # This directory should contain _only_ cisa_cool_retro_0.png.
        ("/usr/share/backgrounds/cool/", 1),
    ],
)
def test_extra_files_do_not_exist(host, d, count):
    """Test that undesired files WERE NOT copied over.

    This test was created to ensure that #13 is resolved and stays
    resolved.

    """
    assert len(host.file(d).listdir()) == count


# This test is commented out until #29 is resolved.
# def test_symlink_exists(host):
#     """Test that the file share symlink exists for the test user.

#     Note that this test is dependent on the side_effect playbook being
#     run.
#     """
#     f = host.file("/home/test/Desktop/share")
#     assert f.exists
#     assert f.is_symlink
#     assert f.linked_to == "/share"
#     assert f.user == "test"
#     assert f.group == "test"
