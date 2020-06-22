# D2L GitHub Workflow Lint


## Usage

Add the file `.github/workflows/d2l-workflow-lint.yml` with these contents:

```yaml
name: Workflow Lint
on:
  pull_request:
    paths:
      - '.github/workflows/*.yml'
  schedule:
    # Noon (EST) once every Monday
    - cron: '0 4 * * 1'

jobs:
  lint:
  runs-on: [self-hosted, Linux]
  steps:
    - name: Checkout
      uses: Brightspace/third-party-actions@actions/checkout
    - name: Lint
      uses: Brightspace/d2l-github-workflow-lint@master
```
