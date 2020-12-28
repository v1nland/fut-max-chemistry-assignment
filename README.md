# fut max chemistry assignment

This project helps you maximize your team chemistry. Uses Python 2.7.16.

## Local install

Before you run the program, you need a postgresql database containing the fut players. Inside the 'sql' folder, there's a fut database updated on december 25, 2020. You can download postgres from [it's website](https://www.postgresql.org/download) and manually run the 'sql/players_202012252237.sql' script. The default credentials for this program to work are:

    > db_user: postgres
    > db_pass: 123
    > db_name: fut
    > port: 5432

Once you have postgres installed, running and you executed the 'sql/players_202012252237.sql' script, you'll see the 'fut' database and the 'players' table.

Now, you need build this module, run:

    > python setup.py build

Then you can either put the file build/lib-<YOUR-PLATFOrm>/LAPJV.so in the same directory as the code that will be using it, or you can install it so that all of your python programs can see it:

    > python setup.py install

To run the program, you need to install all dependencies:

    > pip install -r requirements.txt --user

Once it's done, run:

    > python fut/cli.py

## Docker install

If you want to use this repository without installing any dependency, there's a Dockerfile that you can freely edit. By default, this Dockerfile will execute "cli.py" script.

As mentioned in the local install section, before you run the program, you need a postgresql database containing the fut players. Inside the 'sql' folder, there's a fut database updated on december 25, 2020. 

    > docker run --name postgres-fut -e POSTGRES_PASSWORD=123 -d -p 5432:5432 postgres:alpine
    > docker cp sql/players_202012252237.sql postgres-fut:/home/
    > docker exec -u postgres postgres-fut psql postgres postgres -f /home/players_202012252237.sql

Please note this program uses those credentials by default, if you want to change it, please edit 'fut/db.py' script.

Next step is configurate our postgres IP. To get postgres container's IP, run:

    > docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-fut

Then, you'll have to put that IP on the 'fut/db.py' script, line 14, 'host' parameter. The result has to be something like:

    > db = DB(dbname='fut', host='172.17.0.2', port=5432, user='postgres', passwd='123')

Finally, run the following command to execute the program.

    > docker build -t fut-max-chemistry-assignment . && docker run -it fut-max-chemistry-assignment

You will be asked for the necessary variables for the program to run.
