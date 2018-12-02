# Architecture

The linshare-api module is designed to contain all LinShare API.
This module contains resource definions and CRUD methods.

APIs:
  - user:
    - guests
    - documents
    - shares
    - ...
  - admin:
    - domains
    - functionalities
    - ...

The main class is named CoreCli, this class contains all default methods
(authentication, parsers, helpers, ...) for building a new API.
For now, there is only two API: UserCli and AdminCli.

UserCli is defined in user/__init__. This API support multiple versions
of LinShare for each endpoints.

# Usage

```python
from linshareapi.user import UserCli
host="http://localhost:8080"
user="user1@linshare.org"
password="password1"
verbose = True
debug = 1

cli = UserCli(host, user, password, verbose, debug)
cli.nocache = True
cli.auth()
data = cli.documents.list()
print data[0]
```

# Resource definition

  * How to add a new endoint in the admin API

    * Duplicate the file template_api.py to a new file, use the resource name as the file name:
      * file name: my_resources.py
      * class name: class MyResources(GenericClass):

    * Add the new endpoint to AdminCli in admin/__init__.py
      * endpoint name: self.my_resources = MyResources(self)
