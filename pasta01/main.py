import subprocess
import os

cwd = os.getcwd()
# Defina o comando como uma string
command = "git tag --sort=-creatordate | head -n 3"

# Execute o comando 
process = subprocess.Popen(command, cwd = cwd, stdout=subprocess.PIPE, shell=True, text=True)

# Obtenha a saída do comando
output, error = process.communicate()

# Imprima a saída
print(cwd)
