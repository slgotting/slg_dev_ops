import os
import argparse


def install_nginx(os='ubuntu', codename='bionic'):

    os.system('sudo touch /etc/apt/sources.list.d/nginx.list')
    with open('/etc/apt/sources.list.d/nginx.list', 'w') as f:
        print(
            f'deb http://nginx.org/packages/mainline/{os}/ {codename} nginx',
            file=f)
        print(
            f'deb-src http://nginx.org/packages/mainline/{os}/ {codename} nginx',
            file=f)
    os.system('wget http://nginx.org/keys/nginx_signing.key')
    os.system('sudo apt-key add nginx_signing.key')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y nginx')
    os.system('sudo /etc/init.d/nginx start')

# The file you just created instructs the advanced package tool (APT) package management system to utilize the Official NGINX package repository. Modifying the file to provide the correct endpoint and code name for your distribution ensures that the APT utility receives the correct .deb packages for your system. The following commands download the NGINX GPG package signing key and import it into APT. Providing APT trhe signing key enables the APT system to validate packages from the repository. The apt-get update command instructs the APT system to refresh its package listings from its known repositories. After the package list is refreshed, you can install NGINX Open Source from the Official NGINX repository. After you install it, the final command starts NGINX.
