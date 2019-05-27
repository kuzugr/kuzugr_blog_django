## 環境
- python 3.7

## 実行方法
1. python3 -m venv myenv
2. source myenv/bin/activate
3. pip install -e .[dev] -c constraints.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

## flake8 check
1. flake8 --exclude=myenv/

## autopep8
1. autopep8 -ivr . --exclude ./myenv

## pytest with flake8
1. pytest --flake8
