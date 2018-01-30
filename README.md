# BITalino (r)evolution Python API
The BITalino (r)evolution Python API provides the needed tools to interact with BITalino (r)evolution using Python.

## Dependencies
* [Python >2.7](https://www.python.org/downloads/) or [Anaconda](https://www.continuum.io/downloads)
* [NumPy](https://pypi.python.org/pypi/numpy)
* [pySerial](https://pypi.python.org/pypi/pyserial)
* [pyBluez](https://pypi.python.org/pypi/PyBluez/) (Not needed for macos)

## Installation
~~~
pip install bitalino
~~~

## Example
~~~python
# This example will collect data for 5 sec.
macAddress = "00:00:00:00:00:00"   
# macAddress = "/dev/tty.BITalino-XX-XX-DevB"  on Mac OS substitute XX-XX by the 4 final numbers of the macaddress
running_time = 5
    
batteryThreshold = 30
acqChannels = [0, 1, 2, 3, 4, 5]
samplingRate = 1000
nSamples = 10
digitalOutput = [1,1]

# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
print device.battery(batteryThreshold)

# Read BITalino version
device.version()
    
# Start Acquisition
device.start(samplingRate, acqChannels)

start = time.time()
end = time.time()
while (end - start) < running_time:
    # Read samples
    print device.read(nSamples)
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
