-- Select * from certificates;
-- Select * from person;
-- SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';

BEGIN TRANSACTION;
    UPDATE person SET age = 40 where name = 'Anonymous';

    UPDATE person SET age = 'random' where name = 'testuser';
COMMIT TRANSACTION;
