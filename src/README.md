Prerequisite :
1. Python (version 3)
2. Requests Module
	Download it using :
    	pip install requests
	pip install "requests[security]"

Install the package using :
pip install src/dist/simulation-0.1-py3-none-any.whl

Api usage :
simulation filename
where filename is the sensor data file that you want to run simulations against.

Response :
{
	message : "success",
	images : [
	]
}

TO Build the Package :
1. Go into /src directory
2. Run this command :
   ```python -m pip install --user --upgrade setuptools wheel```
   ```python setup.py sdist bdist_wheel```
