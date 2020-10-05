# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
from rasa_core_sdk.events import AllSlotsReset

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import random
import dateutil.parser

'''
class action_room_search(Action):

    def name(self) -> Text:
        return "action_room_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility= tracker.get_slot("facility_type")
        room = tracker.get_slot("room_type")
        people = tracker.get_slot("number_of_people")

        message = "Yes we have the room available"
        dispatcher.utter_message(text="Well you are looking for {} of type {} for {}, {}".format(facility,room,people,message))

        return [SlotSet("message",message)]
'''

class action_book_room(Action):
    def name(self) -> Text:
        return "action_book_rooms"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
        print("hi")
        gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Deluxe Room",
                            "subtitle": "These Deluxe Rooms let you relax as you admire a beautiful view of the pool. Stay connected as you enjoy our free WiFi and watch movies with our 32-inch LCD TV and DVD player.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/deluxe_room_details",
                                    "title": "Read More"
                                },
                              {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                },  
                            ]
                        },

                        {
                            "title": "Junior Suite",
                            "subtitle": "Large bedroom with exquisitely embroidered queen or king size bed. Elegant, luxury decor with rich fabrics. Separate sitting room with sofa and armchairs.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/junior_suite_details",
                                    "title": "Read More"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                },
                            ]
                        },
                        {
                            "title": "Club Suite",
                            "image_url":"https://media-cdn.tripadvisor.com/media/photo-s/12/77/d8/18/club-suite-living-room.jpg",
                            "subtitle": "The Club Suite is the ideal choice for a comfortable and lavish stay for both small families and business travelers alike. The gently soothing views and the calming ambiance of the suite add to an enriching experience for our guests.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/club_suite_details",
                                    "title": "Read More"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                }, 
                            ]
                        },
                        
                    ]
                }
            }
        }
        dispatcher.utter_message(json_message=gt)
        return []  


class RoomForm(FormAction):
    def name(self) -> Text:
        return "room_form"

    @staticmethod
    def required_slots(tracker:Tracker) -> List[Text]:
        """ A list of slots that form has to fill"""
        if tracker.get_slot("have_children") == True:
            return ["name","time","number_of_adults","have_children","number_of_children"]
        else:
            return ["name","time","number_of_adults","have_children"]
    def slot_mappings(self) -> Dict[Text,Any]:
        
        return {"name": self.from_text(intent="name"),
                "time": self.from_entity(entity="time"),
                "number_of_adults": self.from_text(intent=None),
                "have_children": [self.from_intent(intent="affirm",value=True),
                                self.from_intent(intent="deny",value=False)],
                "number_of_children": self.from_text(intent=None)}

    '''
    @staticmethod
    def room_db() -> List[Text]:
        """ Database of Room"""
        return[
            "deluxe room",
            "heritage deluxe room",
            "club shangre-la executive",
            "the junior suites",
            "the business suites",
            "the presidential suites",
        ]
    '''
    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False
    '''        
    def validate_room_types(self,value: Text, dispatcher: CollectingDispatcher, tracker:Tracker,domain: Dict[Text,Any]) -> Dict[Text,Any]:
        if value.lower() in self.room_db():
            return {"room_types":value}
        else:
            dispatcher.utter_template("utter_wrong_room_types",tracker)
            return {"room_types": None}
    '''
    def validate_number_of_adults(self,value: Text, dispatcher: CollectingDispatcher, tracker:Tracker,domain: Dict[Text,Any]) -> Dict[Text,Any]:
        if self.is_int(value) and int(value) >0:
            return {"number_of_adults":value}
        else:
            dispatcher.utter_template("utter_wrong_number_of_adults",tracker)
            return {"number_of_adults":None}

    def validate_number_of_children(self,value: Text, dispatcher: CollectingDispatcher, tracker:Tracker,domain: Dict[Text,Any]) -> Dict[Text,Any]:
        if self.is_int(value) and int(value) >0:
            return {"number_of_children":value}
        else:
            dispatcher.utter_template("utter_wrong_number_of_children",tracker)
            return {"number_of_children":None}

    def validate_time(self,
                  value: Text,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any],
                  ) -> Dict[Text, Any]:
    
        if value != None:
            datetime_obj = dateutil.parser.parse(value)
            apptDate= datetime_obj.strftime('%m-%d-%Y')
            
        return {"time": apptDate}

    def submit(self,dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict]:

        dispatcher.utter_template("utter_submit",tracker)
        return []

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        
        return [SlotSet("name",None),SlotSet("number_of_adults",None),SlotSet("have_children",None),SlotSet("number_of_children",None)]

def store_sheet(name,room_types,time,number_of_adults,have_children,number_of_children):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        num = random.randint (0,99999)
        raw_update=[num,name,room_types,time,number_of_adults,have_children,number_of_children]
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials=ServiceAccountCredentials.from_json_keyfile_name('credential.json',scope)
        clients=gspread.authorize(credentials)
        sheet = clients.open('Rasa').sheet1
        sheet.append_row(raw_update)

        response= 'I’m sharing the information on your behalf with our team. Have a nice day!'

        print(response)
        return []

class storedata(Action):

    def name(self) -> Text:
        return "action_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = store_sheet(
            tracker.get_slot('name'),
            tracker.get_slot('room_types'),
            tracker.get_slot('time'),
            tracker.get_slot('number_of_adults'),
            tracker.get_slot('have_children'),
            tracker.get_slot('number_of_children')
            )
        return []