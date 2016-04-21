all:

migs:
	python manage.py makemigrations
mig:
	python manage.py migrate
merge:
	python manage.py makemigrations --merge
sync:
	python manage.py syncdb
run:
	python manage.py runserver
user:
	python manage.py createsuperuser
collect:
	python manage.py collectstatic
sh:
	python manage.py shell
dbsh:
	python manage.py dbshell
del:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -not -name "__init__.pyc" -delete
	rm db.sqlite3
pull:
	git pull --no-edit
add:
	git add -v --all
commit:
	git commit -v -a
push:
	git push -v
fpush:
	git push -v -f
rst:
	git reset --hard
srst:
	git reset
st:
	git status -v
clean:
	git clean -f
