# fut max chemistry assignment

This project helps you maximize your team chemistry.

First of all, you need build this module, run:

    > python setup.py build

Then you can either put the file build/lib-<YOUR-PLATFOrm>/LAPJV.so in the same directory as the code that will be using it, or you can install it so that all of your python programs can see it:

    > python setup.py install

To run the program, you need to install all dependencies:

    > pip install -r requirements.txt --user

Before you run the program, you need a postgresql database containing the fut players. Inside the 'sql' folder, there's a fut database updated on december 25, 2020. Once it's done, run:

    > python fut/cli.py

You will be asked for the necessary variables for the program to run.
