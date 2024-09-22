# docker-compose for DMOJ

This is a docker-compose setup for running a DMOJ instance.
The backend judge is based on `dmoj/runtimes-tier1`.

## Usage

1. Copy `.env_example` and `site.env_example`. Edit its contents. 
  (`JUDGE_KEY` in `.env` and `DB_PASSWORD` in `site.env` must be changed, the others may be left as is and it should work.)

  ```
  cp .env_example .env
  cp site.env_example site.env
  ```

2. Run docker compose. 
  ```
  docker compose up
  ```

3. The site should be available at `http://localhost:8000/`.
  Right now the *bridge* and *judge* container will log out errors, but the *site* and *db* should be working.
  Access `http://localhost:8000/admin/judge`, and create a judge with the name and key you set in `.env`.

4. To stop the containers, run
  ```
  docker compose down
  ```