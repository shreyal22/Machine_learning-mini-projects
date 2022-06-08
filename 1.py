class radio:
    color='black'
    brand='philips'
    acpower=False
    headphone=False
    def __init__(self):
        self.power='ON'
        self.mod=None
        self.freq=0.0
        self.vol=0
    def power_switch(self,power_status):
        self.power=power_status
        print('your radio is '+str(self.power))
    def mode_switch(self,mod_status):
        self.mod=mod_status
        print('your mod is'+str(self.mod))
    def freq_switch(self,freq_status):
        self.freq=freq_status
        print('the frequency is '+str(self.freq))
    def vol_switch(self,vol_status):
        self.vol=vol_status
        print('the vol is '+str(self.vol))
sj_radio=radio()
print('the color of the radio is'+ radio.color)
print('the brand is'+radio.brand)
sj_radio.power_switch('ON')
sj_radio.mode_switch('FM')
sj_radio.freq_switch(122.9)
sj_radio.vol_switch(23)
sj_radio=None



