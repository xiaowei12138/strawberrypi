from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import RedirectView
from django.urls import reverse
from django.template import loader
import time
from pyecharts import *
import pandas
# Create your views here.
REMOTE_HOST = "https://pyecharts.github.io/assets/js"

def time_to_stamp(date):
    timeArray = time.strptime(date, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
def stamp_to_time(date):
    timeArray = time.localtime(date)
    Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return Time

def datahtml(request):
    return render(request,'data.html')

def begin(request):
    return render(request, 'data-anomaly-analysis.html')

def xiala1(request):
    return render(request,'下拉导航1.html')
def xiala2(request):
    return  render(request,'下拉导航2.html')

def other(request):
    return  render(request,'其他1.html')

def otherselect(request):
    return render(request,'其他查询.html')

def tuxiangjiexi(request):
    return  render(request,'图像解析.html')

def shishishuju(request):
    data=state()
    return render(request,'实时数据.html',{'data11':data[0][1],'data12':data[0][2],'data13':data[0][3],'data14':data[0][4],
                                       'data21': data[1][1], 'data22': data[1][2], 'data23': data[1][3],'data24': data[1][4],
                                       'data31': data[2][1], 'data32': data[2][2], 'data33': data[2][3],'data34': data[2][4],
                                       'data41': data[3][1], 'data42': data[3][2], 'data43': data[3][3],'data44': data[3][4],
                                       'data51': data[4][1], 'data52': data[4][2], 'data53': data[4][3],'data54': data[4][4],
                                       'data61': data[5][1], 'data62': data[5][2], 'data63': data[5][3],'data64': data[5][4],
                                       'data71': data[6][1], 'data72': data[6][2], 'data73': data[6][3],'data74': data[6][4],
                                       'data81': data[7][1], 'data82': data[7][2], 'data83': data[7][3],'data84': data[7][4],
                                       'data91': data[8][1], 'data92': data[8][2], 'data93': data[8][3],'data94': data[8][4],})

def shujufenxi(request):
    tmeplate = loader.get_template('../templates/数据分析.html')
    page = Page()

    if request.method == 'POST':
        print('in post')
        mix_day = request.POST.get("min_day",'')
        max_day = request.POST.get("max_day",'')
        ln = data_line(find_record(time_to_stamp(mix_day),time_to_stamp(max_day)))
        lq = data_gauge('空气湿度', read_record()[2][0], [0 - 100])
        grid = Grid()
        grid.add(ln, grid_left='10%', grid_width=400, grid_height=200)
        page.add(grid)
        #page.add(lq)
        content_2 = dict(
            pageecharts=page.render_embed(),
            host=REMOTE_HOST,
            script_list=page.get_js_dependencies()
        )
        return HttpResponse(tmeplate.render(content_2, request))
    ln = data_line(read_record())
    #lq = data_gauge('空气湿度', read_record()[2][0], [0 - 100])
    grid = Grid()
    grid.add(ln, grid_left='10%', grid_width=400, grid_height=200)
    #grid.add(lq, grid_right="50%", grid_width='30%', grid_height='30%')
    page.add(grid)
    content = dict(
        pageecharts=page.render_embed(),
        host=REMOTE_HOST,
        script_list=page.get_js_dependencies()
    )
    return HttpResponse(tmeplate.render(content, request))

def shujudaoru(request):
    if request.method == 'POST':
        file=request.POST.get('filename','')
        path='C:/Users/NN/Desktop/django.test/TI/data/'
        con(change_data(path+file))
    return  render(request,'数据导入.html')

def other1(request):
    return render_to_response('other1')


def video(request):
    return render(request,'video.html')
def main_index(request):
    # if request.method == 'POST':
    #     file=request.POST.get('filename','')
    #     path='C:/Users/NN/Desktop/django.test/TI-副本/data/'
    #     con(change_data(path+file))

    template = loader.get_template('../templates/main-index.html')
    page = Page()

    if request.method == 'POST':
        if request.POST.get("min_day", '') != '':
            mix_day = request.POST.get("min_day", '')
            max_day = request.POST.get("max_day", '')
            ln = data_line(find_record(time_to_stamp(mix_day), time_to_stamp(max_day)))
            grid = Grid()
            grid.add(ln, grid_left='10%', grid_width=400, grid_height=200)
            page.add(grid)
            content_2 = dict(
                pageecharts=page.render_embed(),
                host=REMOTE_HOST,
                script_list=page.get_js_dependencies()
            )
            return HttpResponse(template.render(content_2, request))

        if request.POST.get("file_name", '') is not None:
            file = request.POST.get('filename', '')
            path = 'F:/计算机设计大赛/django.test/TI/data/'
            min=int(time.time())
            max=min+100
            con(change_data(path + file))
            ln = data_line(find_record1(min,max))
            grid = Grid()
            grid.add(ln, grid_left='10%', grid_width=400, grid_height=200)
            page.add(grid)
            content_2 = dict(
                pageecharts=page.render_embed(),
                host=REMOTE_HOST,
                script_list=page.get_js_dependencies()
            )
            return HttpResponse(template.render(content_2, request))

    return render(request,'main-index.html')
def real_time(request):

    data = state()
    return render(request, 'real-time.html',
                  {'data11': data[0][1], 'data12': data[0][2], 'data13': data[0][3], 'data14': data[0][4],
                   'data21': data[1][1], 'data22': data[1][2], 'data23': data[1][3], 'data24': data[1][4],
                   'data31': data[2][1], 'data32': data[2][2], 'data33': data[2][3], 'data34': data[2][4],
                   'data41': data[3][1], 'data42': data[3][2], 'data43': data[3][3], 'data44': data[3][4],
                   'data51': data[4][1], 'data52': data[4][2], 'data53': data[4][3], 'data54': data[4][4],
                   'data61': data[5][1], 'data62': data[5][2], 'data63': data[5][3], 'data64': data[5][4],
                   'data71': data[6][1], 'data72': data[6][2], 'data73': data[6][3], 'data74': data[6][4],
                   'data81': data[7][1], 'data82': data[7][2], 'data83': data[7][3], 'data84': data[7][4],
                   'data91': data[8][1], 'data92': data[8][2], 'data93': data[8][3], 'data94': data[8][4]})

def data_anomaly_analysis(request):
    data = get_timestamp()
    #______
    if request.POST.get('btn31','') == 'renovate':
        print(request.POST.get('btn31',''))
        data=get_timestamp()
        return render(request, 'data-anomaly-analysis.html',{"data":data})

    if request.POST.get('btn32', '') == 'order':
        data=get_data_from_abnormal()
        image = data[0]
        data1 = []
        data2 = []
        for i in data[1]:
            data1.append(i[0] + i[2])
            if data2==[]:
                data2.append(i[1].split(",") )
        base64_code = get_base64_from_sql(int(image))
        im_name=str(image)+'.jpg'
        a = get_img_from_base64(im_name, base64_code)
        return render(request, 'data-anomaly-analysis.html', {"data1": data1, "data2": data2[0], "images": a})
        # _______________
    return render(request, 'data-anomaly-analysis.html', {"data1": data})
def etiological_analysis(request):
    if request.POST.get('order', '') !='':
        print('tvybunim')
        tmeplate = loader.get_template('../templates/etiological-analysis.html')
        sick_kind=request.POST.get('department', '')
        sick_time=request.POST.get('major', '')
        sick_day=request.POST.get('splittime', '')
        print(sick_kind,sick_time,sick_day)
        # sick_long=int(sick_day)*86400
        # min_day=int(sick_time)-int(sick_long)
        # max_day=int(sick_time)+int(sick_long)
        print('successfully fetch time')
        day=0
        kind=0
        dat=''
        if int(sick_kind) ==0:
            day=1536151682
        if int(sick_kind) ==1:
            day=1536306261
        if int(sick_kind) ==2:
            day=1536399388
        if int(sick_kind) <= 5:
            day=1536648116
        if int(sick_day) == 0:
            kind=5
        if int(sick_day) == 1:
            kind=12
        if int(sick_day) == 2:
            kind=20
        if int(sick_time) == 0:
            dat='11'
        if int(sick_time) == 1:
            dat='12'
        if int(sick_time) == 2:
            dat='13'
        min_day=day-kind
        max_day=day+kind
        print(min_day,max_day,dat,kind)
        ln = data_line0(find_record(min_day, max_day,dat))
        grid = Grid()
        grid.add(ln, grid_left='10%', grid_width=400, grid_height=200)
        page = Page()
        page.add(grid)
        content_2 = dict(
            pageecharts=page.render_embed(),
            host=REMOTE_HOST,
            script_list=page.get_js_dependencies()
        )
        return HttpResponse(tmeplate.render(content_2, request))
        #return render(request, 'etiological-analysis.html')
    return render(request, 'etiological-analysis.html')

def abnormal(request):
    return render(request,'abnormal.html')
