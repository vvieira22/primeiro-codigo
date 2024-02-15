import subprocess
import os
import git

# Defina o diretório de trabalho
repo_dir = "C:\\ProgramData\\Jenkins\\.jenkins\workspace\\teste\\pasta01"

# Abra o repositório
repo = git.Repo(repo_dir)

# Obtenha as três últimas tags ordenadas por data de criação
tags = repo.tags.sort(key=lambda t: t.commit.committed_datetime, reverse=True)[:3]

# Imprima as tags
for tag in tags:
    print(tag.name)
