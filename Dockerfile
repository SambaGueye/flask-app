FROM python:3
WORKDIR /app
COPY app.py /app
# ADD dataset.csv /app
COPY requirements.txt /app
	
RUN pip install -r requirements.txt

CMD ["python", "./app.py",  "--host=0.0.0.0"]