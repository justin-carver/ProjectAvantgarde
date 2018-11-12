import random
import file

content = None

class CustomFile:
  @staticmethod
  def readFileToObj(fname):
    with open(fname) as f:
      global content
      content = f.readlines()
    content = [x.strip() for x in content]
    return content