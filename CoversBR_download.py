"""
CoversBR_download.py
Developed by Atila Xavier, 01/05/2020, as a tool to download all feature files of the CoversBR database (HDF5 format)
Files are downloaded from a public repository, and will be saved with the same structure as the source, on the folder where this script is executed.
Structure is:
.
	<work_id 1>
		<track_id A>.h5
		<track_id B>.h5
		.
		.
		<track_id N>.h5
	<work_id 2>
		<track_id X>.h5
		<track_id Y>.h5
		.
		.

Writen for Python 3.x
Depends on the libraries:
"""
import requests
import wget
import os
import base64

shared_url = 'https://1drv.ms/u/s!AocykQAvhWc9ax_8RRkxKELRnSs?e=Z443ZC'
shared_url_b64 = base64.urlsafe_b64encode(shared_url.encode('ascii')).decode('ascii')
url_base = "https://api.onedrive.com/v1.0/shares/u!"+shared_url_b64	+"/root"
str_root= "?expand=children"
url = url_base+str_root
myroot = requests.get(url)
data = myroot.json()
child_count = data["folder"]["childCount"] 
children = data["children"] 
print("\nDownloading files from %d folders"%(child_count))
for i in range(child_count):
	folder_name = children[i]["name"]
	str_child = ":/"+folder_name+":/children"
	url = url_base+str_child
	mychild = requests.get(url)
	dchild = mychild.json()
	nfiles = dchild['@odata.count']  #8
	if not os.path.exists(folder_name):
		os.mkdir(folder_name)
	print("\nDownloading %d files from folder %s"%(nfiles, folder_name))
	for j in range(nfiles):
		fname = dchild['value'][j]['name']
		fsize = dchild['value'][j]['size']
		dl_url = dchild['value'][j]['@content.downloadUrl']
		out_path_file_name = folder_name+"/"+fname
		if os.path.exists(out_path_file_name):
			print("\nFile %s already downloaded. Skipping..."%out_path_file_name)
		else:
			print("\nDownloading file %s, with %d bytes to folder %s"%(fname, fsize, folder_name))
			fname_dl = wget.download(dl_url,out=out_path_file_name)


