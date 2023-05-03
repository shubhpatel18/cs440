CREATE TABLE IF NOT EXISTS public.player_data
(
	id serial,
	player_id integer NOT NULL,
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
	UNIQUE (player_id, year, week),
	CONSTRAINT player_data_pkey1 PRIMARY KEY (id),
	CONSTRAINT fk_player_id FOREIGN KEY (player_id) REFERENCES players(player_id),
	CONSTRAINT fk_college_id FOREIGN KEY (college_id) REFERENCES colleges(college_id)
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.player_data OWNER to tau;

CREATE INDEX player_id_index
ON public.player_data(player_id);
