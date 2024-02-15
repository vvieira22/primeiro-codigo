import subprocess
import os
import git

print("100")
print("200")

directory = os.getcwd().replace('\\', '/')
print("300")

# Abra o repositório
print(git.Repo(directory))
repo = git.Repo(directory)
print(repo)
print("400")
repo.git.fetch("-p", "--tags")
print("500")

# Obtenha as três últimas tags ordenadas por data de criação
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime, reverse=True)[:3]
print("600")
