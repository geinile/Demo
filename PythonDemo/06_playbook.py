from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor

def rundb(hosts_lists,playbooks):
    Options = namedtuple('Options',
                         ['connection',
                          'remote_user',
                          'ask_sudo_pass',
                          'verbosity',
                          'ask_pass',
                          'module_path',
                          'forks',
                          'become',
                          'become_method',
                          'become_user',
                          'check',
                          'listhosts',
                          'listtasks',
                          'listtags',
                          'syntax',
                          'sudo_user',
                          'sudo',
                          'diff'])
    options = Options(connection='smart',
                      remote_user=None,
                      ask_pass=None,
                      sudo_user=None,
                      forks=5,
                      sudo=None,
                      ask_sudo_pass=False,
                      verbosity=5,
                      module_path=None,
                      become=None,
                      become_method=None,
                      become_user=None,
                      check=False,
                      diff=False,
                      listhosts=None,
                      listtasks=None,
                      listtags=None,
                      syntax=None)
    loader = DataLoader()                   #转换器,转换成python语法
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=hosts_lists)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    playbook = PlaybookExecutor(
        playbooks=playbooks,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=options,
        passwords=passwords
    )
    result = playbook.run()
    print(result)

if __name__ == '__main__':
        rundb(['/var/ansible/hosts'],['/var/ansible/twoplay.yaml'])