
import svn.local
import pprint



# r = svn.local.LocalClient('D:\\test')
# r.export('D:\\test')
#
# pprint.pprint(r.info())
import os

import svn.remote

r = svn.remote.RemoteClient('http://172.16.2.135:8088/svn/Devops/books')
r.checkout(os.path.dirname(__file__))
print(r)