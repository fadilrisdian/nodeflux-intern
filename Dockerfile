# python open-cv
FROM jjanzic/docker-python3-opencv

RUN apt-get update

# env
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN ls -la $APP_HOME/

#opencv dependencies 
RUN apt-get update
#apt-get install -y python3-opencv
#RUN pip install opencv-python

#Install packages
RUN pip install -r requirements.txt

#Make port available
EXPOSE 80

# Define env variable 
ENV NAME streamlit-opencv

# Run app.py 
CMD [ "streamlit", "run", "app.py" ]
