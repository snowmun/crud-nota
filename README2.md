
-mysql  Ver 8.0.29
-vue    ver 2

Installed dependencies in vue(npm install):
    -vue-router: "^3.5.1",
    -vue-swal: "^1.0.0",
    -vue-toasted: "^1.1.28",
    -vuex: "^3.1.2"
    -bootstrap: "^5.2.3",
    -bootstrap-vue: "^2.23.1",

Installed dependencies in fastApi (review requirements.txt in Backend and run pip install -r requirements.txt) in root:
    -email-validator==1.3.1
    -fastapi==0.82.0
    -mysql==0.0.3
    -mysql-connector-python==8.0.29
    -mysqlclient==2.1.1
    -uvicorn==0.18.3

-extracts the Dump folder from the root of the project
-import the database in mySQL workbench
    a.go to server tab
    b.select data import note: database should be named note_test
    C. We select the folder where the delivered files are located
    IMPORTANT! before pressing start import check that on the left it says dump structure and dat
    This will insert both the tables and the data

-When entering the front then test-note and run npm init
-then we will start the application with an npm run serve

-then we enter the back and start with run (uvicorn main:app --reload) in root


