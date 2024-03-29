#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""TODO"""


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
# Copyright 2014 Frédéric MARTIN
#
# Contributors list :
#
#  Frédéric MARTIN frederic.martin.fma@gmail.com
#

from linshareapi.core import CoreCli
from linshareapi.core import ApiNotImplementedYet as ANIY
from linshareapi.core import GenericClass
from linshareapi.admin.domains import Domains
from linshareapi.admin.domains import Domains2
from linshareapi.admin.domains import Domains5
from linshareapi.admin.domainpatterns import DomainPatterns
from linshareapi.admin.domainpatterns import DomainPatterns2
from linshareapi.admin.functionalities import Functionalities
from linshareapi.admin.functionalities import Functionalities5
from linshareapi.admin.threads import Threads
from linshareapi.admin.threadmembers import ThreadsMembers
from linshareapi.admin.threadmembers import ThreadsMembers2
from linshareapi.admin.shared_spaces import SharedSpaces
from linshareapi.admin.shared_spaces import SharedSpacesV5
from linshareapi.admin.users import Users
from linshareapi.admin.iusers import InconsistentUsers
from linshareapi.admin.ldapconnections import LdapConnections
from linshareapi.admin.ldapconnections import LdapConnections2
from linshareapi.admin.domainpolicies import DomainPolicies
from linshareapi.admin.upgradetasks import UpgradeTasks
from linshareapi.admin.welcomemessages import WelcomeMessages
from linshareapi.admin.public_keys import PublicKeys
from linshareapi.admin.jwt import Jwt
from linshareapi.admin.authentication import Authentication
from linshareapi.admin.mail_configs import MailConfigs
from linshareapi.admin.mail_attachments import MailAttachments
from linshareapi.admin.mail_activations import MailActivations


class AdminCli(CoreCli):
    """TODO"""
    # pylint: disable=too-many-instance-attributes

    VERSION = 2.2
    VERSIONS = [0, 1, 2, 2.2]
    VERSIONS = [0, 1, 2, 2.2, 4.0, 4.1, 4.2, 5]

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-statements
    def __init__(self, host, user, password, verbose, debug, api_version=None,
                 verify=True, auth_type="plain"):
        super().__init__(host, user, password, verbose, debug,
                         verify=verify, auth_type=auth_type)
        self.log.debug("api_version : %s", api_version)
        if api_version is None:
            api_version = self.VERSION
        if api_version not in self.VERSIONS:
            raise ValueError("API version not supported : " + str(api_version))
        self.base_url = "linshare/webservice/rest/admin"
        # Default API
        self.threads = ANIY(self, api_version, "threads")
        self.thread_members = ANIY(self, api_version, "thread_members")
        self.users = ANIY(self, api_version, "users")
        self.iusers = ANIY(self, api_version, "iusers")
        self.domains = ANIY(self, api_version, "domains")
        self.ldap_connections = ANIY(self, api_version, "ldap_connections")
        self.domain_patterns = ANIY(self, api_version, "domain_patterns")
        self.funcs = ANIY(self, api_version, "funcs")
        self.domain_policies = ANIY(self, api_version, "domain_policies")
        self.public_keys = ANIY(self, api_version, "public_keys")
        self.jwt = ANIY(self, api_version, "jwt")
        self.authentication = Authentication(self)
        self.mail_configs = MailConfigs(self)
        self.raw = GenericClass(self)
        self.mail_attachments = ANIY(self, api_version, "mail_attachments")
        self.shared_spaces = ANIY(self, api_version, "shared_spaces")
        # API declarations
        if api_version == 0:
            self.threads = Threads(self)
            self.thread_members = ThreadsMembers(self)
            self.users = Users(self)
            self.iusers = InconsistentUsers(self)
            self.domains = Domains(self)
            self.ldap_connections = LdapConnections(self)
            self.domain_patterns = DomainPatterns(self)
            self.funcs = Functionalities(self)
            self.domain_policies = DomainPolicies(self)
        elif api_version == 1:
            self.threads = Threads(self)
            self.thread_members = ThreadsMembers(self)
            self.users = Users(self)
            self.iusers = InconsistentUsers(self)
            self.domains = Domains(self)
            self.ldap_connections = LdapConnections2(self)
            self.domain_patterns = DomainPatterns2(self)
            self.welcome_messages = WelcomeMessages(self)
            self.funcs = Functionalities(self)
            self.domain_policies = DomainPolicies(self)
            self.mail_activations = MailActivations(self)
        elif 2 <= api_version < 5:
            self.threads = Threads(self)
            self.thread_members = ThreadsMembers2(self)
            self.users = Users(self)
            self.iusers = InconsistentUsers(self)
            self.domains = Domains2(self)
            self.ldap_connections = LdapConnections2(self)
            self.domain_patterns = DomainPatterns2(self)
            self.funcs = Functionalities(self)
            self.domain_policies = DomainPolicies(self)
            self.upgrade_tasks = UpgradeTasks(self)
            self.welcome_messages = WelcomeMessages(self)
            self.public_keys = PublicKeys(self)
            self.mail_activations = MailActivations(self)
        if 2.2 <= api_version < 5:
            self.jwt = Jwt(self)
            self.shared_spaces = SharedSpaces(self)
            self.mail_attachments = MailAttachments(self)
        if api_version >= 4:
            self.base_url = "linshare/webservice/rest/admin/v4"
        if api_version >= 5:
            self.base_url = "linshare/webservice/rest/admin/v5"
            self.domains = Domains5(self)
            self.funcs = Functionalities5(self)
            self.shared_spaces = SharedSpacesV5(self)
