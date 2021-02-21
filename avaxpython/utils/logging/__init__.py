# avax-python : Python tools for the exploration of the Avalanche AVAX network.
#
# Documentation at https://crypto.bi

"""

Copyright © 2021 ojrdev

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

# --#--#--


from avaxpython.Config import Config
from avaxpython.utils import logging

# Factory ...
class Factory:
    def __init__(self):
        pass

# factory ...
class factory:

    def __init__(self):
	    self.config = Config()
	    self.loggers = []

    # Make ...
    def Make(self):
        l, err = New(f.config)
        if err == None:
            self.loggers.append(l)
        
        return l, err

    # MakeChain ...
    def MakeChain(self, chainID, subdir):
        config = f.config
        config.MsgPrefix = chainID + " Chain"
        config.Directory = filepath.Join(config.Directory, "chain", chainID, subdir)

        log, err = New(config)
        if err == nil:
            f.loggers.append(log)
        
        return log, err


    # MakeSubdir ...
    def MakeSubdir(self, subdir):
        config = f.config
        config.Directory = filepath.Join(config.Directory, subdir)

        log, err = New(config)
        if err == nil:
            f.loggers.append(log)
        
        return log, err


    # Close ...
    def Close(self):
        for _, log in f.loggers:
            log.Stop()
        
        f.loggers = nil



# NewFactory ...
def NewFactory(config: Config):
	return factory(config=config)
	