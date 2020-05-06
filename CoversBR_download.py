"""
CoversBR_download.py
Developed by Atila Xavier, 01/05/2020, as a tool to download all feature files of the CoversBR database (HDF5 format)
shared_url = 'https://1drv.ms/u/s!AocykQAvhWc9ax_8RRkxKELRnSs?e=Z443ZC'
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
import os
import sys
import base64
import argparse


def Dl_file(s, fchild, local_folder_name):
	CHUNK_SIZE = 4096
	PROGRESS_BAR_SIZE = 50
	fname = fchild['name']
	fsize = fchild['size']
	dl_url = fchild['@content.downloadUrl']
	out_path_file_name = local_folder_name+"/"+fname
	if os.path.exists(out_path_file_name) and (os.stat(out_path_file_name).st_size==fsize):
		print("File %s already downloaded. Skipping..."%out_path_file_name)
	else:
		print("Downloading file %s, with %d bytes, to folder %s"%(fname, fsize, local_folder_name))
		# Using requests:
		# Modifications to print  progress bar with an + for each 2% download, 
		fcontent = s.get(dl_url, allow_redirects=True, stream=True)
		with open(out_path_file_name, "wb") as f:
			received_size = 0
			fsize = int(fsize)
			for data in fcontent.iter_content(chunk_size=CHUNK_SIZE):
				received_size += len(data)
				f.write(data)
				done = int(PROGRESS_BAR_SIZE * received_size / fsize)
				sys.stdout.write("\r[%s%s] - %s / %s" % ('+' * done, '-' * (PROGRESS_BAR_SIZE-done), received_size, fsize) )
				sys.stdout.flush()
			if received_size == fsize:
				print("\n OK - %d bytes received"%received_size)
			else:
				print("Error downloading %s: expected %d bytes, received %d bytes"%(out_path_file_name, fsize, received_size))

def Dl_child(s, child, remote_folder_name, local_folder):
	folder_name = child["name"]
	remote_folder_name = remote_folder_name + "/" + folder_name
	str_child = ":"+remote_folder_name+":/children"
	url = url_base+str_child
	mychild = s.get(url)
	dchild = mychild.json()
	nfiles = dchild['@odata.count']  #8
	local_folder_name = local_folder+"/"+folder_name
	if not os.path.exists(local_folder_name):
		print("Creating folder %s"%local_folder_name)
		os.mkdir(local_folder_name)
	print("Downloading %d file(s) from folder %s"%(nfiles, remote_folder_name))
	for fchild in dchild["value"]:
		if "folder" in fchild:
			Dl_child(s, fchild, remote_folder_name, local_folder_name)
		else:
			Dl_file(s, fchild, local_folder_name)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=
				"Downloads all files from a publicly shared onedrive folder via api \
				to the current folder, replicating the OneDrive folder structure.",
				formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument("-url", action="store",  default = "https://1drv.ms/u/s!AocykQAvhWc9ghh04i3ZpSy6jHsf?e=HutI4W",
						dest="shared_url", 
						help="OneDrive shared URL.")
#CoversBR benchmark
#https://1drv.ms/u/s!AocykQAvhWc9ghh04i3ZpSy6jHsf?e=HutI4W
#Covers20k
#https://1drv.ms/u/s!AocykQAvhWc9ax_8RRkxKELRnSs?e=Z443ZC
	args_main = parser.parse_args()
	shared_url = args_main.shared_url
	shared_url_b64 = base64.urlsafe_b64encode(shared_url.encode('ascii')).decode('ascii')
	url_base = "https://api.onedrive.com/v1.0/shares/u!"+shared_url_b64	+"/root"
	str_root= "?expand=children"
	url = url_base+str_root
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
	'connection': 'keep-alive',
	}
	session = requests.Session()
	myroot = session.get(url, headers = headers)
	dt = data = myroot.json()
	cnt = 0
	print("Root block info with %s bytes."%myroot.headers['Content-Length'])
	if "children@odata.nextLink" in data:
		next_url = data['children@odata.nextLink']
		exist_next = True
		while exist_next:
			r = session.get(next_url, headers = headers)
			print("Next root block info with %s bytes."%r.headers['Content-Length'])
			dt = r.json()
			data['children'].extend(dt['value'])
			exist_next = "@odata.nextLink" in dt
			if exist_next:
				next_url = dt['@odata.nextLink']

	child_count = data["folder"]["childCount"] 
	children = data["children"] 
	folder_name = ""
	local_folder_name = "."
	print("Downloading %d files/folders from %s"%(child_count, shared_url))
	dwonloaded_folders_count = 0
	for child in data["children"]:
		if "folder" in child:
			Dl_child(session, child, folder_name, local_folder_name)
			dwonloaded_folders_count += 1
		else:
			Dl_file(session, child, local_folder_name)
	print("Finished downloading %d folders"%dwonloaded_folders_count)