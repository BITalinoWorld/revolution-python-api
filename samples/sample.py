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
digitalOutput = [1, 1]

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
