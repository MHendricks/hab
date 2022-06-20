This folder contains examples of configuring Hab.

* 1_site is an example of a general site level configuration.
* 2_host is an example of extending the site level configuration with distros and configs per individual host.
* 3_developer is an example of how a developer can setup their environment for testing easily.

Depending on your requirements you may want to define a 3 tiered site configuration allowing for site level configuration with host and user level configurations. For example:
`HAB_PATH=~/.hab_user.json:/opt/hab/hab_host.json:/mnt/network/share/hab_site.json`

This will use distros and configs from all 3 locations. If there are duplicates, the left most path where it is defined is used.
