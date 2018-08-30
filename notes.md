## High level notes

### Set up (details in README)

1. Set up virtual environment and install minimum dependencies (Django, selenium, a web driver)
2. Immediately start by writing a functional test. At first, this will just check that the boilerplate app runs,and should be an expected failure. For example:

```
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
```

3. Do whatever else necessary to make the test pass. For example:

* Use Django to to create a project & app
* Start the Django dev server

### MVP

1. Write comments in the functional test to __describe the user story__ of an MVP
2. __Expand the functional test__ for the user story
3. With the functional test failing expectedly, consider how to pass the tests, and __begin writing unit tests__ that describe the passing behavior.
4. __Write the minimal application__ code to pass the expectedly failing unit tests.
5. __Iterate steps 3 & 4__ until the functional test is further along or passing.
6. Rinse & repeat.

## Todos

