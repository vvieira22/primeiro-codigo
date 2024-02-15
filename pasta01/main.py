import subprocess
import os
import git

print("100")
print("200")

directory = os.getcwd().replace('\\', '/')

# Abra o repositório
repo = git.Repo(directory)
repo.git.fetch("-p", "--tags")

# Obtenha as três últimas tags ordenadas por data de criação
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime, reverse=True)[:3]

print("100")
