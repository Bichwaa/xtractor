from .extractor import extract
from .stripper import Stripper


def recover(path=None):
 if path!=None:
  s = Stripper(path)
 else:
  s = Stripper()
 xml = s.strip()
 extract(xml)
