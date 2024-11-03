# Duplicates-Remover
Duplicate Remover is a Class designed to efficiently identify and delete duplicate files within a specified folder and its subfolders.
Each deletion is logged in a separated log file for easy tracking. This tool uses exclusively python built-in libraries.

Features:

- Identifies and Deletes Duplicates: Scans the specified folder and subfolders to find identical files and removes them, freeing up valuable space on your hardware.
- Logging: Each deletion action is recorded in a log file, providing a clear record of processed files.
- Lightweight: Uses only Python's built-in libraries, making it easy to use without external dependencies.

In order to use Duplicates Remover, initialize it from the command line with the specified folder paths. The tool uses argparse to accept input parameters for the source folder (where duplicates will be checked) and the log folder (where deletion logs will be saved)
