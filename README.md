# Example of broken django project with coverage 6+.

## Prep a virtualenv first

```
python3 -m venv venv
source venv/bin/activate
pip install django coverage
```

## Coverage broken
Running coverage with the provided `.coveragerc` breaks. This config tries to set source to `demo.management`.

```
$ coverage run ./manage.py cover_this
Traceback (most recent call last):
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/bin/coverage", line 10, in <module>
    sys.exit(main())
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/cmdline.py", line 889, in main
    status = CoverageScript().command_line(argv)
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/cmdline.py", line 599, in command_line
    return self.do_run(options, args)
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/cmdline.py", line 761, in do_run
    self.coverage.start()
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/control.py", line 551, in start
    self._init_for_start()
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/control.py", line 513, in _init_for_start
    self._inorout.configure(self.config)
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/inorout.py", line 278, in configure
    modfile, path = file_and_path_for_module(pkg)
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/coverage/inorout.py", line 122, in file_and_path_for_module
    spec = importlib.util.find_spec(modulename)
  File "/usr/lib/python3.7/importlib/util.py", line 94, in find_spec
    parent = __import__(parent_name, fromlist=['__path__'])
  File "/home/asedeno/src/django-coverage6-breakage-demo/demo/__init__.py", line 5, in <module>
    is_debug = getattr(settings, 'DEBUG', False)
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/django/conf/__init__.py", line 82, in __getattr__
    self._setup(name)
  File "/home/asedeno/src/django-coverage6-breakage-demo/venv/lib/python3.7/site-packages/django/conf/__init__.py", line 67, in _setup
    % (desc, ENVIRONMENT_VARIABLE))
django.core.exceptions.ImproperlyConfigured: Requested setting DEBUG, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
```

With two other possible `.coveragerc` files, things work.

The first one sources `demo` instead of `demo.management`

```
$ coverage run --rcfile=.coveragerc-works ./manage.py cover_this
Hello, world!
$ coverage report
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
demo/__init__.py                             2      0   100%
demo/asgi.py                                 4      4     0%
demo/management/__init__.py                  0      0   100%
demo/management/commands/__init__.py         0      0   100%
demo/management/commands/cover_this.py       5      0   100%
demo/settings.py                            19      0   100%
demo/urls.py                                 3      0   100%
demo/wsgi.py                                 4      4     0%
------------------------------------------------------------
TOTAL                                       37      8    78%
```

The second one uses `include` to limit the report to `demo/management`.

```
$ coverage run --rcfile=.coveragerc-works2 ./manage.py cover_this
Hello, world!
$ coverage report
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
demo/management/__init__.py                  0      0   100%
demo/management/commands/__init__.py         0      0   100%
demo/management/commands/cover_this.py       5      0   100%
------------------------------------------------------------
TOTAL                                        5      0   100%

```
