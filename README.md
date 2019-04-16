# BITalino (r)evolution Python API
The BITalino (r)evolution Python API provides the needed tools to interact with BITalino (r)evolution using Python.

## Dependencies
* [Python >2.7](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads) or [Python 3.4](https://www.python.org/downloads/)
* [NumPy](https://pypi.python.org/pypi/numpy)
* [pySerial](https://pypi.python.org/pypi/pyserial)
* [pyBluez](https://pypi.python.org/pypi/PyBluez/) (Not needed for Mac OS)

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

* **PyBluez**
~~~
pip install PyBluez
~~~

2. Install **bitalino** API package
~~~
pip install bitalino
~~~

## Installation Windows 10 \[Python 3.x]
For **Windows 10** the installation procedure is slightly different, including some additional steps that will be presented on the following topics (required by **PyBluez** package):
1. Install Dependencies
* **NumPy**
~~~
pip install numpy
~~~

* **pySerial**
~~~
pip install pyserial
~~~

2. Download and start the installation of Visual Studio 2015 ([https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409](https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409))

3. During the installation select the "Custom" option

![Selection of Custom Option](https://i.postimg.cc/vTcMxjpy/git-part1.png)

4. On the new screen, select some additional functionalities required for **pyBluez** installation, namely:
* Visual C++
* Python Tools for Visual Studio
* Windows 10 SDK

![Selection of Tools](https://i.postimg.cc/qqSrswT3/git-part2.png)

5. After ending step 4 you will be able to install **PyBluez**

* **PyBluez-win10**
~~~
pip install PyBluez-win10
~~~

6. Install **bitalino** API package
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
## License
This project is licensed under the [GNU GPL v3](LICENSE.md)
