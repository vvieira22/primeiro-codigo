import subprocess
import os
import git

# Abra o repositório
repo = git.Repo("C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\teste")
for remote in repo.remotes:
    remote.fetch()

# Obtenha as três últimas tags ordenadas por data de criação
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime, reverse=True)[:3]

# Imprima as tags
for tag in tags:
    print(tag.name)
