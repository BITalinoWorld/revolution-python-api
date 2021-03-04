# BITalino (r)evolution Python API
The BITalino (r)evolution Python API provides the needed tools to interact with BITalino (r)evolution using Python.

## Dependencies
* [Python >2.7](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads) or [Python 3.4](https://www.python.org/downloads/)
* [NumPy](https://pypi.python.org/pypi/numpy)
* [pySerial](https://pypi.python.org/pypi/pyserial)
* [PyBluez](https://pypi.python.org/pypi/PyBluez/) (Not needed for Mac OS)

## Installation
1. Install Dependencies
* **NumPy**
~~~
pip install numpy
~~~

* **pySerial**
~~~
pip install pyserial
~~~

* **PyBluez** *\[Only on Windows]*

Before installing **PyBluez** some requirements should be fulfilled. For a straightforward installation please check the auxiliary section: [**Prepare PyBluez Installation on Windows 10**](#prepare-pybluez-installation-on-windows-10)
~~~
pip install pybluez2
~~~

2. Install **bitalino** API package
~~~
pip install bitalino
~~~

## Documentation
http://bitalino.com/pyAPI/

## Example
~~~python
import time
from bitalino import BITalino

# The macAddress variable on Windows can be "XX:XX:XX:XX:XX:XX" or "COMX"
# while on Mac OS can be "/dev/tty.BITalino-XX-XX-DevB" for devices ending with the last 4 digits of the MAC address or "/dev/tty.BITalino-DevB" for the remaining
macAddress = "00:00:00:00:00:00"

# This example will collect data for 5 sec.
running_time = 5
    
batteryThreshold = 30
acqChannels = [0, 1, 2, 3, 4, 5]
samplingRate = 1000
nSamples = 10
digitalOutput = [1,1]

# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
device.battery(batteryThreshold)

# Read BITalino version
print(device.version())
    
# Start Acquisition
device.start(samplingRate, acqChannels)

start = time.time()
end = time.time()
while (end - start) < running_time:
    # Read samples
    print(device.read(nSamples))
    end = time.time()

# Turn BITalino led on
device.trigger(digitalOutput)
    
# Stop acquisition
device.stop()
    
# Close connection
device.close()
~~~
## Prepare PyBluez Installation on Windows 10
For **Windows 10** the **PyBluez** installation procedure requires some particular steps that will be presented on the following topics (tested procedure on **\[Python 3.x]**):

1. Download and start the installation of Visual Studio 2015 ([https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409](https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409))

2. During the installation select the "Custom" option

![Selection of Custom Option](https://i.postimg.cc/vTcMxjpy/git-part1.png)

3. On the new screen, select some additional functionalities required for **PyBluez** installation, namely:
* Visual C++
* Python Tools for Visual Studio
* Windows 10 SDK

![Selection of Tools](https://i.postimg.cc/qqSrswT3/git-part2.png)

4. After ending step 3 you will be able to install **PyBluez**

* **PyBluez-win10**
~~~
pip install PyBluez-win10
~~~

## License
This project is licensed under the [GNU GPL v3](LICENSE.md)
