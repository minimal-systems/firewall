# package_install script for installing the package via the package manager 

import os
import shutil
import time


run_install_script():
    current_time = time.strftime("%Y%m%d%H%M%S")
    print('backing up the old rule...')
    shutil.copyfile('etc/firewall/rules.conf', f'/etc/firewall/rules.conf.bak{current_time}') #backup the old rules
    shutil.copyfile('tmp/package_install/firewall/rules.conf', '/etc/firewall/rules.conf') #copy the new rules
    shutil.copyfile('tmp/package_install/firewall/rules.conf', 'tmp/package_install/firewall/rules.conf.bak.new{current_time}') #backup the new rules
    print('syncing the new rules...')
    subproccess.call(['firewalld', '--reload']) #sync the new rules

if install_from_package_manager == True':
    try:
    run_install_script()
    else:
    print('failed to install the package. Please install from the packagte manager, or run "pam --install package_name --force --no-confirm"')