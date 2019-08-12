#python

import datetime
import time
from iqoptionapi.ws.chanels.base import Base

#work for forex digit cfd(stock)

class Digital_options_place_digital_option(Base):
    name = "sendMessage"
    def __call__(self,instrument_id,amount):
        data = {
        "name": "digital-options.place-digital-option",
        "version":"1.0",
        "body":{
            "user_balance_id":int(self.api.profile.balance_id),
            "instrument_id":str(instrument_id),
            "amount":str(amount)
            
            }
        }
        self.send_websocket_request(self.name, data)
 
