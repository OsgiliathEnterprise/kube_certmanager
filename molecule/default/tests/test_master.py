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
