# install an externak module and use it to perform an operation of ur choice


import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("hey! bhoomika here with some python learnings")
engine.runAndWait()