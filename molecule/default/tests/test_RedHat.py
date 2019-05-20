import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('centos7')


@pytest.mark.parametrize('pkg', [
    'httpd',
    'firewalld'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'httpd',
    'firewalld'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize('file, content', [
    ("/etc/firewalld/zones/public.xml", "<service name=\"http\"/>")
])
def test_firewalld(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
