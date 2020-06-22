import argparse
import os
import ruamel.yaml
import sys

class Linter:
  def __init__(self, workflowPath):
    self.workflowPath = workflowPath
    self.success = True
   
  def error(self, yamlNode, msg):
    print('::error file=%s,line=%s,col=%s::%s' % (self.workflowPath, yamlNode.lc.line, yamlNode.lc.col, msg))
    self.success = False

  def warning(self, yamlNode, msg):
    print('::warning file=%s,line=%s,col=%s::%s' % (self.workflowPath, yamlNode.lc.line, yamlNode.lc.col, msg))

  def checkForTimeout(self, jobId, job):
    if 'timeout-minutes' in job:
      return

    self.error(job, 'Please explicitly set timeout-minutes (to a low value) to prevent run-away jobs')

  def lint(self, addMarkers=False):
    if addMarkers:
      print('::group name=' + self.workflowPath + '::Linting ' + self.workflowPath)

    yaml = ruamel.yaml.YAML()
    with open(self.workflowPath) as f:
      workflow = yaml.load(f.read())

    # Per-job lints
    for jobId in workflow['jobs']:
      self.checkForTimeout(jobId, workflow['jobs'][jobId])

    if addMarkers:
      print('::endgroup::')
      
    return self.success


if __name__ == '__main__':
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
    workflows = os.listdir(args.dir)
    workflows = filter(lambda path: path.endswith('.yml'), workflows)
    workflows = map(lambda path: args.dir + '/' + path, workflows)
  else:
    workflows = [args.file]
  
  for workflow in workflows:
    linter = Linter(workflow)
      
    if not linter.lint(addMarkers=True):
      success = False
  
  if not success:
    sys.exit(1)

