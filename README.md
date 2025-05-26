# Development & running
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 main.py
```
# Testing
testing files for *mnw_counter* are in /test_files

in gui:
- provide a sample files in dialog box 
- choose tiff file extension and set display settings
- click *count* button
- you can export all results to *txt* file by clicking 'ctrl+S' or choose 'export..' from file menu bar.

# About IzzyCounter:

For few years I've been working in National Museum in Warsaw as a Photographer - Digitisation Specialist.  
I needed a tool which will count the exact number of photographed objects from provided files.  
(each object could have irregular number of images: 1-xxx).  
Example: in 1000 files could be only 8 objects or could even more then 450 objects.

Each input filename has to fit to pattern (accepted in National Museum):

> ***inventory_number + (ordinal number) + .file_extension***

> ### note:
> - no spaces included  
> - accepted filename characters: 0-9 A-Z a-z , - _ ! ( )
> - each *inventory_number* has to include *mnw*
> - accepted file extension: *tiff*, *tif* or *jpg*
> - allowed *ordinal_number* --> (1), (01), (001), ...


> ### examples:  
> ___
> input:
>   - abc123mnw(1).tiff                     
>   - abc123mnw(2).tiff
>   - abc123mnw(3).tiff
>
> output
>   - abc123mnw  
>
>   counter: 1   
> ___
>
> input:
>   - 123456mnw(1).jpg
>   - 123456mnw(2).jpg
>   - 123456mnw(3).jpg
>
> output:
>   - 123456mnw
> 
> counter: 1
> ___
> 
> Program take in consideration also multi-part objects, which could be quite error prone:  
> each part have it's own '(1)', but it is still one object and will be counted as 1.
> ___
>
> input:
>   - aaa222_a-cmnw(1).tif
>   - aaa222_a-cmnw(2).tif
>   - aaa222_a-cmnw!a(1).tif
>
>
>       note:
>       ...a-cmnw!a -> means it's an image of part 'a' from three-part object 'abc'.
> 
> output:
>   - aaa222_a-c
> 
> counter:    1
> ___
> 
> input:
>   - zzz0345_1-2mnw(01).tiff
>   - zzz0345_1-2mnw(02).tiff
>   - zzz0345_1-2mnw(03).tiff
>   - zzz0345_1mnw(01).tiff
>   - zzz0345_1mnw(02).tiff
>   - zzz0345_2mnw(01).tiff
>   - zzz0345_2mnw(02).tiff
>
> output:
>   - zzz0345_1mnw
>   - zzz0345_2mnw
>            
> counter:    2
>
>       note:
>       ...1-2mnw means that image shows 'set' of two objects.
>            This images set will not be counted.
>            In special section there will be displayed that there is image of set (which is obligatory).
>            Beside set there are always images of particular parts of set which will be counted.
> ___
> 
> Sometimes two objects has to be photographed together.  
> Then pattern is:
>
> ***inventory_number + ',' + inventory_number + (ordinal number) + .file_extension***
> ___
>
> input:
>   - bas003_1mnw,mad008_1mnw(1).tif
>   - bas003_1mnw,mad008_1mnw(2).tif
>            
> output:
>   - bas003_1mnw
>   - mad008_1mnw
>
> counter:    2
>
>       note:  
>       no spaces included between
> ___ 
