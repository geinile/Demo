#自定义ansible模块
#但是要export ANSIBLE_LIBRARY=/to/your/module/path,声明这个模块的位置
#调用:ansible all -m rcopy -a "yuan=/etc/hosts mubiao=/tmp/zhuji"


from ansible.module_utils.basic import AnsibleModule
import shutil

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mobiao=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mubiao'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()

