# AsyncSqlalchemyTemplate
Template for
[asynchronous](https://docs.python.org/3/library/asyncio.html)
[SqlAlchemy](https://docs.sqlalchemy.org/en/20/)
usage.

## Prerequisites

Running of this project locally requires the following tools to be
present on the host system:

* `docker` (version 23.05.0+)
* `docker compose` (version 2.21.0+)

## Tests environment

To run tests:
1. Go into `docker/tests/` folder
2. Execute

  ```bash
  docker compose up --abort-on-container-exit
  ```
