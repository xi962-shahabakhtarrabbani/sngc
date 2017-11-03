
Steps :
1- Once you clone the repo on your systems, cd to the sngc directory and create a python virtual environment using the following command :

virtualenv env

If virtualenv isn't already installed, then install it using 'pip install virtualenv'
For using pip command, you will need to ensure that pip is installed. To install pip, use command 'sudo apt-get install python-pip'


2- Once the virtual environment named 'env' is created, you will see a directory named 'env' is created as well. You will have to activate this environment before proceeding to install the python packages exclusively for this project.

To activate the virtualenv, from your sngc folder, use the command  :
source env/bin/activate

You will see that (env) is reflected before the directory name in your terminal.

To deactivate the virtualenv, use the command  : deactivate

The use of the virtual environment is to create a separate python environment for every project so that the dependencies of projects don't interfere with the system python packages, or with each other's dependencies.

3- Once the virtual environment is activated, install the dependencies for this project that are mentioned in the requirements.txt file using the command : pip install -r requirements.txt

This would install all the dependencies for this project. Now if anyone of us are installing another python package, we will have to write that into our requirements.txt file using : pip freeze > requirements.txt

4- Now you will have to individually install the Fusion Charts library on your systems. It's a trial version though but it will work indefinitely.

Use npm to install the fusioncharts. Use : npm install fusioncharts.
If npm is not installed, then you can probably install it using : sudo apt-get install npm (I am not so sure about this command though)

npm install fusioncharts will create a fusioncharts directory inside your node_modules directory which will be created in your home directory(if not already present)

5- Now the code that I have pushed has code that is directed towards the node_modules folder of my system. You will have to manually change that code to set the target to your system's folder.

6- Now you can finally start your flask app. I would suggest to use an IDE like 'PyCharm Community Edition', it's provided by free from JetBrains.

7- If you are not using an IDE, hit : python main.py and this would start the flask server. 
Go to localhost:3000 and the app would be ready there.
