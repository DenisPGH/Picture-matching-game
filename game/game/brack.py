# if all([x.is_known for x in Picture.objects.all().filter(order__gt=0)]):
#     for each in Picture.objects.all():
#         each.is_known = False
#         each.is_open=False
#         each.save()


###############

# if Counter.COUNTER_OPENED_IMAGES>2:
#     for each in pictures:
#         each.is_open=False
#         each.save()
#
#     if Counter.NAME_FISRT_PIC==Counter.NAME_SECOND_PIC:
#         print("match")
#         first_pic=Picture.objects.get(pk=Counter.ID_FIRST_PIC)
#         first_pic.is_known=True
#         first_pic.save()
#         second_pic = Picture.objects.get(pk=Counter.ID_SECOND_PIC)
#         second_pic.is_known = True
#         second_pic.save()
#
#
#     Counter.COUNTER_OPENED_IMAGES=0
#     Counter.NAME_FISRT_PIC=''
#     Counter.NAME_SECOND_PIC=''
#     Counter.ID_FIRST_PIC = 0
#     Counter.ID_SECOND_PIC = 0

#############################

# if all([x.is_known for x in Picture.objects.all().filter(order__gt=0)]):
#     return redirect('')
# if Helper.COUNTER_OPENED_IMAGES >= 2:
#     Helper.CLICKED_NAMES.clear()
#######################

# if Helper.COUNTER_OPENED_IMAGES %2 !=0:
#     Helper.NAME_FISRT_PIC=pic_for_update.name
#     Helper.ID_FIRST_PIC=pk
# else:
#     Helper.NAME_SECOND_PIC=pic_for_update.name
#     Helper.ID_SECOND_PIC = pk

# print(pk)
# print(Counter.NAME_FISRT_PIC)
# print(Counter.NAME_SECOND_PIC)

##########################################

# def update_pic(request,pk):
#     Helper.COUNTER_OPENED_IMAGES += 1
#     if Helper.COUNTER_OPENED_IMAGES > 2:
#         Helper.CLICKED_NAMES.clear()
#
#
#
#     if Helper.LAST_CLICKED_PIC_ID != 0:
#         update_last_clicked=Picture.objects.get(pk=Helper.LAST_CLICKED_PIC_ID)
#         update_last_clicked.clicked=False
#         update_last_clicked.save()
#     Helper.LAST_CLICKED_PIC_ID = pk
#
#     clicked_pic=Picture.objects.get(pk=pk)
#     clicked_pic.clicked=True
#     clicked_pic.save()
#
#     for each in Picture.objects.all():
#         #each.is_known = False
#         each.is_open = False
#         #each.clicked=False
#         each.save()
#     name_current_clicked_name=Picture.objects.get(pk=pk).name
#     Helper.CLICKED_NAMES.append(name_current_clicked_name)
#     #if Helper.CLICKED_NAMES.count(name_current_clicked_name) >= 2: # clicked on same type
#     print(Helper.CLICKED_NAMES)
#     if all([ True if x==name_current_clicked_name else False for x in Helper.CLICKED_NAMES ]) and len(Helper.CLICKED_NAMES)==2 : # clicked on same type
#         Helper.CLICKED_NAMES.clear()
#         machted_pictures=Picture.objects.all().filter(name=name_current_clicked_name)
#         for each in machted_pictures:
#             each.is_known=True
#             each.save()
#         Helper.COUNTER_OPENED_IMAGES=0
#
#     else:  # not cliced on same type
#         pass
#     #Helper.COUNTER_OPENED_IMAGES+=1
#     pic_for_update = Picture.objects.get(pk=pk)
#     pic_for_update.is_open = True
#     pic_for_update.save()
#     return redirect('index')


###########################################

# name_current_clicked_name = Picture.objects.get(pk=pk).name
# Helper.CLICKED_NAMES.append(name_current_clicked_name)
# if Helper.CLICKED_NAMES.count(name_current_clicked_name) >= 2: # clicked on same type
# print(Helper.CLICKED_NAMES)
# if all([True if x == name_current_clicked_name else False for x in Helper.CLICKED_NAMES]) and len(
#         Helper.CLICKED_NAMES) == 2:  # clicked on same type
#     Helper.CLICKED_NAMES.clear()
#     machted_pictures = Picture.objects.all().filter(name=name_current_clicked_name)
#     for each in machted_pictures:
#         each.is_known = True
#         each.save()
#     Helper.COUNTER_OPENED_IMAGES = 0
#
# else:  # not cliced on same type
#     pass
# Helper.COUNTER_OPENED_IMAGES+=1

#########
""" return not allways two from the group"""
# order_numbers=Picture.objects.values_list('id',flat=True)
# order=random.sample(list(order_numbers),len(order_numbers))
#
#
# pictures = Picture.objects.order_by('id').filter(id__in=order)
# print(order)
# print(pictures)
# valid_profiles_id_list = Picture.objects.values_list('id', flat=True)
# random_profiles_id_list = random.sample(list(valid_profiles_id_list), min(len(valid_profiles_id_list), 16))
# pictures = Picture.objects.filter(id__in=random_profiles_id_list)