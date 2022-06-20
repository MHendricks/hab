This folder defines the uri configurations. It allows you to define what distros to use.

`default.json` is used if the requested uri isn't defined. This lets you define a global
default configuration if you don't need to customize the setup for each individual
project. The user will still use the uri `project_z/bob`, but if there isn't a
configuration for bob or project_z it will fallback to the default configuration.

`app_mayas.json` shows an example of making a generic application launcher targeted at
maya, but not a specific project.
