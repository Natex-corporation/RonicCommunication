FROM python:3
ADD beeing online all the time.py /
RUN pip install time
RUN pip install webbrowser
CMD [ "python", "./beeing online all the time.py" ]