FROM python:3.10
# set work directory
WORKDIR /home/d0gied/sirius_bot
# copy project
ENV TOKEN="TOKEN"
COPY . /home/d0gied/sirius_bot

RUN pip install -r ./requirements.txt

# install dependencies
CMD ["python", "main.py"]
