""" 
The assumption is made that the docx file format is a standard that'll not change.

this module deals with the pulling a docx file apart.
It;
    - converts a docx file to a zip file & save it to a temp folder. 
    - gets the compressed file that contains the text from the docx turned zip file.
"""

import os, tempfile, shutil,platform

from pathlib import Path



class Stripper():

    DLOAD_DIR = Path.joinpath(Path.home(), Path('Downloads')) #users downloads directory path
    copied_file_name = "s.docx" # a copy of the file to be stripped will always be named s.docx
    copied_file_rename = "s.zip" # after the file tobe exctracted is converted to zip it will be named s.zip 
    docx_filepath = '' #user provided path to file to be extracted is stored in this variable
    temp_dir = None #path to generated temporaryorking directory will be stored here
    

    def __init__(self, docx_path: str = None):
        if docx_path == None:
            self.docx_filepath = input("input path to the docx file: \n")
        else:
            self.docx_filepath = docx_path
        self._make_temp_dir()

    @classmethod
    def platform_stroke(cls):
        '''returns OS compliant filepath slashes... or strokes. lol'''
        if platform.system() == "Windows":
            return "\\"
        return "/"


    def _make_temp_dir(self):
        ''' Creates a temporary directory in the users downloads directory '''
        self.temp_dir = tempfile.TemporaryDirectory(dir = self.DLOAD_DIR)
        return self


    def _copy_file_to_temp_dir(self):
        '''
        copies file to the temporary folder created by instantiating this class
        also converts it to a zip file while at it
        '''
        shutil.copyfile(self.docx_filepath,self.temp_dir.name + f"{self.platform_stroke()}{self.copied_file_name}")
        os.rename(self.temp_dir.name + f"{self.platform_stroke()}{self.copied_file_name}", self.temp_dir.name + f"{self.platform_stroke()}{self.copied_file_rename}")
        return self


    def _extract_zip(self):
        shutil.unpack_archive(self.temp_dir.name + f"{self.platform_stroke()}{self.copied_file_rename}", self.temp_dir.name, 'zip')
        return self

    
    def strip(self):
        ''' uses some of class Stripper's private methods to copy desired docx file to the temporary directory created at class initialization then
        convert it to a zip file before returning the path to the zip file content that contains the text to be extracted '''
        
        self._copy_file_to_temp_dir()
        self._extract_zip()
        return self.temp_dir.name + f"{self.platform_stroke()}word{self.platform_stroke()}document.xml"