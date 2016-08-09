#-*- coding: utf-8 -*-
from tkinter import *
import pickle
window = Tk()
window.title("Database Students")

####################### UI 설계

## 이름,라벨
Label(window, text="이름: ").grid(row=0, column=0, sticky=W)
entry1 = Entry(window, width=20, bg="light green")
entry1.grid(row=0, column=1, sticky=W)
Label(window, text="점수: ").grid(row=0, column=2, sticky=E)
entry2 = Entry(window, width=7, bg="light green")
entry2.grid(row=0, column=3, sticky=W)
Label(window, text="번호: ").grid(row=1, column=2, sticky=E)
entry3 = Entry(window, width=5, bg="light green")
entry3.grid(row=1, column=3, sticky=W)
Label(window, text="파일이름: ").grid(row=2, column=2, sticky=E)
entry4 = Entry(window, width=20, bg="light blue")
entry4.grid(row=2, column=3, sticky=W)
Label(window, text="파일이름: ").grid(row=3, column=2, sticky=E)
entry5 = Entry(window, width=20, bg="light blue")
entry5.grid(row=3, column=3, sticky=W)

## 아래 버튼
num_pad = Frame(window)
num_pad.grid(row=4, column=1, columnspan=4, sticky=W)
                                                                                                                                                                                                                                                                                                                                    
## 데이터 출력창
output = Text(window, width=75, height=10, wrap=WORD, background="light yellow")
output.grid(row=5, column=0, columnspan=5, sticky=W)

## 상태 메시지 출력창
output2 = Text(window, width=75, height=1, wrap=WORD, background="light pink")
output2.grid(row=6, column=0, columnspan=5, sticky=W)

## 우측버튼
num_right_pad = Frame(window)
num_right_pad.grid(row=0, column=4, rowspan=4,sticky=W)
num_rightpad_list=['추가','삭제','저장','열기']
data = [] #이어붙일 데이터
dataNum = 1 #데이터 갯수

def storeScore(size, data):
    result = []
    for i in range(size):
        result.append([data[i][0], data[i][1], data[i][2]])
    return result

def sortNum(data):
    return data[0]
def sortName(data):
    return data[1]
def sortScore(data):
    return eval(data[2])

## 하단 키 기능
def click1(): # 번호순
    output2.delete("1.0",END)
    global data
    output2.delete("1.0",END)
    result = storeScore(dataNum-1, data)
    data = sorted(result, reverse=False, key=sortNum)
    output.delete("1.0",END)
    cnt=1
    for a in data:
        cnt += 1
    for b in range(0,cnt-1):
        enter_text = "%2d %10s %3f\n" %(data[b][0], data[b][1], eval(data[b][2]))
        output.insert(END, enter_text)
Button(num_pad, text = "번호순", width = 5, command=click1).grid(row = 0, column = 0)

def click2(): #이름순
    output2.delete("1.0",END)
    global data
    output2.delete("1.0",END)
    result = storeScore(dataNum-1, data)
    data = sorted(result, reverse=False, key=sortName)
    output.delete("1.0",END)
    cnt=1
    for a in data:
        cnt += 1
    for b in range(0,cnt-1):
        enter_text = "%2d %10s %3f\n" %(data[b][0], data[b][1], eval(data[b][2]))
        output.insert(END, enter_text)
Button(num_pad, text = "이름순", width = 5, command=click2).grid(row = 0, column = 1)

def click3(): #점수 내림차순
    global data
    output2.delete("1.0",END)
    result = storeScore(dataNum-1, data)
    data = sorted(result, reverse=True, key=sortScore)
    output.delete("1.0",END)
    cnt=1
    for a in data:
        cnt += 1
    for b in range(0,cnt-1):
        enter_text = "%2d %10s %3f\n" %(data[b][0], data[b][1], eval(data[b][2]))
        output.insert(END, enter_text)
Button(num_pad, text = "점수내림차순", width = 15, command=click3).grid(row = 0, column = 2)

def click4(): #점수 오름차순
    global data
    output2.delete("1.0",END)
    result = storeScore(dataNum-1, data)
    data = sorted(result, reverse=False, key=sortScore)
    output.delete("1.0",END)
    cnt=1
    for a in data:
        cnt += 1
    for b in range(0,cnt-1):
        enter_text = "%2d %10s %3f\n" %(data[b][0], data[b][1], eval(data[b][2]))
        output.insert(END, enter_text)
Button(num_pad, text = "점수오름차순", width = 15, command=click4).grid(row = 0, column = 3)
    
