CREATE TABLE IF NOT EXISTS public.players
(
	id serial,
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
	year integer NOT NULL,
	week integer NOT NULL,
	CONSTRAINT players_pkey1 PRIMARY KEY (id)
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.players OWNER to tau;
