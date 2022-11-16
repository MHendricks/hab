This is an example of a 3 tiered configuration. The majority of configuration is served
by a network file server all hosts connect to. This can be extended by host specific
configurations for locally installed applications.

Users can customize the configuration even more by adding user specific configurations.
This allows developers to easily test their changes directly from the svc checkouts
without needing to deploy code changes.

Example of how this could be configured for a given host.
`HAB_PATH=~/.hab_user.json:/opt/hab/hab_host.json:/mnt/network/share/hab_site.json`

```bash
$ cd examples/site_host_user/
$ export HAB_PATHS="./3_developer/dev.json;./2_host/host.json;./1_site/site.json"
$ hab dump app/mayas
WARNING:hab.parsers.hab_base:Can not add "C:\blur\dev\hab\examples\site_host_user\1_site\configs\default.json", the context "default" it is already set
Dump of FlatConfig('app/mayas')
--------------------------------------------------------------
aliases:  maya maya20 mayapy mayapy20 maya23 mayapy23
--------------------------------------------------------------
```
NOTE: Using a relative path in `HAB_PATH` is not recommended, however hab will expand
`~` and environment variables.


* 1_site is an example of a general site level configuration.
* 2_host is an example of extending the site level configuration with distros and configs per individual host.
* 3_developer is an example of how a developer can setup their environment for testing easily.

This will use distros and configs from all 3 locations. If there are duplicates, the
left most path where it is defined is used. The warning printed lets you know that site
level implementation of default.json is already configured. In this case a developer copy.
