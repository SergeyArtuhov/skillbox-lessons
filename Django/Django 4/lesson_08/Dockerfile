FROM python:3.12
# использование образа python 3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /app
# рабочая директория

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY mysite .

#CMD ["python", "manage.py", "runserver"]
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]