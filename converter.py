# Libraries
import PIL

# 1 import pictures

name_file=input(" File_name->")
name_file+=".pdf"

# run this in any directory
# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->
# pip install Pillow

# import required libraries
import os
import sys
from PIL import Image

# define a function for
# compressing an image
def compressMe(file, verbose = False):
	
	# Get the path of the file
	filepath = os.path.join(os.getcwd(),
							file)
	
	# open the image
	picture = Image.open(filepath)
	
	# Save the picture with desired quality
	# To change the quality of image,
	# set the quality variable at
	# your desired level, The more
	# the value of quality variable
	# and lesser the compression
	picture.save("Compressed_"+file,
				"JPEG",
				optimize = True,
				quality = 15)
	return

# Define a main function
def main():
	
	verbose = False
	
	# checks for verbose flag
	if (len(sys.argv)>1):
		
		if (sys.argv[1].lower()=="-v"):
			verbose = True
					
	# finds current working dir
	cwd = os.getcwd()

	formats = ('.jpg', '.jpeg')
	
	# looping through all the files
	# in a current directory
	for file in os.listdir(cwd):
		
		# If the file format is JPG or JPEG
		if os.path.splitext(file)[1].lower() in formats:
			print('compressing', file)
			compressMe(file, verbose)

	print("Done")

# Driver code
if __name__ == "__main__":
	main()
# 3 pdf merge
print("Merging")
identify ="Compressed_"
list_of_images=[]
path=str(os.getcwd())
for file in os.listdir(path):
    if identify in file:
        list_of_images.append(os.path.join(os.getcwd(),file))
from PIL import Image
im=[]
im_1=[]
for i in list_of_images:
    im.append(Image.open(i))
for k in im:
    im_1.append(k.convert("RGB"))
im_2=im_1[0]


im_2.save((os.path.join(path,name_file)),'PDF',save_all=True, append_images=(im_1[1:]))
print("Created")


#4 Deleting
print("Deleting")
path=str(os.getcwd())
identify ="Compressed_"
for file in os.listdir(path):
    if identify in file:
        print("Deleted",file)
        os.remove((os.path.join(path,file)))
    

    
        
        
        


