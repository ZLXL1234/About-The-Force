import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("File Opening Example")
root.geometry("500x300")

input_text = tk.StringVar()
output_text = tk.StringVar()
ffmpeg = tk.StringVar()

#输入文件
input_label = tk.Label(root, text="输入:")
input_label.place(x=10, y=10)
input_entry = tk.Entry(root)
input_entry.place(x=10, y=40, width=200, height=30)
#定义
def open_input_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)
        os.open(file_path, flags=os.O_RDONLY)
        input_text.set(input_entry.get())
#选择文件
select_button = tk.Button(root, text="选择", command=open_input_file)
select_button.place(x=220, y=40, width=60, height=30)

#输出文件
output_label = tk.Label(root, text="输出文件名:")
output_label.place(x=10, y=80)
output_entry = tk.Entry(root)
output_entry.place(x=10, y=110, width=200, height=30)

#码率
bit_label = tk.Label(root, text="码率:")
bit_label.place(x=10, y=150)
bit_spinbox = tk.Spinbox(root, from_=500, to=20000, increment=500, width=10)
bit_spinbox.place(x=10, y=180, width=200, height=30)

#命令输出
def get_path():
    output_text.set(output_entry.get())
    input_text.set(input_entry.get())
    ffmpeg.set(bit_spinbox.get())
    out = "-i '{}' -c:a copy -c:v hevc_nvenc -r 30 -color_range 2 -rc-lookahead 55 -b:v {}k -preset 1 -tune 1 -profile:v 2 -tier 1 -rc 1 -spatial_aq 1 -temporal_aq 1 -multipass 2 -b_ref_mode 1 -threads 1 'F:\输出视频\\{}.mp4'".format(input_text.get(), ffmpeg.get(), output_text.get())
    print (out)

select_button = tk.Button(root, text="启动", command=get_path)
select_button.place(x=10, y=220, width=60, height=30)

#退出
button = tk.Button(root, text="退出", command=root.quit)
button.place(x=430, y=260, width=60, height=30)
root.mainloop()
