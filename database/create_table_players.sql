CREATE TABLE IF NOT EXISTS public.players_2022_w1
(
	player_id integer NOT NULL,
	player_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
	position character varying(20) COLLATE pg_catalog."default" NOT NULL,
	receptions integer NOT NULL DEFAULT 0,
	total_yards integer NOT NULL DEFAULT 0,
	touchdowns integer NOT NULL DEFAULT 0,
	turnovers_lost integer NOT NULL DEFAULT 0,
	sacks integer NOT NULL DEFAULT 0,
	tackles_for_loss integer NOT NULL DEFAULT 0,
	interceptions integer NOT NULL DEFAULT 0,
	fumbles_recovered integer NOT NULL DEFAULT 0,
	punting_yards integer NOT NULL DEFAULT 0,
	fg_percentage integer NOT NULL DEFAULT 0,
	injury_status character varying(12) COLLATE pg_catalog."default" NOT NULL DEFAULT 'Healthy'::character varying,
	college_id integer NOT NULL,
	CONSTRAINT players_pkey1 PRIMARY KEY (player_id)
) TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS public.players_2022_w2  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w3  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w4  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w5  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w6  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w7  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w8  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w9  (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w10 (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w11 (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w12 (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w13 (LIKE public.players_2022_w1) TABLESPACE pg_default;
CREATE TABLE IF NOT EXISTS public.players_2022_w14 (LIKE public.players_2022_w1) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.players_2022_w1  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w2  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w3  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w4  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w5  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w6  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w7  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w8  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w9  OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w10 OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w11 OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w12 OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w13 OWNER to tau;
ALTER TABLE IF EXISTS public.players_2022_w14 OWNER to tau;
