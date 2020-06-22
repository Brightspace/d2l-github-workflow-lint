# D2L GitHub Workflow Lint

A linter for GitHub Action workflows, specific to D2L.

## Usage

Add the file `.github/workflows/d2l-workflow-lint.yml` (please use this file name) with these contents:

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

Things of note:

* It will run on every PR that touches a workflow file.
* It will run weekly, so that we can audit workflows across our org that don't recieve frequent changes too.
