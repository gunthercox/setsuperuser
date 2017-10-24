# setsuperuser

Django command for setting the super user from environment variables.

## Installation

This package can be installed with `pip`.

```
pip install setsuperuser
```

Add `setsuperuser` to `INSTALLED_APPS`.

```
INSTALLED_APPS = [
    # ...
    'setsuperuser',
]
```

Set the following environment variables to create the superuser.

- `SUPERUSER_EMAIL`
- `SUPERUSER_PASSWORD`
