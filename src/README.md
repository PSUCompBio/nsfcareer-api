Prerequisite :
1. Python (version 3)
2. Requests Module
	Download it using :
    	pip install requests
	    pip install "requests[security]"
        pip install yattag

Install the package using :
pip install src/dist/simulation-0.1-py3-none-any.whl


Api usage :
simulation filename --filename "Path/to/sensor/file" --user "Your Git-Radar Account Username" --password "Your Git-Radar Account Password"
where filename is the sensor data file that you want to run simulations against.

** If above command doesn't work uninstall the package :
-> pip uninstall simulation
-> pip install src/dist/simulation-0.1.tar.gz

The response will be stored inside timestamp folder

TO Build the Package (Only for development Purpose):
1. Go into /src directory
2. Run this command :
   ```python -m pip install --user --upgrade setuptools wheel```
   ```python setup.py sdist bdist_wheel```
