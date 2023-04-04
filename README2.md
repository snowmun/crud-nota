
-mysql  Ver 8.0.29
-vue    ver 2

Installed dependencies in vue:
    -vue-router: "^3.5.1",
    -vue-swal: "^1.0.0",
    -vue-toasted: "^1.1.28",
    -vuex: "^3.1.2"
    -bootstrap: "^5.2.3",
    -bootstrap-vue: "^2.23.1",

Installed dependencies in fastApi (review requirements.txt in Backend):
    -email-validator==1.3.1
    -fastapi==0.82.0
    -mysql==0.0.3
    -mysql-connector-python==8.0.29
    -mysqlclient==2.1.1
    -uvicorn==0.18.3

-extract the Dump folder from the root of the project
-export the database in mySQL workbench
    a.go to the server tab
    b.select data import
    c. We select the folder where the delivered files are
    d.in the same dump folder there is a folder called select please run the db query

-When entering the front then test-note and run npm init
-then we will start the application with an npm run serve

-then we enter the back and start with uvicorn main: app --reload
