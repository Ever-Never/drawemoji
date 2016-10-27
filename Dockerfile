FROM python:3.5
RUN apt-get update && apt-get install -yqq libfreetype6-dev
COPY Pillow /code/Pillow
RUN pip install /code/Pillow
CMD python /code/SharingRender.py
