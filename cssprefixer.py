#!/usr/bin/env python
# CSSPrefixer
# Copyright 2010 MyFreeWeb <me@myfreeweb.ru>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        import cssprefixer
        result = ''
        if '--debug' in sys.argv:
            debug = True
        else:
            debug = False

        for arg in sys.argv[1:]:
            if arg != '--debug':
                result += cssprefixer.process(open(arg, 'r').read(), debug).cssText
        print result
    else:
        print "Usage: cssprefixer.py <filenames> --debug"