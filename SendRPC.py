import sys
import logging
import time

from lxml import etree
import xml.etree.ElementTree as ET
from ncclient import manager
from ncclient import operations
import base64

from xml.dom.minidom import parseString
import xml.dom.minidom

log = logging.getLogger(__name__)

# 不同厂家命名空间不一样
RPC_STRING1="""
         <get>
               <filter type="subtree">
                     <top xmlns="http://www.huawei.com/netconf/data:1.0">
                           <LLDP>
                                 <LLDPNeighbors></LLDPNeighbors>
                           </LLDP>
                     </top>
               </filter>
         </get>
"""
# 建立与设备的连接
def test_connection(host, port, user, password):
    return manager.connect(host=host, port=port, username=user, password=password, hostkey_verify=False, ssh_config=None, allow_agent=True, look_for_keys=False)
def test_rpc(host, port, user, password):
    # 1.创建NETCONF会话
    with test_connection(host, port=port, user=user, password=password) as m:
        n = m._session.id
        print("This session id is %s." % (n))
        t = etree.fromstring(RPC_STRING)
        resp = m.dispatch(t)
        print("XmlResponse: " + resp.xml)
        time.sleep(2)

if __name__ == '__main__':
    test_rpc("192.172.1.6", 830, "admin", "hello12345")