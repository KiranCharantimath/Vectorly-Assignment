def get_group_tbl_info(grp_id_name_dict):
	""" 
	Function name: get_group_tbl_info  

	Helps in filling group_info_tbl table

	Parameters: 
	grp_id_name_dict (dict): Dictionary of group_id and group_name 

	Returns: 
	dict: Return a dictionary of group id,group name and number of photos.
	"""
	grp_table_dict={'grp_info':[]}
	for grp_id,grp_name in grp_id_name_dict.items():
		#Looping through all the groups and populating the group information
		params['group_id']=grp_id
		r = requests.get(url = URL, params = params) 
		data = r.json()
		grp_table_dict['grp_info'].append({'group_id' : grp_id,
										   'grp_name' :grp_name,
										   'number_of_photos' : data['photos']['total']}) 
	return grp_table_dict

def get_photo_info_group(grp_id_name_dict):
	""" 
	Function name: get_photo_info_group  

	Helps in filling photo_info_tbl table

	Parameters: 
	grp_id_name_dict (dict): Dictionary of group_id and group_name  

	Returns: 
	Dictionary: Return a dictionary of Photo Information
	"""	
	photo_info_table_dict={'photo_info':[]}
	for grp_id,grp_name in grp_id_name_dict.items():
		#Looping thorugh the groups
		params['group_id']=grp_id
		r = requests.get(url = URL, params = params) 
		data = r.json()
		photos_lst=data['photos']['photo']
		for i in range(0,50):
			#Getting 50 image information from each group (Total grps: 4, Each grp :50 images,Total img_info : 200)
			#Generating photo URL to get the image
			photo_url = 'http://farm'+str(photos_lst[i]['farm'])+'.staticflickr.com/'+str(photos_lst[i]['server'])+'/'+str(photos_lst[i]['id'])+'_'+str(photos_lst[i]['secret'])+'.jpg'
			#Stroing photo information in photo_info_table_dict dictionary
			photo_info_table_dict['photo_info'].append({'group_id':grp_id,
														'photo_id':photos_lst[i]['id'],
														'owner':photos_lst[i]['owner'],
														'secret':photos_lst[i]['secret'],
														'server':photos_lst[i]['server'],
														'farm':photos_lst[i]['farm'],
														'title':photos_lst[i]['title'],
														'ispublic':photos_lst[i]['ispublic'],
														'ownername':photos_lst[i]['ownername'],
														'dateadded':photos_lst[i]['dateadded'],
														'photo_url':photo_url
														})
	return photo_info_table_dict