FROM python:3.10
# set work directory
WORKDIR /home/d0gied/bot
# copy project
ENV TOKEN="TOKEN"
COPY . /home/d0gied/bot

# install dependencies
RUN pip install -r ./requirements.txt

CMD ["python", "main.py"]
