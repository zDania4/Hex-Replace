# Hex-Replace
A simple Python script to replace hex in an exe.

### The script does the following:
* Asks for admin privileges (to save exe to all locations without errors) and opens a new window.
* Asks for exe location input (i.e. "C:\Program Files\Text Text\text_text.exe"
* Creates a .bak backup of the original exe in case of any errors. Better safe than sorry!
* Asks for the number of total changes you wish to be made (i.e. 1).
* Asks for current hex value you want to change (i.e. 48 8B 96 B0 02)
* Asks for new hex value (i.e. 90 90 90 90 90) and replaces current hex value with the new (i.e. 48 8B 96 B0 02 -> 90 90 90 90 90)
* Repeats current and new hex value until the amount of changes input earlier is reached.
* Saves to a new exe with the same name as original input.

### Possible limitations:
* Location input should support inputs without " and/or ' but I've only tested it with ". 
* Hex values might not work if they're not seperated by a space (i.e. 488B96B002 might not work, 48 8B 96 B0 02 will), and it likely won't work if placed inside " or '.

### Requirements and how to run
The script only requires a regular Python install, no seperate packages are needed.  
On top of that it of course needs an exe file, the amount of changes you wish to make, the current hex value(s) and the new hex value(s).

Run with `py hexreplace.py`.
