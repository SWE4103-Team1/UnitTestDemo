from django.test import TestCase

# Unit test class inherits from django.test.TestCase
# which inherits from unittest.TestCase
class DemoAppUnitTests(TestCase):
	def test_true_is_true(self):
		isTrue = True
		self.assertTrue(isTrue)

	def test_false_is_false(self):
		isFalse = False
		self.assertFalse(isFalse)
