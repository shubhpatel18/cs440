CREATE TABLE IF NOT EXISTS public.colleges
(
	college_id serial,
	college_name character varying(50) NOT NULL,
	wins integer NOT NULL DEFAULT 0,
	ties integer NOT NULL DEFAULT 0,
	losses integer NOT NULL DEFAULT 0,
	CONSTRAINT colleges_pkey PRIMARY KEY (college_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.colleges
	OWNER to tau;

CREATE INDEX college_name_index
ON public.colleges(college_name);