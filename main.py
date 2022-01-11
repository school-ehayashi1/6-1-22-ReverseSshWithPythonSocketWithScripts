import os
#https://stackoverflow.com/questions/3751900/create-file-path-from-variables
import subprocess
process = subprocess.Popen(['powershell','-c', 'Get -PSDrive -PSProvider "Filesystem"'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout)

