CREATE TABLE IF NOT EXISTS public.users
(
	user_id serial,
	username character varying(30) UNIQUE COLLATE pg_catalog."default" NOT NULL,
	name character varying(30) COLLATE pg_catalog."default",
	password character varying(40) COLLATE pg_catalog."default" NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
	OWNER to tau;

CREATE INDEX username_index
ON public.users(username);