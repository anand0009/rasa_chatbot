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
  - utter_cheer_up

## check1
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* affirm
  - utter_ask_more
* book
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* deny
  - action_reset_all_slots
  - utter_reconfirm
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* affirm
  - action_store
  - action_reset_all_slots
  - utter_contact

## check
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* affirm
  - utter_ask_more
* book
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* affirm
  - action_store
  - action_reset_all_slots
  - utter_contact

## check negative
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* deny
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* affirm
  - utter_ask_more
* book
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* deny
  - action_reset_all_slots
  - utter_reconfirm
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* affirm
  - action_store
  - action_reset_all_slots
  - utter_contact

## check negative 1
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* deny
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* affirm
  - utter_ask_more
* book
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* affirm
  - action_store
  - action_reset_all_slots
  - utter_contact

## check3
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* affirm
  - utter_ask_more
* describe
  - utter_dulexe_room_details
  - utter_more
* book
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* deny
  - action_reset_all_slots
  - utter_reconfirm
  - room_form
  - form{"name":"room_form"}
  - form{"name": null}
  - utter_slots_values
* affirm
  - action_store
  - action_reset_all_slots
  - utter_contact

## check3
* greet
  - utter_how_can_i_help
* rooms_and_suites
  - utter_ask_room_types
* deluxe_room
  - utter_deluxe_image
  - utter_deluxe_confirm
* affirm
  - utter_ask_more
* describe
  - utter_dulexe_room_details
  - utter_more
* thanks
  - utter_thanks