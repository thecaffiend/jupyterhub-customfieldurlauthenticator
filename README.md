# jupyterhub-customfieldurlauthenticator

Authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that allows authentication against a url, but also checks the response for a  
against a configurable set of fields from the config object.

## Usage
After installation, you can then use the authenticator by adding the following
lines to your `jupyterhub_config.py` (replacing square bracket items with your
values):

```
c.JupyterHub.authenticator_class = 'customfieldurlauthenticator.CustomFieldUrlAuthenticator'
c.CustomFieldUrlAuthenticator.server_address = 'http://[address]'
c.CustomFieldUrlAuthenticator.server_port = [port]
# This does no magic with slashes. If you require a trailing one and it's not
# provided, this will error now. Same with leading slash (NEEDED FOR NOW)
c.CustomFieldUrlAuthenticator.login_route = '[/path/to/login/service]'
```

## Installation
```
pip install [-e] git+git://github.com/theaffiend/jupyterhub-customfieldurlauthenticator.git
```
depends on jupyterhub-urlauthenticator


## TODO
* get this on pypi
* make authenticator smarter about trailing/leading slashes in URL/routes
* add a way to specify header values (right now json only)
* Add error handling.
* tests
* better code/auto doc

## Other
