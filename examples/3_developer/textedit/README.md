This folder can be a git(svn, etc) checkout of the textedit repo. The habitat version
number is likely defined by adding a git ignored `.hab_version.txt` file, or
using setuptools_scm to pull the version number directly from git(with or without
defining a pip package). See
[Specifying distro version](https://github.com/blurstudio/habitat#specifying-distro-version)
for more details.

```bash
$ hab --site /c/blur/dev/hab/examples/3_developer/dev.json --site /c/blur/dev/hab/examples/1_site/site.json dump project_a -vvv
py -3.7
Dump of FlatConfig('default')
-------------------------------------------------------------------------------------------------------------
name:  default
uri:  project_a
aliases:  maya:  C:\Program Files\Autodesk\Maya2023\bin\maya.exe
          maya23:  C:\Program Files\Autodesk\Maya2023\bin\maya.exe
          mayapy:  C:\Program Files\Autodesk\Maya2023\bin\mayapy.exe
          mayapy23:  C:\Program Files\Autodesk\Maya2023\bin\mayapy.exe
          textedit:  notepad.exe
distros:  maya2023:  maya2023
          textedit:  textedit

inherits:  False
versions:  maya2023==2023.0:  C:\blur\dev\hab\examples\1_site\distros\maya\2023.0\.hab.json
           textedit==1.0.0:  C:\blur\dev\hab\examples\3_developer\textedit\.hab.json
-------------------------------------------------------------------------------------------------------------
````

You can see that its pulling in the textedit from 3_developer instead of the one defined in 1_site.
