# Installation
```console
# pip install 'git+https://github.com/kevinmgranger/pelorus-extra#subdirectory=pelorus-pr'
```
# Goals

- [x] access e2e logs for a given PR number and test name
- [x] click
- [x] proper setuptools integration
- [x] test installing from pip with git url
- [ ] RELEASE
- [x] list failing tests for given PR number
- [ ] get logs for unit tests too
- [ ] list failing tests, checking if a PR is currently checked out
- [ ] list failing tests, checking if the current branch has an associated PR

# Misc, to triage

- [ ] if stdout is not terminal, write logs. if is terminal, open in editor!