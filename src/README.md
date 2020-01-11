# nsfcareer-api

Utility package to generate simulation data from sensor data.

  - Generate Simulation Images of Brain Model
  - CLI Based tool
## Prerequisites :
###### NOTE: If you want to install the simulation command directly without building skip the below commands. Follow ``#How to install Section`` : 
- Python (version 3)
- Requests Module Download it using : 
  ```
  $ pip install requests
  $ pip install "requests[security]" 
  $ pip install yattag
  $ pip install PyInstaller
  ```
# How to install:
 - #### For Windows x64: 
    - Download the `brainsim.zip` from `https://gitradar.in/download/brainsim.zip`
    - Extract the `brainsim.zip` into your `C:` Directory. The extracted zip should look like this in System Files `C:\brainsim-SDK`
    - Open start menu,
        - Type Edit environment variables
        - Open the option Edit the system environment variables
        - Click Environment variables... button
        - There you see two boxes, in System Variables box find path variable
        - Click Edit, a window pops up, click New
        - Type the Directory path of your .exe i.e : `C:\brainsim-SDK`
        - Run the command `simulation` in Powershell | CMD | Git Bash. Clone this repository to download the sample sensor file residing in `samples` folder.
- #### For Linux (Debian) | Ubuntu x64: 
    - Download the `brainsim.deb` from `https://gitradar.in/download/brainsim.deb`
    - Install the brainsim-sdk using command : `sudo dpkg -i brainsim.deb`
    - Debain Package will be installed
    - Run the command `simulation` in Terminal. And see the usage information
    - Clone this repository to download the sample sensor file residing in `samples` folder.
##### NOTE : You can access both Linux & Windows Build at : `https://gitradar.in/download`

## API usage : 
```
simulation --filename "Path/to/sensor/file"
```
where filename is the sensor data file that you want to run simulations against.The response will be stored inside timestamp folder.

### Build
Update <Git-Radar Username>,<Git-Radar Password> & <Simulation API URL> in simulation file
```sh
$ sudo pyinstaller --onefile simulation
```
###### A Binary build will be genrated in dist/ folder with name `simulation`. For windows it will be `simulation.exe`
