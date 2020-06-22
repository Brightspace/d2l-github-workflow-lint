import io
import sys
import unittest

from lint import lint

class Tests(unittest.TestCase):
  def setUp(self):
    self.stdout_backup = sys.stdout
    self.out = io.StringIO()
    sys.stdout = self.out

  def tearDown(self):
    sys.stdout = self.stdout_backup

  def stdout(self):
    return self.out.getvalue().strip()

  def test_missing_timeout(self):
    linter = new Linter('test-data/missing-job-timeout.yml')
    success = linter.lint()
    self.assertFalse(success)
    self.assertEqual(self.stdout(), '::error file=test-data/missing-job-timeout.yml,line=7,col=4::Please explicitly set timeout-minutes (to a low value) to prevent run-away jobs')

if __name__ == '__main__':
  unittest.main()
