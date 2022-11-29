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
- [ ] list failing tests, checking if a PR is currently checked out

- [x] list failing tests, checking if the current branch has an associated PR
    - [ ] how can we check how many args are passed? does it need to be that custom class? seems like too much work tbh
- [ ] get logs for unit tests too

# Misc, to triage

- [ ] if stdout is not terminal, write logs. if is terminal, open in editor!
- [ ] sometimes the PR doesn't get resolved? 729 namely.