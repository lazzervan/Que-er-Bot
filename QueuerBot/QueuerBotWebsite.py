import streamlit as st
import time
#from QueuerBot import qid

#15 people waiting infront of you
#2- 16
# your queue id number is:
# enter queue id number to be tracked
# average waiting time
# your waiting time

beta_st.set_page_config(page_title= "Queuer Bot Website", page_icon=":star:")

#header sec
#[theme]
backgroundColor="#00aeff"
secondaryBackgroundColor="#022b75"
textColor="#ffffff"
font="monospace"



with st.container():
    st.title("Queuer Bot Queue")
    
    placeholder = st.empty()

    with st.container():
        
        idtracker = st.text_input("**Enter Queue ID to track:**", "0")

        

    for seconds in range(1000):
            #with open('spots.txt') as g:


        with placeholder.container():
            with open('websitedata.txt') as f:
                st.header("Your Queue ID is: " + idtracker)
                data = f.readlines()
                howmany = data[0].rstrip("\n")
                nowserve = data[1].rstrip("\n")
                first = data[2].rstrip("\n")
                last = data[3].rstrip("\n")
                average = data[4].rstrip("\n")

                waitingtime = (float(average)) / 60
                waitingid = ((float(idtracker) - float(nowserve)) * float(waitingtime))
                #waitingtimeseconds = (float(howmany)*float(average)) % 60
                if first == idtracker:
                    st.warning("**You're up next!**")
                    
                else:
                    pass

                st.subheader(howmany+" People waiting in front of you.")
                #st.subheader(nowserve)
                st.subheader("Now Serving: " + "**"+nowserve+"**")
                st.subheader("First: "+ first + " Last: " + last)
                st.subheader("Approx. Waiting Time: " + str(int(waitingid)) +" minute/s ")
                #st.subheader("Last   in Queue: "+last)
                #st.subheader("wow")
                
            
            time.sleep(1)
    

    
