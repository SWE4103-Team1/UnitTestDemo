# Django Unit Test Demo
This repository serves as a demonstration of how we can add unit tests to individual Django components to verify their functional behavior. 

## Setting up unit tests
The most basic configuration is defining your unit tests within the test.py file found in the Django app file structure (DemoApp in this repo). Django uses the python standard library unittest package so that is what we will use as it is what will be easiest. 

When creating a unit test class, ensure that you inherit from django.test.TestCase as this will provide you with all the required unittest features and also make sure Django doesn't cry for help. This is explained in the [Django wiki](https://docs.djangoproject.com/en/3.2/topics/testing/overview/): "If your tests rely on database access such as creating or querying models, be sure to create your test classes as subclasses of django.test.TestCase rather than unittest.TestCase. Using unittest.TestCase avoids the cost of running each test in a transaction and flushing the database, but if your tests interact with the database their behavior will vary based on the order that the test runner executes them. This can lead to unit tests that pass when run in isolation but fail when run in a suite."

## Running your unit tests
At the root directory of your Django application execute:
```bash
$ python manage.py test
```
This will find all test cases (subclasses of unittest.TestCase) in any file whos name begins with test, automatically build a test suite out of those test cases, and run that suite.

You can specify particular tests to run by supplying ```python manage.py test``` with specific modules, packages, test cases, or methods.

If a test requires a database, a blank test database is created for the test. This is elaborated on in furthur detail [in the wiki](https://docs.djangoproject.com/en/3.2/topics/testing/overview/#the-test-database).

## More information
[Django Testing Documentation](https://docs.djangoproject.com/en/3.2/topics/testing/overview/#module-django.test)