## 우측 키 기능
def click(key):
    global dataNum
    global data
    output2.delete("1.0",END)
    if key == '추가':
        if entry1.get() == "":
            output2.insert(END, "[이름 오류] 이름에 빈칸을 넣으면 안됩니다.")
        elif entry2.get() == "":
            output2.insert(END,"[점수입력 오류] 점수에 빈값을 넣으면 안됩니다.")
        else:
            try:
                if eval(entry2.get()):
                    checkName=0
                    for z in range(0,dataNum-1):
                        if entry1.get() == data[z][1]:
                            output2.insert(END, "[이름 중복 오류] 이름이 중복됩니다.")
                            checkName=1
                    if checkName==0:
                        max = 0
                        for i in range(0,dataNum-1):
                            if max < data[i][0]:
                                max = data[i][0]
                        data.append([max+1, entry1.get(), entry2.get()])
                        entered_text = "%2d %10s %3f\n" %(data[dataNum-1][0],data[dataNum-1][1], eval(data[dataNum-1][2]))
                        output.insert(END, entered_text)
                        dataNum += 1
                        output2.insert(END,"[입력 성공!]")
                        entry1.delete(0, END)
                        entry2.delete(0, END)
                        entry3.delete(0, END)
                        entry4.delete(0, END)
                        entry5.delete(0, END)
            except NameError:
                output2.insert(END,"[점수입력 오류] 점수에 숫자가 아닌값을 넣으면 안됩니다.")
            except ValueError:
                output2.insert(END,"[점수입력 오류] 점수는 0이상의 숫자만 들어갈 수 있습니다.")
            except SyntaxError:
                output2.insert(END,"[점수입력 오류] 점수에는 숫자만 넣으십시요!")
            except:
                output2.insert(END, "[점수입력 오류] 입력할 점수를 다시 한번 확인해 보세요")
                     
       

    elif key == '삭제':
        if entry3.get() == "":
            output2.insert(END, "[번호 삭제 오류] 삭제할 번호에 빈칸을 넣으면 안됩니다.")
        else:
            try:
                if eval(entry3.get()):
                    checkNum = 0
                    for j in range(0, dataNum-1):
                        if eval(entry3.get()) == data[j][0]:
                            checkNum = 1
                    if checkNum == 1:
                        output.delete("1.0",END)
                        newData = [] #새로운데이터 생성
                        check=0
                        for cnt in range(0,dataNum-1):
                            if data[cnt][0] == eval(entry3.get()):
                                #print("CHECK")
                                check=1
                            elif check==0:
                                #print("No ckeck")
                                newData.append(data[cnt])
                            else:
                                #print("Is CHECK")
                                newData.append(data[cnt])
                        dataNum -= 1
                        data=newData
                        for cnnt in range(0,dataNum-1):
                            entered_text = "%2d %10s %3f\n" %(data[cnnt][0], data[cnnt][1], eval(data[cnnt][2]))
                            output.insert(END, entered_text)
                        output2.insert(END, "[삭제성공]")
                    else:
                        output2.insert(END, "[번호 삭제 오류] 삭제할 번호가 없습니다")
            except NameError:
                output2.insert(END, "[번호 삭제 오류] 삭제할 번호에 숫자가 아닌 문자 등을 넣지 마십시요!!")
            except SyntaxError:
                output2.insert(END, "[번호 삭제 오류] 숫자가 아닌 이상한 기호를 넣지 마십시요!")
            except:
                output2.insert(END, "[번호 삭제 오류] 삭제할 번호를 다시 한번 확인해 보세요")
            
     
    elif key == '저장':
        if entry4.get() == "":
            output2.insert(END, "[파일 저장 오류] 저장할 이름을 입력하여 주세요. (공백불가)")
        else:
            f = open(entry4.get(),'wb')
            pickle.dump(data, f)
            output2.insert(END, "[저장 성공]")
            f.close
    elif key == '열기':
        if entry5.get() == "":
            output2.insert(END, "[파일 열기 오류] 불러올 파일을 입력하여 주세요. (공백불가)")
        else:
            try:
                output.delete("1.0",END)
                f=open(entry5.get(), 'rb')
                other = pickle.load(f)
                cnt = 1
                for a in other:
                    cnt += 1
                for b in range(0,cnt-1):
                    enter_text = "%2d %10s %3f\n" %(other[b][0], other[b][1], eval(other[b][2]))
                    output.insert(END, enter_text)
                data = other
                dataNum = cnt
                output2.insert(END, "[파일 열기 성공]")
            except FileNotFoundError:
                output2.insert(END, "[파일 열기 오류] 입력한 파일이름을 찾을 수 없습니다!!")
            except:
                output2.insert(END, "[파일 열기 오류] 불러올 파일 이름을 다시 확인해 보세요.")


## 우측 키        
r=0
for btn_text in num_rightpad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_right_pad, text=btn_text, width = 5, command=cmd).grid(row = r, column = 4)
    r += 1
