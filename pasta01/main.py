import subprocess
import os
import git
import os

directory = os.getcwd().replace('\\', '/')

# Abra o repositório
repo = git.Repo(directory)

# Obtenha as três últimas tags ordenadas por data de criação
tags = repo.tags.sort(key=lambda t: t.commit.committed_datetime, reverse=True)[:3]

# Imprima as tags
for tag in tags:
    print(tag.name)
