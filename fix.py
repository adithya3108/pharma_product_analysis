import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv
import time
selected_file_path = None# Global variable to store the file path
choice2=None
def choose_file():
    global selected_file_path
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename()
    selected_file_path = file_path
    #print(selected_file_path)

def submit(root):
    pass
    
def exit_app(root):
    root.destroy()

def choice():
    global choice2
    options2 = ["List of sales of product", "PIE-CHART OF THE PRODUCT", "List of sales of pharmacy"]
    choice2 = -1

    def set_choice(event):
        choice2 = combo.get()
        for i in range(0, 3):
            if choice2 == options2[i]:
                choice2 = i
                break
        stockist_activity(selected_file_path, choice2)
        #print(selected_file_path, choice2)
        
    root = tk.Tk()
    root.title("Choose an Option")
    root.geometry("800x400")  # Set the window size

    root.configure(bg="lightblue")
    style = ttk.Style(root)
    style.configure("TButton", font=("Arial", 18), foreground="black", background="lightblue")
    style.configure("TLabel", font=("Arial", 20), foreground="black", background="lightblue")
    style.configure("TCombobox", font=("Arial", 18), foreground="black", background="white")

    top_frame = tk.Frame(root, bg="lightblue")
    top_frame.pack(pady=20)

    file_label = tk.Label(top_frame, text="Click the button to select a file:")
    file_label.pack(side="left")

    open_button = tk.Button(top_frame, text="Open File Dialog", command=choose_file)
    open_button.pack(side="left")

    middle_frame = tk.Frame(root, bg="lightblue")
    middle_frame.pack(pady=10)

    service_label = tk.Label(middle_frame, text="Select an option:")
    service_label.pack(side="left")

    combo = ttk.Combobox(middle_frame, values=options2)
    combo.set("Choose an option")
    combo.bind("<<ComboboxSelected>>", set_choice)
    combo.pack(side="left")

    bottom_frame = tk.Frame(root, bg="lightblue")
    bottom_frame.pack(pady=20)
    
    submit_button = tk.Button(bottom_frame, text="Submit", command=lambda: submit(root))
    submit_button.pack(side="left", padx=20)

    exit_button = tk.Button(bottom_frame, text="Exit", command=lambda: exit_app(root))
    exit_button.pack(side="left", padx=20)

    root.protocol("WM_DELETE_WINDOW", lambda: exit_app(root))
    root.mainloop()

   

    return choice2


