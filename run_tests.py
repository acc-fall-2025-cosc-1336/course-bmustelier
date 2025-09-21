import unittest
from tests.homework.b_in_proc_out import tests_in_proc_out

suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
unittest.TextTestRunner(verbosity=2).run(suite)