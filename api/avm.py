# avax-python : Python tools for the exploration of the Avalanche AVAX network.
#
# Documentation at https://crypto.bi

"""

Copyright © 2021 ojrdev

Support this Open Source project!
Donate to X-avax1qr6yzjykcjmeflztsgv6y88dl0xnlel3chs3r4

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

# --#--#--


import avaxpython
import jsrpc

caller = avaxpython.get_caller()

def buildGenesis(genesisData):

    data = {
        "genesisData": genesisData
    }

    return caller("avm.buildGenesis", data)


def importKey(privateKey, username, password):

    data = {
        "privateKey": privateKey,
        "username": username,
        "password": password
    }

    return caller("avm.importKey", data)


def exportKey(address, username, password):

    data = {
        "address": address,
        "username": username,
        "password": password
    }

    return caller("avm.exportKey", data)


def exportAVA(to_addr, amt, username, password):

    data = {
        "to": to_addr,
        "amount": int(amt),
        "username": username,
        "password": password
    }

    return caller("avm.exportAVA", data)


def importAVA(to, username, password):

    data = {
        "to": to,
        "username": username,
        "password": password
    }

    return caller("avm.importAVA", data)


def getAllBalances(address):

    data = {
        "address": address
    }

    return caller("avm.getAllBalances", data)


def getBalance(address, assetID):

    data = {
        "address": address,
        "assetID": assetID
    }

    return caller("avm.getBalance", data)


def getUTXOs(addresses):

    data = {
        "addresses": addresses
    }

    return caller("avm.getUTXOs", data)


def getTxStatus(txID):

    data = {
        "txID": txID
    }

    return caller("avm.getTxStatus", data)


def createAddress(username, password):

    data = {
        "username": username,
        "password": password
    }

    return caller("avm.createAddress", data)


def listAddresses(username, password):

    data = {
        "username": username,
        "password": password
    }

    return caller("avm.listAddresses", data)


def issueTx(tx):

    data = {
        "tx": tx
    }

    return caller("avm.issueTx", data)


def signMintTx(tx, minter, username, password):

    data = {
        "tx": tx,
        "minter": minter,
        "username": username,
        "password": password
    }

    return caller("avm.signMintTx", data)


def createMintTx(amount, assetID, to, minters):

    data = {
        "amount": amount,
        "assetID": assetID,
        "to": to,
        "minters": minters
    }

    return caller("avm.createMintTx", data)



def send(amount, assetID, to, username, password):

    data = {
        "amount": amount,
        "assetID": assetID,
        "to": to,
        "username": username,
        "password": password
    }

    return caller("avm.send", data)


def createFixedCapAsset(name, symbol, denomination, initialHolders, username, password):

    """
     initialHolders = [{
        address: string,
        amount: int
    }, ...]
    """

    data = {
        "name": name,
        "symbol": symbol,
        "denomination": denomination,
        "initialHolders": initialHolders,
        "username": username,
        "password": password
    }

    return caller("avm.createFixedCapAsset", data)



def createVariableCapAsset(name, symbol, denomination, minterSets, username, password):

    """
     minterSets = [{
        minters: [string],
        threshold: int
    }, ...]
    """

    data = {
        "name": name,
        "symbol": symbol,
        "denomination": denomination,
        "minterSets": minterSets,
        "username": username,
        "password": password
    }

    return caller("avm.createVariableCapAsset", data)


def getAssetDescription(assetID):

    data = {
        "assetID": assetID
    }

    return caller("avm.getAssetDescription", data)


