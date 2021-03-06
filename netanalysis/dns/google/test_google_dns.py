#!/usr/bin/python
#
# Copyright 2017 Jigsaw Operations LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ipaddress
import unittest

from . import google_dns as gdns


class TestGoogleDns(unittest.TestCase):

    def test_default_servers(self):
        google_dns = gdns.create_default_google_dns()
        self.assertIsNone(google_dns.get_server(
            ipaddress.ip_address("201.249.215.0")))
        server = google_dns.get_server(ipaddress.ip_address("74.125.80.128"))
        self.assertIsNotNone(server)
        self.assertEqual("dls", server.location_id)
        self.assertEqual("74.125.80.128", server.ip_address.compressed)


if __name__ == '__main__':
    unittest.main()
