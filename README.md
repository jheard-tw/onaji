# Onaji　(同じ) 

- Author: Jefferson Heard
- Email: jheard@teamworks.com
- Version: 0.0.1

Onaji is a PyTest plugin for performing regression tests between two commits or two
branches in Git. 

To use Onaji, include it in your `conftest.py` and import the logger object in 
your tests. In each unit test, you call `onaji.log(key, value)` to log an object
to the Onaji backend store. This object will be stored with the commit, branch,
test name, and key. Currently, objects are converted using `repr` but in the
future more formats will be supported.

### Install

```
$ python setup.py install
```

### Usage

##### In your root `conftest.py` make sure to include the plugin:

```python
import pytest

pytest_plugins = ['onaji']
```

##### In each of your pytest files

Include the library

```python
from onaji.logger import onaji
```

Log info in tests

```python
def test_person_name_format_with_nickname():
    assert person.get_nickname_formatted() == ' "Nick"'
    assert person.get_full_name() == "Last, First \"Nick\""
    assert person.format_name("f m l") == "First Middle Last"
    assert person.format_name("p m l") == "Preferred Middle Last"
    assert person.format_name("f n m l") == "First Nick Middle Last"

    onaji.log('person.format_name(f m l)', person.format_name("f m l"))
    onaji.log('person.format_name(p m l)', person.format_name("p m l"))
    onaji.log('person.format_name(p m l)', person.format_name("p m l"))
    onaji.log('person.format_name(f n m l)', person.format_name("f n m l"))
```

Every time you want to run tests against a commit, check out that commit and run 
`pytest`. If your git repo is not at the root of where you run pytest, set the 
`REPO_HOME` environment variable To run the regression diff, use:

```
$ onajidiff <commit_id_a> <commit_id_b>
```

Or to compare two branches:

```
$ onajidiff --branches <branch_name_a> <branch_name_b>
```

Example:

```bash
$ onajidiff 9ea881441704a068d650fcd9dd052a606838ad8a 9ea881441704a068d650fcd9dd052a606838ad8b

Reading files.
Reading left file
Reading right file
Done. Comparing.

================================================================================
2 differences. in test_person_name_format_with_nickname :: person.format_name(f n m l)
--------------------------------------------------------------------------------

--- *.9ea881441704a068d650fcd9dd052a606838ad8a

+++ *.9ea881441704a068d650fcd9dd052a606838ad8b

@@ -1 +1 @@

-'First Nick Middle Last'
+'First Nick Middle LastName'
```

