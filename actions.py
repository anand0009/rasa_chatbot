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
