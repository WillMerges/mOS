# Multi Operating System (mOS)
# Copyright (c) 2016, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

from mostests import *

logger = logging.getLogger()

GiB = 1024**3
MiB = 1024**2
KiB = 1024**1

class Basics(TestCase):
    require = [YOD, 'gup_test']
    modules = ['gup_module.ko']

    def test_memory(self):
        # Verify that get_user_pages works with LWK memory.
        yod(self, './gup_test', '-f', requiresRoot=True)

    def test_do_not_split_huge_pages(self):
        # Verify that get_user_pages works with LWK memory having large pages.
        yod(self, './gup_test', '-f', '-S', 2 * GiB, requiresRoot=True)

    def test_split_huge_pages(self):
        # Verify that get_user_pages works with LWK memory after splitting large pages.
        yod(self, './gup_test', '-f', '-S', 2 * GiB, '-b', requiresRoot=True)
