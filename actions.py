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


class action_room_search(Action):

    def name(self) -> Text:
        return "action_room_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility= tracker.get_slot("facility_type")

        message = "Yes we have the room available"
        dispatcher.utter_message("{}".format(message))

        return [SlotSet("message",message)]

'''
class action_book_room(Action):
    def name(self) -> Text:
        return "action_book_rooms"
    def run(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict[Text,Any]]:
        gt = {
            "attachment": {
                "type": "template",
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
                                    "payload": "/dulex_room_details",
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
                            "image_url":"https://www.discoverysuites.com/files/2015/06/Junior-Suite-Deluxe.jpg",
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
  dispatcher.utter_custom_json(gt)
  return []  

class FacilityForm(FormAction):
     Custom form action to fill all slots required to find specific type facility with its type and value.

    def name(self) -> Text:
        return "facility_form"

    @staticmethod
    def required_slots(tracker:Tracket) -> List[Text]:
        """ A list of slots that form has to fill"""
        return ["facility_type","type_selection"]

    def slot_mapping(self) -> Dict[Text,Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                  intent=["service_provider"]),
                "type_selection": self.from_entity(entity="type_selection",
                                                    intent=['info'])}

    def submit(self,dispatcher: CollectingDispatcher,tracker:Tracker,domain:Dict[Text,Any]) -> List[Dict]:
        return []
'''