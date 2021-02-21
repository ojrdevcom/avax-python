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


from avaxpython.utils import nlimits
from avaxpython.utils.wrappers.Packer import Packer

class Field:

    # Fields that may be packed. These values are not sent over the wire.
    VersionStr = 0
    NetworkID = 1
    NodeID = 2
    MyTime = 3
    IP = 4
    Peers = 5
    ChainID = 6
    RequestID = 7
    Deadline = 8
    ContainerID = 9
    ContainerBytes = 10
    ContainerIDs = 11
    MultiContainerBytes = 12

    # estao no packer
    __op_packer = {
        VersionStr: Packer.TryPackStr,
        NetworkID: Packer.TryPackInt,
        NodeID: Packer.TryPackInt,
        MyTime: Packer.TryPackLong,
        IP: Packer.TryPackIP,
        Peers: Packer.TryPackIPList,
        ChainID: None, # TODO: This will be shortened to use a modified varint spec Packer.TryPackHash
        RequestID: Packer.TryPackInt,
        Deadline: Packer.TryPackLong,
        ContainerID: Packer.TryPackHash,
        ContainerBytes: Packer.TryPackBytes,
        ContainerIDs: Packer.TryPackHashes,
        MultiContainerBytes: Packer.TryPack2DBytes,
    }

    __op_unpacker = {
        VersionStr: Packer.TryUnpackStr,
        NetworkID: Packer.TryUnpackInt,
        NodeID: Packer.TryUnpackInt,
        MyTime: Packer.TryUnpackLong,
        IP: Packer.TryUnpackIP,
        Peers: Packer.TryUnpackIPList,
        ChainID: None, # TODO: This will be shortened to use a modified varint spec Packer.TryUnpackHash
        RequestID: Packer.TryUnpackInt,
        Deadline: Packer.TryUnpackLong,
        ContainerID: Packer.TryUnpackHash,
        ContainerBytes: Packer.TryUnpackBytes,
        ContainerIDs: Packer.TryUnpackHashes,
        MultiContainerBytes: Packer.TryUnpack2DBytes    
    }

    __op_string = {
        VersionStr: "VersionStr",
        NetworkID: "NetworkID",
        NodeID: "NodeID",
        MyTime: "MyTime",
        IP: "IP",
        Peers: "Peers",
        ChainID: "ChainID",
        RequestID: "RequestID",
        Deadline: "Deadline",
        ContainerID: "ContainerID",
        ContainerBytes: "Container Bytes",
        ContainerIDs: "Container IDs",
        MultiContainerBytes: "MultiContainerBytes",
    }

    # Packer returns the packer function that can be used to pack this field.
    # func(*Packer.Packer, interface{})
    @classmethod
    def Packer(cls, field):
        if field in cls.__op_packer: 
            return cls.__op_packer.get(field)
    
        raise Exception(f"Field {field} not found")


    # Unpacker returns the unpacker function that can be used to unpack this field.
    # ) func(*Packer.Packer) interface{}
    @classmethod
    def Unpacker(cls, field):
        if field in cls.__op_unpacker: 
            return cls.__op_packer.get(field)
    
        raise Exception(f"Field {field} not found")


    @classmethod
    def String(cls, field):
        if field in cls.__op_unpacker: 
            return cls.__op_packer.get(field)
    
        raise Exception(f"Field {field} not found")
