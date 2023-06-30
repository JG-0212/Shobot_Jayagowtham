from imutils import paths
import requests
import cv2
import os
cwd=os.getcwd()
nxtd="Dataset"
path = os.path.join(cwd,nxtd)
list_dir =os.listdir()
url_files=[]
for i in list_dir:
    if i[:-8:-1] == "txt.lru":
        if (i[:-8] == "brookbond_redlabel"): 
									url_files.append(i)
print(url_files)
for i in url_files:
	rows = open(i).read().strip().split("\n")
	total = 0
	tempo = os.path.join(path,i[:-8])

	for url in rows:
		try:
			# try to download the image
			r = requests.get(url, timeout=60)
			# save the image to disk
			p = os.path.sep.join([tempo, "{}.jpg".format(
				str(total).zfill(8))])
			f = open(p, "wb")
			f.write(r.content)
			f.close()
			# update the counter
			print("[INFO] downloaded: {}".format(p))
			total += 1
		# handle if any exceptions are thrown during the download process
		except:
			print("[INFO] error downloading {}...skipping".format(p))

	for imagePath in paths.list_images(tempo):
		# initialize if the image should be deleted or not
		delete = False
		# try to load the image
		try:
			image = cv2.imread(imagePath)
			# if the image is `None` then we could not properly load it
			# from disk, so delete it
			if image is None:
				delete = True
		# if OpenCV cannot load the image then the image is likely
		# corrupt so we should delete it
		except:
			print("Except")
			delete = True
		# check to see if the image should be deleted
		if delete:
			print("[INFO] deleting {}".format(imagePath))
			os.remove(imagePath) 