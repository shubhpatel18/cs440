CREATE TABLE IF NOT EXISTS public.colleges
(
	name character varying(50) COLLATE pg_catalog."default" NOT NULL,
	id integer NOT NULL,
	CONSTRAINT colleges_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.colleges
	OWNER to tau;
