#!/usr/bin/env python
#coding=utf-8

import json
import argparse
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkslb.request.v20140515.SetVServerGroupAttributeRequest import SetVServerGroupAttributeRequest
parser = argparse.ArgumentParser()
parser.add_argument('-g', type=str, help='VServerGroupId')
parser.add_argument('-n', type=str, help='VServerGroupName')
parser.add_argument('-f', type=str, help='jsonfile')
args = parser.parse_args()

VServerGroupId=args.g
VServerGroupName=args.n
jsonfile=args.f

client = AcsClient('LTAI4Frg5i92SRmy6n6tvZXJ', '68oDPFLN64lafJTy9lIjYyK4RvaCgm', 'cn-shanghai')

request = SetVServerGroupAttributeRequest()
request.set_accept_format('json')
with open(jsonfile) as fp:
    tmpstr = fp.read()
    backendServerDict = json.loads(tmpstr)

request.set_VServerGroupId(VServerGroupId)
request.set_VServerGroupName(VServerGroupName)
backendServerStr="["+json.dumps(backendServerDict)+"]"
print backendServerStr
request.set_BackendServers(backendServerStr)

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response))
