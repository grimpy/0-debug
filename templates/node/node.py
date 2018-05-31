from js9 import j
from zerorobot.template.base import TemplateBase

CONTAINER_TEMPLATE_UID = 'github.com/zero-os/0-templates/container/0.0.1'
VM_TEMPLATE_UID = 'github.com/zero-os/0-templates/vm/0.0.1'
BOOTSTRAP_TEMPLATE_UID = 'github.com/zero-os/0-templates/zeroos_bootstrap/0.0.1'
ZDB_TEMPLATE_UID = 'github.com/zero-os/0-templates/zerodb/0.0.1'
NODE_CLIENT = 'local'


class Node(TemplateBase):

    version = '0.0.1'
    template_name = 'node'

    def __init__(self, name, guid=None, data=None):
        super().__init__(name=name, guid=guid, data=data)

    @property
    def node_sal(self):
        """
        connection to the node
        """
        return j.clients.zos.sal.get_node(NODE_CLIENT)

    def system(self, command):
        return self._process_result(self.node_sal.client.system(command).get())

    def _process_result(self, result):
        return {
            'code': result.code,
            'data': result.data,
            'stdout': result.stdout,
            'stderr': result.stderr,
        }

    def open_port(self, port):
        return self.node_sal.client.nft.open_port(port)

    def bash(self, command):
        return self._process_result(self.node_sal.client.bash(command).get())

    def add_github_user(self, user):
        return self.system('ssh-add-github-key {}'.format(user))


