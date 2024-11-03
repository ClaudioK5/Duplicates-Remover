from pathlib import Path
from datetime import datetime
import shutil
import hashlib
import argparse
import time


class DuplicateRemover:
    
    """
    A class designed to identify and remove duplicate files within a specified source folder. This class 
    uses MD5 hashing to compare files and determine duplicates, logging each deletion in order to ensure clarity.
    """

    
    def __init__ (self, source_folder, log_folder):

        self.source_folder = source_folder
        self.log_folder = log_folder
        self.log_file = Path(self.log_folder) / "duplicateremover_log.txt"
        
        
        Path(self.log_folder).mkdir(parents=True, exist_ok=True)
        
    
    def log_action(self, message):

        """
        records each duplicate deletion action in order to maintain
        a clear record of processed files.
        """
        
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(self.log_file, 'a') as f: f.write(f"{current_time}: {message}\n")
 
    
    
    def remove_duplicates(self, source_folder = None):

        """
        primary method of the class, responsible for performing all the operations required to identify and delete the duplicates.
        This method uses a nested 'recursion' function to traverse through directories and subdirectories, ensuring that all 
        files are checked.
        """

        source_folder = Path(source_folder or self.source_folder)


        def recursion(sub_folder):

            """
            A nested function within the primary method that recursively processes
            folders and subfolders, taking a subfolder as its only parameter.
            """

            for sub_item in sub_folder.iterdir():

                try:
                    
                    if sub_item.is_file() and self.md5(item) == self.md5(sub_item):
                        
                        sub_item.unlink()
                    
                        self.log_action(f"Duplicate '{item.name}' has been deleted from {self.source_folder}")
                    
                    elif sub_item.is_dir():

                        recursion(sub_item)

                except Exception as e:
                     
                     self.log_action(f"An error occured: {e}")   
                


        """
        the for loop iterates over each item in the folder to identify any identical copies. 
        It uses MD5 hashing in order to  check if the two files are identical.
        """
        
        for item in source_folder.iterdir():

            try:
                
                if item.is_file():
                
                    for comparison_item in source_folder.iterdir():
                    
                        if comparison_item.is_file() and item.exists() and comparison_item.exists():
                        
                        
                            if item.name == comparison_item.name:
                            
                                pass
                        
                            elif self.md5(item) == self.md5(comparison_item):
                            
                            
                                comparison_item.unlink()
                        
                                self.log_action(f"Duplicate '{comparison_item.name}' has been deleted from {self.source_folder}")
             
                        elif comparison_item.is_dir():
                        
                            recursion(comparison_item)

                            

                elif item.is_dir():
                
                    self.remove_duplicates(item)


            except Exception as e:
                
                
                self.log_action(f"An error occured: {e}")   
                

            

              
    def md5(self, fname):

        """
        calculates the md5 hash associated to a file.
        """
        
        hash_md5 = hashlib.md5()
        
        with open(fname, "rb") as f:
            
            for chunk in iter(lambda: f.read(4096), b""):
                
                hash_md5.update(chunk)
                
            return hash_md5.hexdigest()


def parse_arguments():

    parser = argparse.ArgumentParser(description = "Duplicate Remover Tool")

    parser.add_argument("source_folder", type = str, help = "Path to the source folder")

    parser.add_argument("log_folder", type = str, help = "Path to the log folder")

    return parser.parse_args()

if __name__ == "__main__":
    
    args = parse_arguments()

    duplicateremover = DuplicateRemover(args.source_folder, args.log_folder)

    duplicateremover.remove_duplicates()
