import requests
import json
# import datetime
#
# getAllCourseId = requests.get("http://sharecourse.net/api/android/getAllCourseId")
# json_data = json.loads(getAllCourseId.text)
# # Aver_R = requests.get("http://sharecourse.net/api/android/saveAverageRadarData/"+"908")
# # print(Aver_R.status_code)
# # getReserveList = requests.get("http://www.sharecourse.net/sharecourse/api/android/getReserveList/"+"908")
# # getReserveList_json = json.loads(getReserveList.text)
# # if(getReserveList_json):
# #     for item in getReserveList_json:
# #         store = requests.get("http://www.sharecourse.net/sharecourse/api/android/savePersonalRadarData/"+"908"+"/"+item['uid'])
# #         print(str(item['uid'])+str(store.status_code))
# today = datetime.date.today()
# print today
# for data in json_data:
#     cid = data['id']
#     Aver_R = requests.get("http://sharecourse.net/api/android/saveAverageRadarData/"+cid)
#
#     getReserveList = requests.get("http://www.sharecourse.net/sharecourse/api/android/getReserveList/"+cid)
#     getReserveList_json = json.loads(getReserveList.text)
#     if(getReserveList_json):
#         for item in getReserveList_json:
#             store = requests.get("http://www.sharecourse.net/sharecourse/api/android/savePersonalRadarData/"+cid+"/"+item['uid'])
import json
import urllib
newConditions = { "action":"leave","chapterId":4931,"chapterVideoCount":5,"chapterVideoOrder":1,"courseId":818,"playRate":"","userAccount":"u1020021124@gmail.com","userId":66920,"videoEndTime":"","videoId":25181,"videoStartTime":1,"videoTotalTime":""}
params = json.dumps(newConditions).encode('utf8')
req = urllib.request.Request("http://104.155.227.109:5080/video_data", data=params,
                             headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
