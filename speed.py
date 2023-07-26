'''
    program: Internet speed checker
    author : akr
    GitHub : a-k-r-a-k-r

'''
import tkinter
import speedtest

root=tkinter.Tk()
root.title("Internet Speed Checker")

st=speedtest.Speedtest()
def get_download_speed():
    dw_sp=st.download()
    print(dw_sp)
    red_slider.set(dw_sp)

output_frame=tkinter.Frame(root)
input_frame=tkinter.Frame(root)
output_frame.pack()
input_frame.pack()

red_slider = tkinter.Scale(input_frame, from_=255, to=0)
red_slider.pack()
bton=tkinter.Button(input_frame,text="check",command=get_download_speed)
bton.pack()
root.mainloop()

'''

st = speedtest.Speedtest()
option=int(input("choose 123"))
if option==1:
    print(st.download())
elif option==2:
    print(st.upload())
elif option==3:
    servernames=[]
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("incorect chice")



def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]


def main():
    for i in range(3):
        print("making test #{}".format(i+1))
        d, u, p = test()
        print(f"Test {i+1}")
        print(f"Download {d}")
        print(f"Upload {u}")
        print(f"Ping {p}")


if __name__ == "__main__":
    main()'''