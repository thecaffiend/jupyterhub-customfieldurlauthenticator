# jupyterhub-customfieldurlauthenticator

Authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that allows authentication against a url, but also checks the response for  
against a configurable set of fields from the config object.

All keys in the config dict need to be in the response for the authentication
to succeed, and the values for each key need to match what comes back in the
response.

In addition to the custom fields dict, the username is also retrieved from the
response. If all custom fields validate, and the username is in the response,
the authentication will succeed.

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

# custom response fields to include in validation. this will check the response
# for ['some_key'] == True for example.
c.CustomFieldUrlAuthenticator.custom_fields = dict(some_key=True)

```

## Installation
```
pip install [-e] git+git://github.com/thecaffiend/jupyterhub-customfieldurlauthenticator.git
```
depends on [jupyterhub-urlauthenticator](http://github.com/thecaffiend/jupyterhub-urlauthenticator)


## TODO
* get this on pypi
* make authenticator smarter about trailing/leading slashes in URL/routes
* add a way to specify header values (right now json only)
* Add error handling.
* tests
* better code/auto doc

## Other
