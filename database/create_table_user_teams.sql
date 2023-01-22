CREATE TABLE IF NOT EXISTS public.UserTeams
(
	"name" character varying(20) COLLATE pg_catalog."default" NOT NULL DEFAULT '"myteam"'::character varying,
	"id" SERIAL,
	"quarterback_id" integer,
	"runningback_id" integer,
	"wide_receiver_1_id" integer,
	"wide_receiver_2_id" integer,
	"tight_end_id" integer,
	"flex_id" integer,
	"center_id" integer,
	"left_guard_id" integer,
	"right_guard_id" integer,
	"left_tackle_id" integer,
	"right_tackle_id" integer,
	"kicker_id" integer,
	"punter_id" integer,
	"defensive_end_1_id" integer,
	"defensive_end_2_id" integer,
	"defensive_tackle_1_ID" integer,
	"defensive_tackle_2_ID" integer,
	"linebacker_1_id" integer,
	"linebacker_2_id" integer,
	"linebacker_3_id" integer,
	"cornerback_1_id" integer,
	"cornerback_2_id" integer,
	"safety_1_id" integer,
	"safety_2_id" integer,
	CONSTRAINT players_pkey PRIMARY KEY ("id")
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.UserTeams
	OWNER to tau;
