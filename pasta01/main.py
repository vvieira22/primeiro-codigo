import subprocess
import os
import git

directory = os.getcwd().replace('\\', '/')

# Abra o repositório
repo = git.Repo(directory)

# Obtenha as três últimas tags ordenadas por data de criação
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime, reverse=True)[:3]

# Imprima as tags
for tag in tags:
    print(tag.name)
