# docker-compose for DMOJ

This is a docker-compose setup for running a DMOJ instance.
The backend judge is based on `dmoj/runtimes-tier1`.

## Usage

1. Copy all 3 example setting files as follows:

  ```
  cp .env_example .env
  cp site.env_example site.env
  cp db-entrypoint.sql_example db-entrypoint.sql
  ```

2. Fill in the necessary fields in each file.
  `JUDGE_KEY` in `.env` and `DB_PASSWORD` in `site.env` must be filled in.
   Additionally, in `db-entrypoint.sql`, fill in the `DB_PASSWORD` that you set in `site.env`.
   All other settings could be left as is, and it should work.

2. Run docker compose. Wait a moment until the **site** container invokes the **db** and the initial migration is complete.
  ```
  docker compose up
  ```

3. The site should now be available at `http://localhost:8000/`.
  Right now the **bridge** and **judge** container will log out errors, but the **site** and **db** should be working.
  Access `http://localhost:8000/admin/judge`, and create a judge with the name and key you set in `.env`.

4. Now both the site and judge servers are running. 
  Write problem statements and configure settings via the admin interface.
  Add testcases/custom checkers under the `problems/` directory.

5. To stop the containers, run
  ```
  docker compose down
  ```