## book room path
* greet
  - utter_how_can_i_help
* service_provider {"facility_type":"room"}
  - utter_ask_room_type
* info {"room_type":"deluxe","number_of_person":"3 person"}
  - action_room_search
  - slot{"message":"Yes we have the room available"}
* thanks
  - utter_goodbye

## book room + people 
* greet
  - utter_how_can_i_help
* service_provider {"facility_type":"room"}
  - utter_ask_room_type
* info {"room_type":"deluxe"}
  - utter_ask_number_of_people
* inform {"number_of_person":"3 person"}
  - action_room_search
  - slot{"message":"Yes we have the room available"}
* thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
