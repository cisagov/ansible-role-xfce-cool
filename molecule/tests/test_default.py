"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


# TODO: Add some meaningful tests for this Ansible role.
#
# See this issue:
# https://github.com/cisagov/ansible-role-xfce-cool/issues/6
@pytest.mark.parametrize("x", [True])
def test_packages(host, x):
    """Run a dummy test, just to show what one would look like."""
    assert x
