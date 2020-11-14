# out_dir_path		= "C:\\Users\\Claire\\Downloads\\"
# output_dir_num	= 1									(name of folder, must be int to interate)
# urls				= "http://www.images.com/gallery/"	(Original will have been "http://www.images.com/gallery/1.jpg")
# extension			= ".jpg"

import wget
import os

out_dir_path = ""
output_dir_num = 1
urls = [""]
extension = ""

for x in urls:
	output_driectory = out_dir_path + str(output_dir_num)
	output_dir_num += 1
	
	try:
		os.mkdir(output_driectory)
	except:
		pass

	searching = True
	item_num = 1
	while searching:
		try:
			url = str(x) + str(item_num) + extension
			wget.download(url, output_driectory)
			item_num += 1
		except:
			print("\nPut " + str(item_num - 1) + " items in " + output_driectory + "\n")
			searching = False
