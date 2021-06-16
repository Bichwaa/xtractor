from .extractor import extract
from .stripper import Stripper


def recover(path=None, destination=""):
 if path!=None:
  s = Stripper(path)
 else:
  s = Stripper()
 xml = s.strip()
 return extract(xml, destination=destination)
