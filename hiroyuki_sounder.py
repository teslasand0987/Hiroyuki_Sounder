import sys
# -*- coding:utf-8 -*-
import tkinter
from tkinter import StringVar, ttk

import pyaudio
import wave

audio = pyaudio.PyAudio()

empty_namelist = []
empty_namelist2 = []
num = 0

for i in range(audio.get_device_count()):
    dev = audio.get_device_info_by_index(i)
    #print(dev['name'], end=':')
    #print(dev['hostApi'], end=':')
    #print(dev['index'])
    
    if dev['hostApi'] == 0:
        empty_namelist.append(dev['name'])
        
        if dev['maxOutputChannels'] > 0:
            empty_namelist2.append(dev['name'])

#音声再生やボリューム調整用関数
#=================================================================================================
def sound_play():
    #val = float(s.get() / 100)
    sound_file = "SE/wav/your_impression_right.wav"

    if sound_var == 0:
        sound_file = "SE/wav/your_impression_right.wav"
    elif sound_var == 1:
        sound_file = "SE/wav/can_you_stop_lying.wav"
    elif sound_var == 2:
        sound_file = "SE/wav/need_detect_a_liar.wav"
    elif sound_var == 3:
        sound_file = "SE/wav/intelligence_problem.wav"
    elif sound_var == 4:
        sound_file = "SE/wav/do_you_have_data.wav"
    elif sound_var == 5:
        sound_file = "SE/wav/heee_hiroyuki_01.wav"
    elif sound_var == 6:
        sound_file = "SE/wav/this_question_is_correct.wav"
    elif sound_var == 7:
        sound_file = "SE/wav/never_give_up_your_life.wav"
    elif sound_var == 8:
        sound_file = "SE/wav/hiroyuki_felt_uncomfortable.wav"
    elif sound_var == 9:
        sound_file = "SE/wav/sorry_hiroyuki_01.wav"
    elif sound_var == 10:
        sound_file = "SE/wav/seikatuhogo_oisii_hiroyuki.wav"
    elif sound_var == 11:
        sound_file = "SE/wav/hiroyuki_think_you_are_so_fool_01.wav"
    elif sound_var == 12:
        sound_file = "SE/wav/shazou.wav"
    elif sound_var == 13:
        sound_file = "SE/wav/cannot_be_blamed.wav"
    elif sound_var == 14:
        sound_file = "SE/wav/subetteru_hiroyuki_02.wav"

    CHUNK_SIZE = 1024

    wf = wave.open(sound_file, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=2,
                output_device_index=device_num,#13:FX,8:機器(ヘッドセット)
                rate=wf.getframerate(),
                input=False,
                output=True)

    data = wf.readframes(CHUNK_SIZE)
 
    # Streamに読み取ったデータを書き込む＝再生する
    while len(data) > 0:
        # Streamに書き込む
        stream.write(data)
    
        # 再度チャンクサイズだけ読み込む。これを繰り返す
        data = wf.readframes(CHUNK_SIZE)
    
    # Streamを止めて、closeする。closeしなければ、start_stream()で再開できる
    stream.stop_stream()
    stream.close()
    # PyAudioインスタンスを破棄する
    p.terminate()




#画面描画とその処理関数
#=================================================================================================
# メインウィンドウ
root = tkinter.Tk()
root.title(u"ひろゆきサウンダー")
root.iconbitmap('images/hiroyuki.ico')
root.geometry("550x300")
# ================================================================================================
frame1 = tkinter.Frame(root)

#ラベル1の作成
label_1 = tkinter.Label(frame1, text='OutputMonitor').grid(row=0, column=0, pady=10)

#コンボボックスの作成と配置
v = StringVar()
pulldown_list = empty_namelist2
combobox = ttk.Combobox(frame1, width=50, values=pulldown_list,textvariable=v, state="readonly")

