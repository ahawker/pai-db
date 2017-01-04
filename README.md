# pai-db

[![PyPI version](https://badge.fury.io/py/pai-db.svg)](https://badge.fury.io/py/pai-db)
[![PyPI versions](https://img.shields.io/pypi/pyversions/pai-db.svg)](https://pypi.python.org/pypi/pai-db)
[![PyPI downloads](https://img.shields.io/pypi/dm/pai-db.svg)](https://pypi.python.org/pypi/pai-db)
[![Build Status](https://travis-ci.org/ahawker/pai-db.svg?branch=master)](https://travis-ci.org/ahawker/pai-db)
[![Coverage Status](https://coveralls.io/repos/github/ahawker/pai-db/badge.svg?branch=master)](https://coveralls.io/github/ahawker/pai-db?branch=master)
[![Code Climate](https://codeclimate.com/github/ahawker/pai-db/badges/gpa.svg)](https://codeclimate.com/github/ahawker/pai-db)
[![Issue Count](https://codeclimate.com/github/ahawker/pai-db/badges/issue_count.svg)](https://codeclimate.com/github/ahawker/pai-db)

Persistent storage of defined resources/relations.

### Status

`pai-db` is in alpha stage and not yet used by any production workloads.

### Installation

Install latest production build using [pip](https://pypi.python.org/pypi/pip):
```bash
    $ pip install pai_db
```

Install latest development build using [pip](https://pypi.python.org/pypi/pip):
```bash
    $ pip install -i https://testpypi.python.org/pypi pai_db
```

Install from source code:
```bash
    $ git clone git@github.com:ahawker/pai-db.git
    $ cd pai_db
    $ python setup.py install
```

### Deployment

Package deployments to index servers are automatically performed by [Travis CI](https://travis-ci.org/).

[PyPI](https://pypi.python.org/pypi/pai-db) - Hosts **Official** Builds

[TestPyPI](https://testpypi.python.org/pypi/pai-db) - Hosts **Development** Builds

Tagged versions of the `master` branch will be deployed to the official PyPI index server while non-tagged versions will be deployed
to the test PyPI index server.

To kick off a new, official deployment, just run one of the following:

**Patch** Version Release: Use this when you make backwards-compatible bug fixes.
```bash
    $ make push-patch
```

**Minor** Version Release: Use this when you add functionality in a backwards-compatible manner.
```bash
    $ make push-minor
```

**Major** Version Release: Use this when you make incompatible API changes.
```bash
    $ make push-major
```

### License

[Apache 2.0](LICENSE)
