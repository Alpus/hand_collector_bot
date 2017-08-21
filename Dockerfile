FROM python:3.5
MAINTAINER Alexander Pushin "work@apushin.com"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app app

RUN groupadd handjob_bot \
  && useradd -g handjob_bot handjob_bot \
  && mkdir images \
  && chown -R handjob_bot:handjob_bot images

USER handjob_bot
ENTRYPOINT python3 app/run_bot.py