device_num = 8
def select_device(self):
    global device_num
    global v
    name = v.get()

    for i in range(len(empty_namelist)):
        if name == empty_namelist[i]:
            device_num = i
            break
    

combobox.set(pulldown_list[0])
combobox.bind('<<ComboboxSelected>>', select_device)
combobox.grid(row=0, column=1)

frame1.pack()

frame3 = tkinter.LabelFrame(root,text="ひろゆきボイス",foreground="blue")
f0 = tkinter.Frame(frame3)
f1 = tkinter.Frame(frame3)
f2 = tkinter.Frame(frame3)
f3 = tkinter.Frame(frame3)
f4 = tkinter.Frame(frame3)

#音種類値
sound_var = 0

#値設定と音再生用関数
def clicked1():
    global sound_var
    sound_var = 0
    sound_play()

def clicked2():
    global sound_var
    sound_var = 1
    sound_play()

def clicked3():
    global sound_var
    sound_var = 2
    sound_play()

def clicked4():
    global sound_var
    sound_var = 3
    sound_play()

def clicked5():
    global sound_var
    sound_var = 4
    sound_play()

def clicked6():
    global sound_var
    sound_var = 5
    sound_play()

def clicked7():
    global sound_var
    sound_var = 6
    sound_play()

def clicked8():
    global sound_var
    sound_var = 7
    sound_play()

def clicked9():
    global sound_var
    sound_var = 8
    sound_play()

def clicked10():
    global sound_var
    sound_var = 9
    sound_play()

def clicked11():
    global sound_var
    sound_var = 10
    sound_play()

def clicked12():
    global sound_var
    sound_var = 11
    sound_play()

def clicked13():
    global sound_var
    sound_var = 12
    sound_play()

def clicked14():
    global sound_var
    sound_var = 13
    sound_play()

def clicked15():
    global sound_var
    sound_var = 14
    sound_play()

b1 = tkinter.Button(f0,text="それは明らかにあなたの感想ですよね？",command=clicked1)
b1.pack(fill = 'x', padx=10, side = 'left')

b2 = tkinter.Button(f0,text="嘘つくのやめてもらっていいすか？",command=clicked2)
b2.pack(fill = 'x', padx=10, side = 'left')

b3 = tkinter.Button(f0,text="嘘は嘘であると見抜ける・・・",command=clicked3)
b3.pack(fill = 'x', padx=10, side = 'left')

b4 = tkinter.Button(f1,text="それはそういう風にしか理解ができない・・・",command=clicked4)
b4.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b5 = tkinter.Button(f1,text="なんかそういうデータとかあるんすか？",command=clicked5)
b5.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b6 = tkinter.Button(f1,text="へ～",command=clicked6)
b6.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b7 = tkinter.Button(f2,text="この疑問は正しいのよ",command=clicked7)
b7.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b8 = tkinter.Button(f2,text="人生諦めるな頑張れ(棒)",command=clicked8)
b8.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b9 = tkinter.Button(f2,text="それのニュースを聞いたときに・・・",command=clicked9)
b9.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b10 = tkinter.Button(f3,text="はい、すいません",command=clicked10)
b10.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b11 = tkinter.Button(f3,text="生活保護はおいしいですよ",command=clicked11)
b11.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b12 = tkinter.Button(f3,text="バカだと思います！",command=clicked12)
b12.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b10 = tkinter.Button(f4,text="写像？何すか写像って",command=clicked13)
b10.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b11 = tkinter.Button(f4,text="僕、他人は責められないっすよ",command=clicked14)
b11.pack(fill = 'x', padx=10, pady=10,  side = 'left')

b12 = tkinter.Button(f4,text="いや、滑ってるよね？",command=clicked15)
b12.pack(fill = 'x', padx=10, pady=10,  side = 'left')

f0.pack()
f1.pack()
f2.pack()
f3.pack()
f4.pack()
frame3.pack()
# ================================================================================================
# アプリの待機
root.mainloop()