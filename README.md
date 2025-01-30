**Example Commands to Run and Test**
- example of running a specific command
`poetry run python lingua/cli.py utc -5`
- how to run tests
`poetry run pytest`

**Update Dependencies**
- update dependencies, dry-run or normal
`poetry update --dry-run`
`poetry update`

**Git Versioning Commands**
- python script to help with the versioning process
`python git_versioning.py {major|minor|patch} [--dry-run]`
`python git_versioning.py minor --dry-run`
`python git_versioning.py minor`

**manual git commands**
- get latest versioning tag that was used
`git describe --tags --match "v*.*.*" --abbrev=0`

- tag the latest commit
`git tag v1.5.0`
`git tag v1.5.2 -m "New release"`

- push to remote with tags
`git push --follow-tags`

**Example commands to build and install**
- build the project
`poetry build`

- install the package
`pip3 install *.whl`

**Aliases for .zshrc**
alias es-num="lingua number"
alias es-date="lingua date"
alias es-len="lingua length"
alias es-dist="lingua distance"
alias es-temp="lingua temp"
alias es-weight="lingua weight"
alias imm="lingua imm"
alias mmi="lingua mmi"
alias tz="lingua tz et"
alias tze="lingua tz et"
alias tzc="lingua tz ct"
alias utc="lingua utc"
alias dst="lingua dst"
