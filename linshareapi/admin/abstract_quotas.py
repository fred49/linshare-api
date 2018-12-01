#! /usr/bin/env python
# -*- coding: utf-8 -*-


# This file is part of Linshare api.
#
# LinShare api is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LinShare api is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LinShare api.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2018 Frédéric MARTIN
#
# Contributors list :
#
#  Frédéric MARTIN frederic.martin.fma@gmail.com
#


from __future__ import unicode_literals
import urllib
from linshareapi.core import ResourceBuilder
from linshareapi.cache import Cache as CCache
from linshareapi.cache import Invalid as IInvalid
from linshareapi.admin.core import GenericClass
from linshareapi.admin.core import Time as CTime
from linshareapi.admin.core import CM

# pylint: disable=C0111
# Missing docstring
# pylint: disable=R0903
# Too few public methods
# -----------------------------------------------------------------------------
class Time(CTime):
    def __init__(self, suffix, **kwargs):
        super(Time, self).__init__('quota.' + suffix, **kwargs)


# -----------------------------------------------------------------------------
class Cache(CCache):
    def __init__(self, **kwargs):
        super(Cache, self).__init__(CM, 'quota', **kwargs)


# -----------------------------------------------------------------------------
class Invalid(IInvalid):
    def __init__(self, **kwargs):
        super(Invalid, self).__init__(CM, 'quota', **kwargs)


# -----------------------------------------------------------------------------
class AbstractQuota(GenericClass):

    local_base_url = "quotas"

    def get_rbu(self):
        rbu = ResourceBuilder("quotas")
        rbu.add_field('uuid', required=True)
        rbu.add_field('domain')
        rbu.add_field('modificationDate')
        rbu.add_field('creationDate')
        return rbu

    @Time('invalid')
    @Invalid()
    def invalid(self):
        return "invalid : ok"

    @Time('list')
    @Cache()
    def list(self):
        url = "{base}".format(
            base=self.local_base_url
        )
        return self.core.list(url)

    @Time('get')
    def get(self, uuid):
        url = "{base}/{uuid}".format(
            base=self.local_base_url,
            uuid=uuid
        )
        return self.core.get(url)

    @Time('update')
    @Invalid()
    def update(self, data):
        """ Update a list."""
        self.debug(data)
        url = "{base}/{uuid}".format(
            base=self.local_base_url,
            uuid=data.get('uuid')
        )
        return self.core.update(url, data)
