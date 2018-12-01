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
from linshareapi.core import ResourceBuilder
from linshareapi.admin.abstract_quotas import Time
# from linshareapi.admin.abstract_quotas import Cache
# from linshareapi.admin.abstract_quotas import Invalid
from linshareapi.admin.abstract_quotas import AbstractQuota


class ContainerQuotas(AbstractQuota):
    """TODO"""

    local_base_url = "quotas/containers"

    def get_rbu(self):
        rbu = ResourceBuilder("containers")
        rbu.add_field('uuid', required=True)
        rbu.add_field('domain')
        rbu.add_field('type')
        rbu.add_field('quota')
        rbu.add_field('quotaOverride')
        rbu.add_field('accountQuota')
        rbu.add_field('accountQuotaOverride')
        rbu.add_field('maxFileSize')
        rbu.add_field('maxFileSizeOverride')
        rbu.add_field('usedSpace')
        rbu.add_field('yersterdayUsedSpace', extended=True)
        rbu.add_field('maintenance', extended=True)
        rbu.add_field('defaultQuota', extended=True)
        rbu.add_field('defaultQuotaOverride', extended=True)
        rbu.add_field('defaultMaxFileSize', extended=True)
        rbu.add_field('defaultMaxFileSizeOverride', extended=True)
        rbu.add_field('defaultAccountQuota', extended=True)
        rbu.add_field('defaultAccountQuotaOverride', extended=True)
        rbu.add_field('parentDomain', hidden=True)
        rbu.add_field('modificationDate', extended=True)
        rbu.add_field('creationDate', extended=True)
        rbu.add_field('batchModificationDate', extended=True)
        return rbu


class DomainQuotas(AbstractQuota):
    """TODO"""

    local_base_url = "quotas/domains"

    def __init__(self, corecli):
        super(DomainQuotas, self).__init__(corecli)
        self.containers = ContainerQuotas(corecli)

    def get_rbu(self):
        rbu = ResourceBuilder("quotas")
        rbu.add_field('uuid', required=True)
        rbu.add_field('domain')
        rbu.add_field('quota')
        rbu.add_field('quotaOverride')
        rbu.add_field('defaultQuota')
        rbu.add_field('defaultQuotaOverride')
        rbu.add_field('usedSpace')
        rbu.add_field('currentValueForSubdomains')
        rbu.add_field('maintenance', extended=True)
        rbu.add_field('parentDomain', extended=True)
        rbu.add_field('domainShared', extended=True)
        rbu.add_field('domainSharedOverride', extended=True)
        rbu.add_field('defaultDomainShared', extended=True)
        rbu.add_field('defaultDomainSharedOverride', extended=True)
        rbu.add_field('yersterdayUsedSpace', extended=True)
        rbu.add_field('modificationDate', extended=True)
        rbu.add_field('creationDate', extended=True)
        rbu.add_field('batchModificationDate', extended=True)
        return rbu
