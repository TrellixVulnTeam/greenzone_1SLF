SHELL: /bin/bash

generate:
	$VENV/bin/alembic -c development.ini revision --autogenerate -m "generate"
update:
	$VENV/bin/alembic -c development.ini upgrade head
