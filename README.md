## A Typical directory structure for running tests using `unittest`

For a typical directory structure like this setup, do the following:

    new_project
    ├── scr
    |   ├── hello_world_folder
    |   │   ├── __init__.py         # make it a package
    |   │   └── hello_world.py
    └── test
        ├── __init__.py         # also make test a package
        └── test_hello_world.py

And in the test modules inside the `test` package, you can import the `hello_world` package and its modules as usual:

    # or an object/function inside the hello_world_folder module
    from scr.hello_world_folder import run_hello_world

    Make sure to include in all directories a init. And change in the init of the test folder the working directory to the scr folder

**Running a single test module:**

To run a single test module, in this case `test_hello_world.py`:

    $ cd new_project
    $ python -m unittest test.test_hello_world

Just reference the test module the same way you import it.

**Running a single test case or test method:**

Also you can run a single `TestCase` or a single test method:

    $ python -m unittest test.test_hello_world.HelloWorldTestCase
    $ python -m unittest test.test_hello_world.HelloWorldTestCase.test_method

**Running all tests:**

You can also use [test discovery][2] which will discover and run all the tests for you, they must be modules or packages named `test*.py` (can be changed with the `-p, --pattern` flag):

    $ cd new_project
    $ python -m unittest discover

This will run all the `test*.py` modules inside the `test` package.


  [1]: https://docs.python.org/2/library/unittest.html#command-line-interface
  [2]: https://docs.python.org/2/library/unittest.html#test-discovery
