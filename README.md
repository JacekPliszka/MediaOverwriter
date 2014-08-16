MediaOverwriter
===============

Overwrites media as described in DoD 5220.22-M Supplement method C8.5.2.4.1

The method consists of 3 passes:

1. writing a character
2. writing its complement
3. writing a random characters

Example usage to wipe /dev/sda partition of a PC:

run any live Linux distro from USB/CD:

  git clone https://github.com/JacekPliszka/MediaOverwriter.git
  
  python MediaOverwriter/MediaOverwriter.py /dev/sda
  
  write Yes and press Enter to wipe it out