def stockist_activity(file_path, choice2):
    if not file_path:
        print("No file selected.")
        return

    if choice2 == -1:
        return

    with open(file_path, 'rt') as file:
         
        if file_path.endswith('MUTHU.csv'):
            # Your MUTHU specific code here
            c=csv.reader(file)
            k=0;e=0;m=[];d={};chemistval={};t=0;kl={}
            #['Customer', 'Product', 'Qty', 'Value', 'Area Name', 'Pin']
            for i in c: # creating a  nested list with essential items 
                y=[]
                k=k+1
                if k>6:
                    y=[i[2],i[4],i[9],i[12],i[16],i[17]]
                    m=m+[y]
                    if t>0:
                        if i[2] not in chemistval:
                            chemistval[i[2]]=float(i[12])
                        else:
                            chemistval[i[2]]=chemistval[i[2]]+float(i[12])
                    t=t+1
            for i in m[::]:
                if i[1] not in kl:
                    kl[i[1]]=float(i[3])
                else:
                    kl[i[1]]=kl[i[1]]+float(i[3])
            b=list(kl.items())
            def pie_chart_muthu():
                import time
                start=time.time()
                nonlocal kl
                pkl={}
                for i in kl.items():
                    if i[-1]>0:
                        pkl[i[0]]=i[1]
                import matplotlib.pyplot as plt
                import time
                start=time.time()
                # defining labels
                activities = list(pkl.keys())
                # portion covered by each label
                slices=list(pkl.values())
     
                # color for each label
        # plotting the pie chart
                plt.pie(slices[:-1], labels = activities[:-1],startangle=90, shadow = True, radius = 2, autopct = '%1.1f%%')
        # plotting legend
                plt.legend(title="LEGEND-NAME OF THE TABLETS")
        # showing the plot
                end=time.time();print(end-start)
                #print(end-start)
                plt.show()
                

            def product_writer_muthu():
                start=time.time()
                nonlocal b
                f=open('product_muthu.csv',"w",newline="")
                fe=csv.writer(f)
                fe.writerow(["muthu".upper()])
                for i in b:
                    c=[i[0],i[1]]
                    fe.writerow(i)
                f.close()
                end=time.time()
                #print(end-start)
            def pharmacy_file_muthu():
                start=time.time()
                nonlocal chemistval
                t=list(chemistval.items())
                f=open('chemist_muthu.csv', "w",newline="")
                fw=csv.writer(f)
                fw.writerow(["muthu".upper()])
                for i in t:
                    c=[i[0],i[1]]
                    fw.writerow(c)
                f.close()
                end=time.time()
                #print(end-start)
            
            if choice2==0:product_writer_muthu();print("given task has been performed")
            elif choice2==1:pie_chart_muthu()
            else:pharmacy_file_muthu();print("given task has been performed".upper())
        elif file_path.endswith('BALAJIGU.csv'):
            # Your BALAJIGU specific code here
            a=csv.reader(file)
            d={};k=0;g=4;chem_list=[];chemval=[];chemvaldict={}
            for i in a :
                if i[0]=="Product Name." or k>1:
                #print(i[5])
                    k=9
                    if i[5]!='' and i[0]!='' and g>5:
                        if i[0] not in d:
                            d[i[0]]=float(i[5])
                        else:
                            d[i[0]]=d[i[0]]+float(i[5])
                    if i[0]!="" and i[1]=="":
                        chem_list=chem_list+[i[0]]
                    if i[0]=="" and i[1]=="" and i[5]!="":
                        chemval=chemval+[float(i[5])]
                    g=6
            for i in range(len(chemval)):
                chemvaldict[chem_list[i]]=chemval[i]
                
            def pie_chart_balajigu():
                import time
                start=time.time()
                nonlocal d;pkl={}
                for i in d.items():
                    if i[-1]>0:
                        pkl[i[0]]=i[1]
                import matplotlib.pyplot as plt
                # defining labels
                activities = list(pkl.keys())
                # portion covered by each label
                slices=list(pkl.values())
        # plotting the pie chart
                plt.pie(slices[:-1], labels = activities[:-1],startangle=90, shadow = True, radius = 1.5, autopct = '%1.1f%%')
                # plotting legend
                plt.legend(title="LEGEND-NAME OF THE TABLETS")
                # showing the plot
                end=time.time()#for checking time
                
                plt.show()

            def pharmawriter():
                import time
                start=time.time()
                nonlocal chemvaldict
                f=open('chemist_balajigu.csv', "w",newline="")
                fw=csv.writer(f)
                for i in chemvaldict.items():
                    fw.writerow([i[0],i[1]])
                f.close()
                
            def product_writer():
                import time
                start=time.time()
                nonlocal d
                m=list(d.items())
                f=open('product_balajigu.csv', "w",newline="")
                fw=csv.writer(f)
                for i in chemvaldict.items():
                    fw.writerow([i[0],i[1]])
                f.close()
                end=time.time()
                print(end-start)
            if choice2==0:product_writer();print("the product have been sorted and the result is written in excel ")
            elif choice2==1:pie_chart_balajigu()
            else:pharmawriter();print("the chemist have been sorted and the result is written in excel ")
        elif file_path.endswith('BHOMIA.csv'):
            c=csv.reader(file);k=0;m=[];u=0;chemist=[];value=[]
            for i in c:
                if k>1 and 'DEEKAY LIFE SCIENCE  (148)' not in i:#list with q,val,name,pincode
                    m=m+[[i[3],i[7],i[8+1],i[-2]]]
                    u=u+1
                    if i[7]!="" and i[9]!="":
                        chemist=chemist+[i[9]]
                        value=value+[i[7]]
            
                k=k+1    
            d={};c=0
            for i in m[1:-1:] :#creating dictionary
                if i[0]=='' and i[1]=='' and i[-1]=='':
                    s=i[2]
                if i[2]=='' and i[3]==''and i[2] not in d :
                    d[s]=(float(i[0]),float(i[1]))
            for i in d.items():
                c=c+i[1][1]
            c=list(d.items())# list of dictionary
            def innsort(sub_li,k): # bubble sort for the inner list  k being index of inner list 
                l = len(sub_li)
                for i in range(0, l):
                    for j in range(0, l-i-1):
                        if (sub_li[j][1][k] > sub_li[j + 1][1][k]):
                            tempo = sub_li[j]
                            sub_li[j]= sub_li[j + 1]
                            sub_li[j + 1]= tempo
                return sub_li
            m=innsort(c,1)
            pdl={}
            for i in m:
                pdl[i[0]]=i[-1][-1]
            
            def pie_chart_bhomia():
                 import time
                 start=time.time()
                
                 nonlocal pdl
                 pkl={}
                 for i in pdl.items():
                     if i[-1]>0:
                         pkl[i[0]]=i[1]
                 import matplotlib.pyplot as plt
                # defining labels
                 activities = list(pkl.keys())
                # portion covered by each label
                 slices=list(pkl.values())
     
                # color for each label
        # plotting the pie chart
                 plt.pie(slices[:-1], labels = activities[:-1],startangle=90, shadow = True, radius = 2, autopct = '%1.1f%%')
        # plotting legend
                 plt.legend(title="LEGEND-NAME OF THE TABLETS")
                 end=time.time()
                 print(end-start)
        # showi ng the plot
                 plt.show()
            def pharmacysales():
                chemval={};nonlocal chemist ,value
                lenght=len(chemist)
                i=1
                while i!=lenght:
                    if chemist[i] not in chemval:
                        chemval[chemist[i]]=float(value[i])
                    else:
                        chemval[chemist[i]]=chemval[chemist[i]]+float(value[i])
                    i=i+1
                return chemval# dictionary containg chemist sales record
            def pharmacy_writer_bhomia():
                l=pharmacysales()
                t=list(l.items())
                f=open('chemist_record_of_bhomia.csv', "w",newline="")
                fw=csv.writer(f) 
                for i in t:
                    c=[i[0],i[1]]
                    fw.writerow(c)
                f.close()
            def product_writer_bhomia():
                nonlocal m
                f=open('product_record_of_bhomia.csv',"w",newline="")
                fe=csv.writer(f)
                for i in m:
                    c=[i[0],i[1][1]]
                    fe.writerow(c)
                f.close()
            if choice2==0:product_writer_bhomia();print("the product sales have been calculated  and the result is written in excel ")
            elif choice2==1:pie_chart_bhomia()
            else:pharmacy_writer_bhomia();print("the chemist sales have been calculated  and the result is written in excel ")

        elif file_path.endswith('MEENAKSHI.csv'):
            
            c=csv.reader(file);m=[];k=e=0;chemist=[];value=[];
            for i in c:
                #print(i[0],i[1],i[3],i[4],i[7])
                if i ==['Bill Date', 'Customer Name', 'Place', 'Pin', 'Qty', 'Free', 'Net Amount', 'Goods Value', 'Area Name'] or k>7:
                    m=m+[[i[0],i[1],i[3],i[4],i[7]]]
                k=k+1
            for i in m[1::]:
                if i[1]!="" or i[-1]!="":
                    chemist=chemist+[i[1]]
                    value=value+[float(i[-1])]
            d={}
            for i in m[1:-2]:
                if i[1]=="" or i[2]=="" or i[3]=="" or i[4]=="":
                    s=i[0]
                    d[s]=[0,0]
                else:
                    c=d[s]
                    c[0]=c[0]+float(i[3])
                    c[1]=c[1]+float(i[4])
                    d[s]=c
            pdl={}
            o=list(d.items())
            #print(o)
            kl={}
            for i in o:
                if i!="":
                    pdl[i[0]]=i[-1][-1]
            def pie_chart_meenakshi():
                 import time
                 start=time.time()
                 nonlocal pdl
                 pkl={}
                 for i in pdl.items():
                     if i[-1]>0:
                         pkl[i[0]]=i[1]
                 import matplotlib.pyplot as plt
                # defining labels
                 activities = list(pkl.keys())
                # portion covered by each label
                 slices=list(pkl.values())
     
                # color for each label
        # plotting the pie chart
                 plt.pie(slices[:-1], labels = activities[:-1],startangle=90, shadow = True, radius = 2, autopct = '%1.1f%%')
        # plotting legend
                 plt.legend(title="LEGEND-NAME OF THE TABLETS")
                 end=time.time()
                 print(end-start)
        # showi ng the plot
                 plt.show()

            def product_writer_meenakshi():
                nonlocal  pdl
                ds=list(pdl.items())
                ds=ds[0:1]+ds[2:]
                f=open('product_meenakshi.csv',"a",newline="")
                fe=csv.writer(f)
                fe.writerow(["meenakshi".upper()])
                for i in ds:
                    c=[i[0],i[1]]
                    fe.writerow(c)
                f.close()
            
            def pharmacyranked():
                chemval={};nonlocal chemist ,value
                lenght=len(chemist)
                i=1
                while i!=lenght:
                    if chemist[i] not in chemval:
                        chemval[chemist[i]]=float(value[i])
                    else:
                        chemval[chemist[i]]=chemval[chemist[i]]+float(value[i])
                    i=i+1
                return chemval# dictionary containg chemist sales record
            def pharmacy_file_meenakshi():
                lt=pharmacyranked()
                t=list(lt.items())
                f=open('chemist_meenakshi.csv', "a",newline="")
                fw=csv.writer(f)
                fw.writerow(["meenakshi ".upper()])
                for i in t:
                    c=[i[0],i[1]]
                    fw.writerow(c)
                f.close()
            if choice2==0:product_writer_meenakshi();print("the product sales have been calculated  and the result is written in excel ")
            elif choice2==1:pie_chart_meenakshi();print("in here")
            else:pharmacy_file_meenakshi();print("the chemist sales have been calculated  and the result is written in excel ")
        elif file_path.endswith('PALANI.csv'):
             
            c=csv.reader(file);k=0;m=[];e=0;chemist=[];value=[];
            for i in c:
                if k>1 and 'DEEKAY LIFE SCIENCE  (148)' not in i:#list with q,val,name,pincode
                    m=m+[[i[3],i[7],i[8+1],i[-2]]]
                    e=e+1
                if i[7]!="" and i[9]!="":
                    chemist=chemist+[i[9]]
                    value=value+[i[7]]
                k=k+1
            d={};c=0
            for i in m[1:-1:]:#creating dictionary
                if i[0]=='' and i[1]=='' and i[-1]=='':
                    s=i[2]
                if i[2]=='' and i[3]==''and i[2] not in d :
                    d[s]=(float(i[0]),float(i[1]))
            for i in d.items():
               # print(i)
                c=c+i[1][1]
            c=list(d.items())
            #print(d,end="\n\n")
            def innsort(sub_li,k): # bubble sort for the inner list  k being index of inner list 
                l = len(sub_li)
                for i in range(0, l):
                    for j in range(0, l-i-1):
                        if (sub_li[j][1][k] > sub_li[j + 1][1][k]):
                            tempo = sub_li[j]
                            sub_li[j]= sub_li[j + 1]
                            sub_li[j + 1]= tempo
                return sub_li
            m=innsort(c,1)#value sorted
            
            pdl={}
            for i in m:
                pdl[i[0]]=i[-1][-1]
            
            def pie_chart_palani():
                 import time
                 start=time.time()
                 nonlocal pdl
                 pkl={}
                 for i in pdl.items():
                     if i[-1]>0:
                         pkl[i[0]]=i[1]
                 import matplotlib.pyplot as plt
                # defining labels
                 activities = list(pkl.keys())
                # portion covered by each label
                 slices=list(pkl.values())
        # plotting the pie chart
                 plt.pie(slices[:-1], labels = activities[:-1],startangle=90, shadow = True, radius = 2, autopct = '%1.1f%%')
        # plotting legend
                 plt.legend(title="LEGEND-NAME OF THE TABLETS")
                 end=time.time();
                 print(end-start)
        # showi ng the plot
                 plt.show()
            def product_writer_palani():
                nonlocal  m 
                f=open('product_of_palani.csv',"w",newline="")
                fe=csv.writer(f)
                for i in m:
                    c=[i[0],i[1][1]]
                    fe.writerow(c)
                f.close()
            def pharmacyranked():
                chemval={};nonlocal chemist ,value
                lenght=len(chemist)
                i=1
                while i!=lenght:
                    if chemist[i] not in chemval:
                        chemval[chemist[i]]=float(value[i])
                    else:
                        chemval[chemist[i]]=chemval[chemist[i]]+float(value[i])
                    i=i+1
                return chemval# dictionary containg chemist sales record
            def pharmacy_file_palani():
                l=pharmacyranked()
                t=list(l.items())
                f=open('chemist_of_palani.csv', "w",newline="")
                fw=csv.writer(f)
                for i in t:
                    c=[i[0],i[1]]
                    fw.writerow(c)
                f.close()
            if choice2==0:product_writer_palani();print("the product sales have been calculated  and the result is written in excel ")
            elif choice2==1:pie_chart_palani()
            else:pharmacy_file_palani();print("the chemist sales have been calculated  and the result is written in excel ")
        elif file_path.endswith('RSPHARMA.csv'):
            c=csv.reader(file);k=0;m=[];e=0;chemist=[];value=[];
            for i in c:
                if k>1 and 'DEEKAY LIFE SCIENCE  (148)' not in i:#list with q,val,name,pincode
                    m=m+[[i[3],i[7],i[8+1],i[-2]]]
                    e=e+1
                if i[7]!="" and i[9]!="":
                    chemist=chemist+[i[9]]
                    value=value+[i[7]]
                k=k+1
            d={};c=0
            for i in m[1:-1:] :#creating dictionary
                if i[0]=='' and i[1]=='' and i[-1]=='':
                    s=i[2]
                if i[2]=='' and i[3]==''and i[2] not in d :
                    d[s]=(float(i[0]),float(i[1]))
            for i in d.items():
                c=c+i[1][1]
            c=list(d.items())# list of dictionary
            def innsort(sub_li,k): # bubble sort for the inner list  k being index of inner list 
                l = len(sub_li)
                for i in range(0, l):
                    for j in range(0, l-i-1):
                        if (sub_li[j][1][k] > sub_li[j + 1][1][k]):
                            tempo = sub_li[j]
                            sub_li[j]= sub_li[j + 1]
                            sub_li[j + 1]= tempo
                return sub_li
            m=innsort(c,1)#value sorted
            pdl={}
            for i in m:
                pdl[i[0]]=i[-1][-1]
            
            def pie_chart_rspharma():
                 import time
                 start=time.time()
                 nonlocal pdl
                 pkl={}
                 for i in pdl.items():
                     if i[-1]>0:
                         pkl[i[0]]=i[1]
                 import matplotlib.pyplot as plt
                # defining labels
                 activities = list(pkl.keys())
                # portion covered by each label
                 slices=list(pkl.values())
     
                # color for each label
        # plotting the pie chart
                 plt.pie(slices[:-1], labels = activities[:-1],startangle=90, shadow = True, radius = 2, autopct = '%1.1f%%')
        # plotting legend
                 plt.legend(title="LEGEND-NAME OF THE TABLETS")
                 end=time.time()
                 print(end-start)
        # showi ng the plot
                 plt.show()
            def product_writer_rspharma():
                nonlocal  m 
                f=open('product_of_RSPHARMA.csv',"w",newline="")
                fe=csv.writer(f)
                for i in m:
                    c=[i[0],i[1][1]]
                    fe.writerow(c)
                f.close()
            def pharmacyranked():
                chemval={};nonlocal chemist ,value
                lenght=len(chemist)
                i=1
                while i!=lenght:
                    if chemist[i] not in chemval:
                        chemval[chemist[i]]=float(value[i])
                    else:
                        chemval[chemist[i]]=chemval[chemist[i]]+float(value[i])
                    i=i+1
                return chemval# dictionary containg chemist sales record
            def pharmacy_file_rspharma():
                l=pharmacyranked()
                t=list(l.items())
                f=open('chemist_of_RSPHARMA.csv', "w",newline="")
                fw=csv.writer(f)
                for i in t:
                    c=[i[0],i[1]]
                    fw.writerow(c)
                f.close()
            if choice2==0:
                product_writer_rspharma();print("the product sales have been calculated  and the result is written in excel ")
            elif choice2==1:
                pie_chart_rspharma()
            else:pharmacy_file_rspharma();print("the chemist sales have been calculated  and the result is written in excel ")
            choice()

if __name__ == "__main__":
    #file_path = choose_file()
   # if not file_path:
        #print("No file selected.")
    
        choice()
        '''
        if choice2 == -1:
            print("No option selected.")
        elif choice2 == "Exit":
            print("Exiting application.")
        else:
            print("leavinf main")
            print(selected_file_path,choice2)
            stockist_activity(selected_file_path, choice2)
        '''
        
            
            
