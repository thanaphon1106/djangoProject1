from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("<H1> Hello Word <br> This is my Word wide web </H1>")

def home(request):
    return render(request, 'home.html')

def personalRecord(request):
    return render(request, 'personalRecord.html')

def educationalRecord(request):
    return render(request, 'educationalRecord.html')

def interests(request):
    return render(request, 'interests.html')

def dreamJob(request):
    return render(request, 'dreamJob.html')

def roleModel(request):
    return render(request, 'roleModel.html')


def showMydata(request):
    id ="65342310063-0"
    name = "Thanaphon"
    add = "Khonkan"
    gender = "Male"
    work = "student"
    weight = 65
    height = 185
    color = "black"
    food = "กระเพราหมูกรอบ"
    productlist = [["PEAK Cosmic รุ่น EW01161A", "2699", "images/s1.png"],
                   ["Nike Air Jordan XXXV Low PF", "5800", "images/s2.png"],
                   ["UA Embiid 1 CNY", "4490", "images/s3.png"],
                   ["LeBron Witness 6","2,880","images/s4.png"],
                   ["PEAK Lightning Lou Williams Crazy6", "1,625", "images/s5.png"],
                   ["Jordan One Take II PF", "3,600", "images/s6.png"],
                   ["Harden Stepback Avatar", "21,920", "images/s7.png"],
                   ["D.O.N. Issue 2 GCA", "2,000", "images/8.png"],
                   ["LeBron Witness 6","2,880","images/s4.png"],
                   ["PEAK Cosmic รุ่น EW01161A", "2699", "images/s1.png"]
                   ]
    context = {'name':name,'id':id,'add':add,'gender':gender,'work':work,'weight':weight,
               'height':height,'color':color,'food':food,'productlist':productlist}
    return render(request,'showMydata.html',context)
