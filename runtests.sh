#!/bin/sh

# avax-python : Python tools for the exploration of the Avalanche AVAX network.
#
# Documentation at https://crypto.bi

# Copyright © 2021 ojrdev

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# --#--#--

# Note: We ignore the 3rdparty/ test suites here because some of them raise random errors under pytest (module loading, etc). 
# Run each 3rdparty module's test suite individually as specified by their documentation.

. ./setenv.sh

export PYTHONPATH=$PYTHONPATH:$ppath/3rdparty/py_crypto_hd_wallet/
export PYTHONPATH=$PYTHONPATH:$ppath/3rdparty/cb58ref/

pytest --ignore=3rdparty/cb58ref/tests/ --ignore=3rdparty/py_crypto_hd_wallet/tests/ --ignore=3rdparty/bip_utils/tests/ --ignore=3rdparty/python-mnemonic/