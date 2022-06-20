These configurations use hard coded file paths instead of relative_roots. This allows
you to specify the location of maya without needing to add a .hab.json file on each
computer. This lets you centrally define that maya 2023 should be installed on every
host and where it is installed to, but has the disadvantage that maya 2023 has to be
installed on every host, and in the same location. An alternative is to define a site
configuration that is installed on each host similar to what you see in the
[examples/2_host](examples/2_host) folder.


You will notice that we are making separate distro's for each year release of maya.
In this case `maya2020` and `maya2023`. This allows you to provide access to two
versions of maya in a single environment.

```bash
$ hab --site examples/1_site/site.json dump app/mayas -vvv
Dump of FlatConfig('app/mayas')
-------------------------------------------------------------------------------------------------------------
name:  mayas
uri:  app/mayas
aliases:  maya:  /usr/autodesk/maya2023/bin/maya
          maya20:  /usr/autodesk/maya2020/bin/maya
          mayapy:  /usr/autodesk/maya2023/bin/mayapy
          mayapy20:  /usr/autodesk/maya2020/bin/mayapy
          maya23:  /usr/autodesk/maya2023/bin/maya
          mayapy23:  /usr/autodesk/maya2023/bin/mayapy
distros:  maya2020:  maya2020
          maya2023:  maya2023
inherits:  False
versions:  maya2020==2020.1:  /home/computer/user/hab/examples/1_site/distros/maya/2020.1/.hab.json
           maya2023==2023.0:  /home/computer/user/hab/examples/1_site/distros/maya/2023.0/.hab.json
-------------------------------------------------------------------------------------------------------------
````

In this you can see the maya alias is using maya2023. This is because maya2023 is the
last distro in the distros list defining that alias in
[examples/1_site/configs/app_mayas.json](examples/1_site/configs/app_mayas.json).
This is also why we are defining maya20 and maya23. It lets users choose the desired
maya version. In most cases general users likely would be encouraged to simply use maya
and ignore the version specific aliases.
