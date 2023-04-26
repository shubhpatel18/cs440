CREATE TABLE IF NOT EXISTS public.fantasy_teams
(
	team_name character varying(20) COLLATE pg_catalog."default" NOT NULL DEFAULT '"myteam"'::character varying,
	team_id serial,
	user_id integer NOT NULL,
	qb_id integer,
	rb_id integer,
	wr1_id integer,
	wr2_id integer,
	te_id integer,
	flex_id integer,
	center_id integer,
	lg_id integer,
	rg_id integer,
	punter_id integer,
	de1_id integer,
	de2_id integer,
	dt1_id integer,
	dt2_id integer,
	lb1_id integer,
	lb2_id integer,
	lb3_id integer,
	cb1_id integer,
	cb2_id integer,
	s1_id integer,
	s2_id integer,
	kicker_id integer,
	CONSTRAINT players_pkey PRIMARY KEY (team_id)
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.fantasy_teams
	OWNER to tau;

CREATE INDEX team_name_index
ON public.fantasy_teams(team_name);

CREATE INDEX user_id_index
ON public.fantasy_teams(user_id);