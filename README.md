# ocs_inventoryNG_server
Ansible role for OCS inventory NG

# Tested

Tested of CentOS 7, Debian 9.X, currently working with no issue (might as well work on RedHat and Fedora, the main difference would be the dependancies)


Ubuntu semi-works, as there is issues between mariaDB and AppArmor.
It is also really slow. This distribution will only receive feable support.

# How to use the Role:

There is little to edit in the config files. For most users, editing the common_vars.yml file on the user, password and database name would suffice. More customisation is allowed as most of the non static parameters are in a var file.

# About the Author

There is little to gain by writing such a role (somehow time consuming to say the least), it was done mainly as a form of practice, might as well share. I will edit it if changes are needed. Please notify me if something breaks/If you have improvements in mind.
