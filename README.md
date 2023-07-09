# AsyncSqlalchemyTemplate
Template for
[asynchronous](https://docs.python.org/3/library/asyncio.html)
[SqlAlchemy](https://docs.sqlalchemy.org/en/20/)
usage.

## Prerequisites

Running of this project locally requires the following tools to be
present on the host system:

* `docker` (version 20.10.0+)
* `docker-compose` (version 1.27.0+)

## Tests environment

To run tests:
1. Go into `docker/tests` folder.
2. Execute `docker-compose up --abort-on-container-exit`.
