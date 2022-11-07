# We suppose that your default python interpreter can be reached by python3
python3 delete_migrations.py
python3 manage.py reset_db --no-input
python3 manage.py makemigrations
python3 manage.py migrate
