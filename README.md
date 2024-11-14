# docker-compose for DMOJ

This is a docker-compose setup for running a DMOJ instance.
The backend judge is based on `dmoj/runtimes-tier1`.

## Usage

1. Copy example `.env` file

  ```
  cp .env.example .env
  ```

2. Fill in the necessary fields in each file.
  `JUDGE_KEY` and `DB_PASSWORD` in `.env` must be filled in.
   All other settings could be left as is, and it should work.

2. Run docker compose. Wait a moment until the initial migration is complete.
  ```
  docker compose up
  ```

3. The site should now be available at `http://localhost:8000/`.

4. To add problems, write problem statements and configure settings via the admin interface.
   Then add testcases/custom checkers under the `problems/` directory.
   Under the directory, `judge.yml` should be created.

   The example is in `problems/judge-example.yml` (Fill in `JUDGE_KEY` with the same string as in `.env`).

5. To stop the containers, run
  ```
  docker compose stop
  ```