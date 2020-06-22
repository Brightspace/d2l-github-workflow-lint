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
    lint('test-data/missing-job-timeout.yml')
    self.assertEqual(self.stdout(), '::error something')

if __name__ == '__main__':
  unittest.main()
