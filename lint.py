import argparse
import os
import ruamel.yaml

def error(f, yamlNode, msg):
  print('::error file=%s,line=%s,col=%s::%s' % (f, yamlNode.lc.line, yamlNode.lc.col, msg))

def warning(f, yamlNode, msg):
  print('::warning file=%s,line=%s,col=%s::%s' % (f, yamlNode.lc.line, yamlNode.lc.col, msg))

def checkForTimeout(f, jobId, job):
  if 'timeout-minutes' in job:
    return

  error(f, job, 'Please explicitly set timeout-minutes (to a low value) to prevent run-away jobs')

def lint(workflowPath):
  print('::group name=' + workflowPath + '::Linting ' + workflowPath)
  yaml = ruamel.yaml.YAML()
  with open(workflowPath) as f:
    workflow = yaml.load(f.read())

  # Per-job lints
  for jobId in workflow['jobs']:
    checkForTimeout(workflowPath, jobId, workflow['jobs'][jobId])

  print('::endgroup::')

#####

parser = argparse .ArgumentParser(description='Lint GitHub Action workflows, for D2L.',
                                  epilog='--file and --dir are mutually exclusive. If neither are provided the behaviour is equivalent to --dir .github/workflows')

parser.add_argument('file', nargs='?', help="The path to a workflow yml file")
parser.add_argument('dir', nargs='?', help="The path to a directory containing workflow yml files")
args = parser.parse_args()

if args.file != None and args.dir != None:
  args.print_help()

if args.file == None and args.dir == None:
  args.dir = '.github/workflows'

if args.dir != None:
  workflows = filter(lambda path: path.endswith('.yml'), os.listdir(args.dir))
  for workflow in workflows:
      lint(args.dir + '/' + workflow)
else:
  lint(args.file)

