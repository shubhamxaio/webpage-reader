# webpage-reader

Steps to run app:

S1: install the dependencies which is in requirements.txt<br>
S2: Migrate the db<br>
S3: run flask app using **flask run** command. Default port will be 5000<br>
S4: run RQ worker **rq worker webpage_reader-tasks**<br>
S5: enter the url on webpage hit submit and check the console it running in backgroud and it will save in db<br>
<br>
DB used: Sqlite<br>
Developed Platform: Ubuntu 16.04<br>
