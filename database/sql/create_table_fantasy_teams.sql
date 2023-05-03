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
	CONSTRAINT players_pkey PRIMARY KEY (team_id),
	CONSTRAINT fk_qb_id FOREIGN KEY (qb_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_rb_id FOREIGN KEY (rb_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_wr1_id FOREIGN KEY (wr1_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_wr2_id FOREIGN KEY (wr2_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_te_id FOREIGN KEY (te_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_flex_id FOREIGN KEY (flex_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_center_id FOREIGN KEY (center_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_lg_id FOREIGN KEY (lg_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_rg_id FOREIGN KEY (rg_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_punter_id FOREIGN KEY (punter_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_de1_id FOREIGN KEY (de1_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_de2_id FOREIGN KEY (de2_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_dt1_id FOREIGN KEY (dt1_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_dt2_id FOREIGN KEY (dt2_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_lb1_id FOREIGN KEY (lb1_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_lb2_id FOREIGN KEY (lb2_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_lb3_id FOREIGN KEY (lb3_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_cb1_id FOREIGN KEY (cb1_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_cb2_id FOREIGN KEY (cb2_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_s1_id FOREIGN KEY (s1_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_s2_id FOREIGN KEY (s2_id) REFERENCES players(player_id, year, week),
	CONSTRAINT fk_kicker_id FOREIGN KEY (kicker_id) REFERENCES players(player_id, year, week)
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.fantasy_teams
	OWNER to tau;

CREATE INDEX team_name_index
ON public.fantasy_teams(team_name);

CREATE INDEX user_id_index
ON public.fantasy_teams(user_id);