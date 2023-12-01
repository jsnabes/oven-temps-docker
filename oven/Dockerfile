FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# add main.py file
COPY ./main.py /code/

# run main.py using python
CMD ["python", "main.py"]



