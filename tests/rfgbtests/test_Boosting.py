"""
Copyright (C) 2017-2018 RFGB Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (at the base of this repository). If not,
see <http://www.gnu.org/licenses/>
"""

from __future__ import print_function

import sys
import unittest

sys.path.append('./')

import rfgb.Boosting

class BoostingTest(unittest.TestCase):

    def test_foo(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
