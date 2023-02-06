# Crypto_api


# Install the below libraries

python -m venv .venv
.\.venv\Scripts\Activate.ps1 

pip install -r requirements.txt

# To build docker image
docker build -t saisri/api-project:0.0.1.RELEASE .

# To run docker image (creating docker container)
docker run -p 5000:5000 {docker_image_ID}


# A Micro service app to fetch crypto currency market updates

Fetching crypto currency market from below site.

 
```
## Implentation of API

This is a simple API for managing market data built using Flask. The API has the following endpoints:

- `/api/v3/markets/summaries`: Retrieves a list of all market data
- `api/v3/markets/<string:id>/summary`: Retrieves a specific market by symbol

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requriement.txt .

```bash
pip install request
aniso8601==8.1.0
flask-marshmallow==0.14.0
Flask-RESTful==0.3.8
marshmallow==3.10.0
marshmallow-sqlalchemy==0.24.1
PyMySQL==0.10.1
pytz==2020.4
six==1.15.0
SQLAlchemy==1.3.22
passlib==1.7.1
Flask-HTTPAuth==3.2.3
flask-bcrypt
flask-jwt-extended
flask-swagger-ui
requests
```
## Swagger documentation
#installation
```bash
from flask_swagger_ui import get_swaggerui_blueprint
```
swagger documentation code is mentioned in swagger.json

![image](https://user-images.githubusercontent.com/122692986/216951722-10a979bf-4ec0-4876-b549-2ba686114dad.png)



## Testing
file name test_main.py

```python
import pytest
