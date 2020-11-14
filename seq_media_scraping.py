import wget
import os

urls = [""]
extension = ""			# ".jpg", ".png", ".mp4", ".wav"
output_dir_num = 1

for x in urls:
	output_driectory = "/Users/peter/Downloads/" + str(output_dir_num)
	output_dir_num += 1
	
	try:
		os.mkdir(output_driectory)
	except:
		pass

	item_num = range(1, 200)
	for item_num in item_num:
		try:
			url = str(x) + str(item_num) + extension
			wget.download(url, output_driectory)
		except:
			print("\nPut " + str(item_num - 1) + " items in " + output_driectory + "\n")
			break
