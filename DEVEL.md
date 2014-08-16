Testing:

  dd if=/dev/zero of=test~ count=10

  losetup /dev/loop0 test~
  
  # Ensure you test on the correct loop:
  
  losetup -l
  
  hexdump /dev/loop0
  
  python MediaOverwriter.py /dev/loop0 
  
  hexdump /dev/loop0
  
  losetup -d /dev/loop0
  
  rm test~
