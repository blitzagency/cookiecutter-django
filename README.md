## PyTest

#### Run Everything
```
DJANGO_SETTINGS_MODULE=app.config.settings.local pytest
```

#### Run Something Specific
```
pytest test_mod.py::test_func   # only run tests that match the "node ID",
                                # e.g. "test_mod.py::test_func" will select
                                # only test_func in test_mod.py

pytest test_mod.py::TestClass::test_method   # run a single method in
                                             # a single class
```
