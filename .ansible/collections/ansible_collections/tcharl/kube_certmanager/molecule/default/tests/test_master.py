"""Role testing files using testinfra."""
testinfra_hosts = ["master.osgiliath.test"]


def test_cert_manager_pods_running(host):
    command = r"""
    kubectl get pods -n cert-manager | \
    grep Running | \
    wc -l"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0


# def test_cert_manager_user_exists(host):
#    command = r"""set -o pipefail && echo '123ADMin'| \
#    kinit admin > /dev/null && \
#    ipa user-find cert-manager-sa | \
#    grep -c 'First name: Cert'"""
#    cmd = host.run(command)
#    assert '1' in cmd.stdout


# def test_freeipa_issuer_pods_running(host):
#    command = r"""
#    kubectl get pods -n freeipa-issuer-system | \
#    grep Running | \
#    wc -l"""
#    with host.sudo():
#        cmd = host.run(command)
#        assert int(cmd.stdout) > 0

def test_certmanager_config_cabundle(host):
    command = r"""
    kubectl get cm ca-bundle -n cert-manager | \
    wc -l"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0


def test_certmanager_config_cabundle_content_ca(host):
    command = r"""
    kubectl get cm ca-bundle -n cert-manager -o yaml | \
    grep 'BEGIN CERTIFICATE' | \
    wc -l"""
    with host.sudo():
        cmd = host.run(command)
        assert int(cmd.stdout) > 0
