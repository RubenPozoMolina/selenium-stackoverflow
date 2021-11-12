## Getting Started

### Prerequisites

install last python 3.x release: 
```
https://www.python.org/downloads/release/
```

Install chromedriver

```bash
export CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` 
sudo mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION
curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
sudo unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION
rm /tmp/chromedriver_linux64.zip
sudo chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver
sudo ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver
```


## Instructions to prepare virtual environment:

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```cmd
py -3 -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

## Executing script:

```bash
export STACKOVERFLOW_EMAIL=your_email@your_domain.com
export STACKOVERFLOW_PASSWORD=your_password
export SELENIUM_HEADLESS=False
python login.py
```

## Docker

Build image:
```bash
docker build -t selenium-stackoverflow .
```

Execute image:
```bash
docker run -e STACKOVERFLOW_EMAIL=your_email@your_domain.com \
  -e STACKOVERFLOW_PASSWORD=your_password \
  selenium-stackoverflow
```


