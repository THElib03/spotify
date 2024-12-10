from pathlib import Path
import json
import re

class Reader:
    dataLoc = ''
    
    """Starts the Reader class and defines the path of the JSON data to use with the class methods."""
    def __init__(self):
        self.dataLoc = Path.cwd().name + '\\SpotifyAccountData\\'
        if Path(self.dataLoc).exists() and Path(self.dataLoc).is_dir():
            print('good job')
        else:
            print('fatal error, the data folder was not found')
        
    """
    Matches all the files in the working folder related to song listing history.
    
    Returns:
        list: An array of WindowsPath object of the files found.
    """
    def getDataFiles(self) -> list:
        dataFiles = []
        for file in Path(self.dataLoc).iterdir():
            if re.search('.*Streaming_History_Audio_\d{4}(-\d{4})?_\d{1,3}\.json', file.name):
                dataFiles.append(file)
                
        return dataFiles    
            
    """
    Matches all the files in the working folder related to song listing history of a given year.
    
    Parameters:
        year (int): The year to be matched against the present files.
        
    Returns:
        list: An array of WindowsPath objects that contain info from the given year.
    """
    def getDataFilesByYear(self, year: int) -> list:
        if not isinstance(year, int) or year < 1900 or year > 2100:
            return 'Invalid year'
        dataByYear = []
        
        for file in Path(self.dataLoc).iterdir():
            pattern = rf'.*Streaming_History_Audio_({year}(-\d{{4}})?|\d{{4}}-{year})_\d{{1,3}}\.json'
            if re.search(pattern, file.name):
                dataByYear.append(file)
                
        return dataByYear