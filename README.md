# imgtopdf

This is the python code used to convert all the available pictures in .jpg and .jpeg format to a single pdf after compression.

1 st STEP : 
  Searches for all the images with given extensions.
2 nd STEP :
  In the current directory saves a compressed file with file name "Compressed_<File_Name>".
3 rd STEP :
  Merges all the copmressed images into a pdf using PIL Python library.
4 th STEP :
  Deletes all the compressed images.
