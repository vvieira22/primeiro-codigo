import subprocess
import os
import git

print("100")
print("200")

directory = os.getcwd().replace('\\', '/')
print("300")

# Abra o repositório
repo = git.Repo("C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\teste")
print("400")
repo.git.fetch("-p", "--tags")
print("500")

# Obtenha as três últimas tags ordenadas por data de criação
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime, reverse=True)[:3]
print("600")
