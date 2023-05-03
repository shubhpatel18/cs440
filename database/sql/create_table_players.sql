CREATE TABLE IF NOT EXISTS public.players
(
	player_id integer NOT NULL,
	player_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
	position character varying(20) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT players_pkey1 PRIMARY KEY (player_id)
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.players OWNER to tau;

CREATE INDEX player_name_index
ON public.players(player_name);

CREATE INDEX position_index
ON public.players(position);
