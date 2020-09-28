## book room path
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - action_reset_all_slots
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* thanks
  - utter_goodbye

## book room stop
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - action_reset_all_slots
  - room_form
  - form{"name":"room_form"}
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_goodbye

## book room continue
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - action_reset_all_slots
  - room_form
  - form{"name":"room_form"}
* out_of_scope
  - utter_ask_continue
* affirm
  - room_form
  - form{"name": null}
  - utter_slots_values

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
