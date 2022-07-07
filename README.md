# :stethoscope: Master Medicos
A simple web app to show data manipulation via Flask and SSMS.

# 🚀 Getting Started
Copy the script from [this file] and execute it in SQL Server.

Once you've created the tables in SSMS, go to [main.py] and edit the credentials. (you only have to change server and database in line 7 and 8)

Type `py main.py` in the project's directory or directly run [main.py]

If all goes well, your webapp will be deployed on localhost:5000 (127.0.0.1:5000)

Type /admin in url (127.0..1:5000/admin) to perform CRUD operations in your database.

# :gear: Requirements
Install via pip

- Pyodbc
- Flask
- Requests

or run ```pip freeze > requirements.txt``` 
then ```pip install -r requirements.txt```

[this file]:https://github.com/cocomo29/MasterMedicos/blob/main/confirmation.sql
[main.py]:https://github.com/cocomo29/MasterMedicos/blob/main/main.py
- if you'd like to see the data manipulation using c# and asp.net core mvc check out [this repo](https://github.com/blurryface92/blurrybooks) by [blurryface](https://github.com/blurryface92)

[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)
