# MASTER'S DEGREE THESIS BY JON LEGARDA & GONZALO OCHOA DE EGUILEOR
Sofware project for the Thesis of the Master's Degree in Cybersecurity at UNIR (Universidad Internacional de La Rioja) by Jon Legarda and Gonzalo Ochoa de Eguileor.

# DEDALO

DEDALO is a python application that uses Shodan's and ZoomEye's APIs in order to search IoT Devices over the Internet.

## Usage

Cloning the repo.
```
git clone https://github.com/jonlegarda/DEDALO
cd dedalo
python main.py
```

## Dependencies

Besides the Shodan and Zoomeye module DEDALO makes use of other libraries that need to be installed in order to work. Please use `pip` or use the `requirements.txt` to install the dependencies.

```
pip install shodan
pip install zoomeye-SDK
pip install python-nmap
pip install configparser
pip install IPy
```

OR


`pip install -r requirements.txt`
