CREATE TABLE IF NOT EXISTS public.users
(
	username character varying(20) COLLATE pg_catalog."default" NOT NULL,
	given_name character varying(20) COLLATE pg_catalog."default",
	family_name character varying(20) COLLATE pg_catalog."default",
	password character varying(40) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (username)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
	OWNER to tau;
