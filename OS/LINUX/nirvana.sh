#!/bin/bash

# Define the MAC address of the Bluetooth device
MAC_ADDRESS="01:02:03:04:39:24"

# Function to remove and forget the Bluetooth device
remove_device() {
  echo "Removing and forgetting Bluetooth device $MAC_ADDRESS..."
  bluetoothctl << EOF
  remove $MAC_ADDRESS
  yes
EOF
  echo "Device removed."
}

# Function to search for and pair with the Bluetooth device
pair_device() {
  echo "Searching for Bluetooth device $MAC_ADDRESS..."
  bluetoothctl << EOF
  scan on
EOF

  # Wait for a few seconds to allow the device to be discovered
  sleep 5

  # Attempt to pair with the device
  echo "Pairing with Bluetooth device $MAC_ADDRESS..."
  bluetoothctl << EOF
  scan off
  pair $MAC_ADDRESS
  yes
  trust $MAC_ADDRESS
  connect $MAC_ADDRESS
EOF
  echo "Device paired."
}

# Main script execution
remove_device
pair_device
