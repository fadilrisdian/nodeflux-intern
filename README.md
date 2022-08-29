# Streamlit Car Counting
## Nodeflux Internship Task 1

![Screenshot from 2022-08-22 10-43-50](https://user-images.githubusercontent.com/105907083/185834315-90fb53e6-67b4-41aa-bf60-bd5e8206700d.png)

### Run app without docker

```
git clone https://github.com/fadilrisdian/streamlit-car-counting
cd streamlit-car-counting
pip install -r requirements.txt
streamlit run App.py
```

### Build application
```
git clone https://github.com/fadilrisdian/streamlit-car-counting
cd streamlit-car-counting
docker build -t car-count:latest .
docker run -p 8501:8501 car-count:latest
```
