
# coding: utf-8

# In[1]:


from pynq import Overlay
from pynq.lib import AxiGPIO
ol = Overlay('btn.bit')


# In[2]:


ol.is_loaded()


# # info command

# In[3]:


ol


# In[4]:


ol.ip_dict.keys()


# In[5]:


#ol.ip_dict['led_gpio']


# In[6]:


led_ip = ol.ip_dict['led_gpio'] #creating alias for IP
switches_ip = ol.ip_dict['sw_gpio']
btns_ip = ol.ip_dict['btn_gpio']
leds = AxiGPIO(led_ip).channel1
switches = AxiGPIO(switches_ip).channel1
btns = AxiGPIO(btns_ip).channel1
switches.setdirection("in") 
switches.setlength(3)
btns.setdirection("in")
btns.read()
switches.read()


# In[7]:


switches[0].read() #read status of swtiches


# In[8]:


switches[1].read()


# In[ ]:


btns.read()


# In[ ]:


while(True):
    if(switches[0].read() == 1):
        leds[0:2].on()
    elif(switches.read() == 0):
        leds[0:2].off()
    if(switches[1].read() == 1):
        leds[2:4].on()
    elif(switches[1].read() == 0):
         leds[2:4].off()
    if(switches[1].read() == 1 and switches[0].read() == 1):
        leds[0:4].on()
    else:
         leds[0:4].off()
    if(btns[1].read() == 1):
        #color = 4
        leds[1].on()
        leds[2:4].off()
        #leds[3:4].off()
    elif(btns[3].read() == 1):
        #color = 3
        leds[3].on()
        leds[0:2].off()
        leds[4].off()
    elif(btns[2].read() == 1):
        #color(5)
        leds[2].on()
        leds[3:4].off()
        leds[0:1].off()
    elif(btns[0].read() == 1):
        leds[0].on()
        leds[1:4].off()

