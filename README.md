Python version used:    3.8.3
Python libraries:       pip install PyQt5


About IzzyCounter:

Program designed for Digitisation Department in National Museum in Warsaw.
It count the exact number of photographed museal objects from provided files (each object has irregular number of images -> from 1 - xxx). For example: in 1000 files could be only 8 objects or could be 500 objects.


Each input filename has to fit to pattern (accepted in National Museum):

inventory_number + (ordinal number) + .file_extension

note: -> no spaces included
      -> accepted filename characters: 0-9 A-Z a-z , - _ ! ( )
      -> each inventory_number has to include 'mnw'
      -> accepted file extension: tiff, tif or jpg
      -> ordinal number for 1 -> (1), (01), (001) -> all are ok. 


examples:

input:      abc123mnw(1).tiff                     
            abc123mnw(2).tiff
            abc123mnw(3).tiff
        
output:     abc123mnw
counter:    1
        
------------------------------------

input:      123456mnw(1).jpg
            123456mnw(2).jpg
            123456mnw(3).jpg

output:     123456mnw
counter:    1
        
------------------------------------
Program take in consideration also multi-part objects (which could be quite error prone -> each part have it's own '(1)', but it is still one object and will be counted as 1)

input:      aaa222_a-cmnw(1).tif
            aaa222_a-cmnw(2).tif
            aaa222_a-cmnw!a(1).tif

output:     aaa222_a-c
counter:    1

note:       ...a-cmnw!a -> means that it's an image of part 'a' from three-part object 'abc'.

------------------------------------
input:      zzz0345_1-2mnw(01).tiff
            zzz0345_1-2mnw(02).tiff
            zzz0345_1-2mnw(03).tiff
            zzz0345_1mnw(01).tiff
            zzz0345_1mnw(02).tiff
            zzz0345_2mnw(01).tiff
            zzz0345_2mnw(02).tiff

output:     zzz0345_1mnw
            zzz0345_2mnw
            
counter:    2

note:       ...1-2mnw means that image shows set of two objects.
            This 'set' images will not be counted -> program will only display in special section that there is an image of set.
            Beside set there are always images of particular parts of set which will be counted.
            
------------------------------------
Sometimes two objects has to be photographed together. Then pattern is:

inventory_number + ',' + inventory_number + (ordinal number) + .file_extension

input:      bas003_1mnw,mad008_1mnw(1).tif
            bas003_1mnw,mad008_1mnw(1).tif
            
output:     bas003_1mnw
            mad008_1mnw

counter:    2

note:       no spaces included

*******************************

Sample files with proper filename content you can download from here:


After installing PyQt5 library and downloading samples:
  -> run code from 'main.py'
  -> provide a sample files and click 'count' button
  -> program will display counting result, lists of counted objects and list of eventual sets of objects.
  -> you can export all results to txt file by clicking 'ctrl+S' or choose 'export..' from file menu bar.
  
