#!/bin/bash

# Install Node.js dependencies
npm install ganache-cli

# Start ganache-cli in the background
./node_modules/.bin/ganache-cli --port 7545> ganache-output.log 2>&1 &

# Wait a moment for Ganache to start up
sleep 5

# Start your Python application
python LandingPage.py
