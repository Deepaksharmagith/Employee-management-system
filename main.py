import streamlit as st                   
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu
import datetime
st.set_page_config(layout="wide")
st.sidebar.header("EMPLOYEE MANAGEMENT SYSTEM")
st.sidebar.image("https://png.pngtree.com/png-clipart/20220726/original/pngtree-quarantine-office-people-employee-manager-png-image_8420225.png")
choice=st.sidebar.selectbox("MY MENU",("HOME","ADMIN LOGIN","EMPLOYEE LOGIN"))
if(choice=="HOME"):
    st.markdown("<center><h1>EMPLOYEE MANAGEMENT SYSTEM</h1></center>",unsafe_allow_html=True)
    st.markdown("<center><img src='https://mitrefinch.com/wp-content/uploads/2016/08/Employee-Management-Software-for-Small-Business.jpg'></center>",unsafe_allow_html=True)
    st.markdown("This is a database Management Application- **designed to manage the data of employee **.")
elif(choice=="EMPLOYEE LOGIN"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    eid=st.sidebar.text_input("Enter Employee ID")
    epass=st.sidebar.text_input("Enter Password")
    btn=st.sidebar.button('Login')
    btn2=st.sidebar.button("Logout")
    if btn2:
        st.session_state['login']=False
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='ems')
        c=mydb.cursor()
        c.execute("select * from emp_details")
        for r in c:
            if(r[0]==eid and r[1]==epass):
                st.session_state['login']=True
                break
        if(st.session_state['login']==False):
            st.error("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.success("Login Successful")
        if st.session_state['login']==btn:
            st.balloons()
        choice1=selected=option_menu(
            menu_title=None,
            options=["APPLY attendancen","target_achieved","check project status","Resignation_form"],
            icons=["person-plus-fill","upload","lightning","activity"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",)

#--------------------------------------------apply attandance-----------------------------------
      
        if choice1=="APPLY attendancen":
            eid=st.text_input("Enter the Employee ID")
            emp_name=st.text_input("Enter the Employee name")
            btn3=st.button("Enter")
            if btn3:
                DIO=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("insert into attendance values(%s,%s,%s)",(eid,emp_name,DIO))
                mydb.commit()
                st.success('Successfully!', icon="✅")

#--------------------------------------------------target_achieved--------------------------------
        elif choice1=="target_achieved":
            eid=st.text_input("Enter the Employee ID")
            target_achieved=st.text_input("Enter the target_achieved") 
            btn3=st.button("Enter")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("Update project  set target_achieved='target_achieved' where eid='eid'")
                mydb.commit()
                st.success("input taken")

#--------------------------------------check progress review-----------------------------
        elif(choice1=="check project status"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='ems')
            c=mydb.cursor()
            c.execute("select * from project ")
            l=[]
            for r in c:
                l.append(r)       
            df=pd.DataFrame(data=l,columns=['eid','project_name','project_assigned','Deadline','target_achieved','progress review'])
            st.dataframe(df)

#-----------------------------------------------Resignation_form----------------------------------------------
        elif choice1=="Resignation_form":
            eid=st.text_input("Enter the Employee ID")
            e_name=st.text_input("Enter the Employee name")
            reasion=st.text_input("What is/are the main reason(s) you’re leaving this position?")
            cc=st.text_input("How would you describe our company culture?")
            aspect=st.text_input("What were your favorite and least favorite aspects of your job?")
            rm=st.text_input("How much would you rate your manager out of 5?")
            btn3=st.button("Fill the form")
            if btn3:
                Dio=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("insert into Resignation_form values(%s,%s,%s,%s,%s,%s,%s)",(Dio,eid,e_name,reasion,cc,aspect,rm))
                mydb.commit()
                st.success('Successfully!', icon="✅")            


        
#----------------------------------------------------------------------------------------------------------------------
elif(choice=="ADMIN LOGIN"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    aid=st.sidebar.text_input("Enter Admin ID")
    apass=st.sidebar.text_input("Enter Password")
    btn=st.sidebar.button('Login')
    btn2=st.sidebar.button("Logout")
    if btn2:
        st.session_state['login']=False
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='ems')
        c=mydb.cursor()
        c.execute("select * from admin_details")
        for r in c:
            if(r[0]==aid and r[1]==apass):
                st.session_state['login']=True
                break
        if(st.session_state['login']==False):
            st.error("Incorrect ID or Password")
    if(st.session_state['login']==True):
        st.success("Login Successful")
        if st.session_state['login']==btn:
            st.balloons()
#-------------------------------------------------------------------------------------------------------
        choice1=selected=option_menu(
            menu_title=None,
            options=["Add Employee","Remove Employee","Update details","Active Employee","assign project","update progress","check project status","check attendance"],
            icons=["person-plus-fill","trash","lightning","activity","upload","lightning"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",)

#--------------------------------------------------add employ--------------------------------
        if choice1=="Add Employee":
            emp_id=st.text_input("Enter the Employee ID")
            emp_pass=st.text_input("Enter the Passward")
            emp_name=st.text_input("Enter the Employee name")
            phone_no=st.text_input("Enter the phone number")
            gender=st.text_input("Enter the Gender")
            address=st.text_input("Enter the address")
            Doj=st.text_input("Enter the Date of join")
            designation=st.text_input("Enter the designation")
            dept=st.text_input("Enter the department")
            salary=st.text_input("Enter the Salary")
            btn3=st.button("Enter")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("insert into emp_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(emp_id,emp_pass,emp_name,phone_no,gender,address,Doj,designation,dept,salary))
                mydb.commit()
                st.success("input taken")

#--------------------------------------------------update emd details--------------------------------
        if choice1=="Update details":
            emp_id=st.text_input("Enter the Employee ID")
            btn5=st.button("Enter")
            if btn5:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("select * from emp_details")
                for row in c:
                    if(row[0]==emp_id)==False:
                        st.error("Incorrect ID or Password")
                    else:
                        phone_no=st.text_input("Enter the Updated designation")
                        address=st.text_input("Enter the Updated department")
                        designation=st.text_input("Enter the Updated Salary")
                        address=st.text_input("Enter the Updated address")
                        dept=st.text_input("Enter the value")
                        salary=st.text_input("Enter the Salary")
                        btn6=st.button("Submit")
                        if btn6:
                            
                            sql='Update emp_details  set phone_no=%s,address=%s,designation=%s,dept=%s,salary=%s where emp_id=%s'
                            data=(phone_no,address,designation,dept,salary,emp_id)
                            c.execute(sql,data)
                            mydb.commit()
                            st.success("Updated")
        


#--------------------------------------------remove emp-----------------------------------

        elif choice1=="Remove Employee":
            emp_id=st.text_input("Enter the Employee ID")
            btn3=st.button("Enter")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("delete from emp_details where emp_id=%s",(emp_id,))
                mydb.commit()
                st.success("Deleted")
#-------------------------------------------------assign project-------------------------
        elif choice1=="assign project":
             eid=st.text_input("Enter the Employee ID")
             project_name=st.text_input("Enter the project_name")
             project_assigned=st.text_input("Enter the project_assigned")
             Deadline=st.text_input("Enter the Deadline")
             target_achieved=st.text_input("Enter the target_achieved")
             progress_review=st.text_input("Enter the progress review") 
             btn3=st.button("Enter")
             if btn3:
                 mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                 c=mydb.cursor()
                 c.execute("insert into project values(%s,%s,%s,%s,%s,%s)",(eid,project_name,project_assigned,Deadline,target_achieved,progress_review))
                 mydb.commit()
                 st.success("input taken")

#-------------------------------------Active Employee---------------------------------
        elif(choice1=="Active Employee"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='ems')
            c=mydb.cursor()
            c.execute("select * from emp_details")
            l=[]
            for r in c:
                l.append(r)       
            df=pd.DataFrame(data=l,columns=['emp_id','emp_pass','emp_name','phone_no','gender','address','Doj','designation','dept','salary'])
            st.dataframe(df)

#---------------------------------------------------update progress--------------------------------------------------

        elif choice1=="update progress":
            emp_id=st.text_input("Enter the Employee ID")
            progress_review=st.text_input("Enter the progress review") 
            btn3=st.button("Enter")
            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="ems")
                c=mydb.cursor()
                c.execute("Update project  set progress='progress review' where eid='emp_id'")
                mydb.commit()
                st.success("input taken")

#------------------------------------------check project status------------------------------------
        elif(choice1=="check project status"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='ems')
            c=mydb.cursor()
            c.execute("select * from project")
            l=[]
            for r in c:
                l.append(r)       
            df=pd.DataFrame(data=l,columns=['eid','project_name','project_assigned','Deadline','target_achieved','progress review'])
            st.dataframe(df)

#--------------------------------------------------------------check attandancen----------------------------------------------------------------
        elif(choice1=="check attendance"):
            mydb=mysql.connector.connect(host='localhost',user='root',password='123456',database='ems')
            c=mydb.cursor()
            c.execute("select * from attendance ")
            l=[]
            for r in c:
                l.append(r)       
            df=pd.DataFrame(data=l,columns=['emp_id','emp_name','DIO'])
            st.dataframe(df)






                
               
               



            
        
