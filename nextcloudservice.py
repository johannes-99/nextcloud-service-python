import os
from webdav3.client import Client
from flask_restful import Resource

class FileModel(Resource):

  def __init__(self, name, directory):
    self._name = name
    self._dir = directory
    self._isdir = self.isdir 
  
  @property
  def isdir(self):
    return self._name.endswith("/")

  @property
  def name(self):
    return self._name 

  @name.setter
  def name(self,name):
    self._name = name

  @property
  def directory(self):
    return "fooo"

  @name.setter
  def directory(self,directory):
    self._directory = directory



options = {

}
client = Client(options)
client.verify = False 


def read_webdav_dir(directory):
  files = []

#"Fotos Save/"
  webdavfiles = client.list("")

  for webdavfile in webdavfiles:
   file = FileModel(webdavfile,directory)
   print(directory)
   files.append( file )

  return files





