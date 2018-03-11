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

Each resource should repect the following design :
(look at guests module for more details)

class Guests(GenericClass):

    def get_rbu(self):
        rbu = ResourceBuilder("guests")
        rbu.add_field('uuid')
        rbu.add_field('firstName', required=True)
        rbu.add_field('lastName', required=True)
        rbu.add_field('mail', required=True)
        return rbu

    @Time('list')
    @Cache()
    def list(self):
        url = "guests"
        return self.core.list(url)

    @Time('get')
    def get(self, uuid):
        """ Get one guest."""
        url = "guests/%(uuid)s" % {
            'uuid': uuid
        }
        return self.core.get(url)

    @Time('delete')
    @Invalid()
    def delete(self, uuid):
        """ Delete one guest."""
        res = self.get(uuid)
        url = "guests/%(uuid)s" % {
            'uuid': uuid
        }
        self.core.delete(url)
        return res

    @Time('update')
    @Invalid()
    def update(self, data):
        """ Update a guest."""
        self.debug(data)
        url = "guests"
        return self.core.update(url, data)

    @Time('create')
    @Invalid()
    def create(self, data):
        self.debug(data)
        self._check(data)
        url = "guests"
        return self.core.create(url, data)
