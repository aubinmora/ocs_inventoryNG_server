# ocs_inventoryNG_server
Ansible role for OCS inventory NG

# Tested

Tested on CentOS 7, Debian 9.X, currently working with no issue (might as well work on RedHat and Fedora, the main difference would be the dependancies)


Ubuntu semi-works, as there is issues between mariaDB and AppArmor.
It is also really slow, break packages dependancies, only allow last version of PHP natively, etc... . This distribution will only receive minimal support.

# How can it be useful?

If OCS is the only service running on your server, dump the base, rebuild it from the ground up, upload the base on the new, then break the old one. OCS up and running depending mainly on your internet speed. New features without the need to get through the hassle of figuring out what's wrong as it just works. (or don't, depends if you like Ubuntu)

# How to use the Role:

There is little to edit in the config files. For most users, editing the common_vars.yml file on the user, password and database name would suffice. More customisation is allowed as most of the non static parameters are in a var file.

# About the Author

There is little to gain by writing such a role (somehow time consuming to say the least), it was done mainly as a form of practice, might as well share. I will edit it if changes are needed. Please notify me if something breaks/If you have improvements in mind.

[![Build Status](https://travis-ci.org/aubinmora/ansible-apache.svg?branch=master)](https://travis-ci.org/username/ansible-apache)
