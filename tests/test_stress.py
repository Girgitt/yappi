import os
import signal
import subprocess
import sys

if sys.version_info < (2, 7): # use unittest2 for < Py2.7
    import unittest2 as _unittest
else:
    import unittest as _unittest

import utils

try:
    import pthreading
except ImportError:
    pthreading = None


class DeadlockTest(utils.YappiUnitTestCase):
    """Test deadklock when starting a thread and yappi at the same time."""

    @_unittest.skipUnless(pthreading, "requires pthreading")
    def test_start_deadlock(self):
        script = os.path.join(os.path.dirname(__file__), 'start_deadlock.py')
        for i in range(1000):
            p = subprocess.Popen(['python', script])
            p.wait()
            if p.returncode == -signal.SIGALRM:
                self.fail("Deadlock detected")
            elif p.returncode != 0:
                raise Exception("Unexpected returncode: %d" % p.returncode)


if __name__ == '__main__':
    _unittest.main()
