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
'''
class action_book_room(Action):
    def name(self) -> Text:
        return "action_book_rooms"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
        print("hi")
        gt = {
            "attachment": {
                "type": "response",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Deluxe Room",
                            "image_url":"https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/125/2017/05/25023446/Rooms-Suites-Section-2nd-Room-Deluxe-Room.jpg",
                            "subtitle": "These Deluxe Rooms let you relax as you admire a beautiful view of the pool. Stay connected as you enjoy our free WiFi and watch movies with our 32-inch LCD TV and DVD player.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/info{/“room_types/”:/“Deluxe/”}",
                                    "title": "Read More"
                                },
                              {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                },  
                            ]
                        }
                        
                        
                    ]
                }
            }
        }
        dispatcher.utter_message(json_message=gt)
        return []  
'''

class RoomForm(FormAction):
    def name(self) -> Text:
        return "room_form"

    @staticmethod
    def required_slots(tracker:Tracker) -> List[Text]:
        """ A list of slots that form has to fill"""
        
        return ["room_types","number_of_adults","number_of_children"]
        
    def slot_mappings(self) -> Dict[Text,Any]:
        return {"room_types": self.from_entity(entity="room_types",
                                                intent=["room_info"]),
                "number_of_adults": self.from_text(intent=None),
                "number_of_children": self.from_text(intent=None)}

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

    @staticmethod
    def is_int(string: Text) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_room_types(self,value: Text, dispatcher: CollectingDispatcher, tracker:Tracker,domain: Dict[Text,Any]) -> Dict[Text,Any]:
        if value.lower() in self.room_db():
            return {"room_types":value}
        else:
            dispatcher.utter_template("utter_wrong_room_types",tracker)
            return {"room_types": None}

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

    def submit(self,dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict]:
        dispatcher.utter_template("utter_submit",tracker)
        return []