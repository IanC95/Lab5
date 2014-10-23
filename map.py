from items import *

room_reception = {
    "name": "Reception",

    "description":
    """You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""",

    "exits": {"south": "Robs", "east": "Tutor", "west": "Parking"},

    "items": []
}

room_robs = {
    "name": "Robs' room",

    "description":
    """You are leaning agains the door of the systems managers'
room. Inside you notice Rob Evans and Rob Davies. They
ignore you. To the north is the reception.""",

    "exits":  {"north": "Reception"},

    "items": [item_map]
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west and the
lecture theatre is to the south.""",

    "exits": {"west": "Reception", "south": "Lecture"},

    "items": [item_handbook]
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"east": "Reception", "south": "Office"},

    "items": [item_keys]
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Parking"},

    "items": [item_wallet]
}

room_lecture = {
    "name": "the lecture theatre",

    "description":
    """You are standing in a grand room, there are many
seats. Kirill stares at you with a deep loathing,
you tremble with fear as Kirill's eyes burn into
your soul. You have no escape, Kirill screams and
charges at you. You prepare yourself for the
onslaught.""",

    "exits": {},

    "items": []
}


rooms = {
    "Reception": room_reception,
    "Robs": room_robs,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office,
    "Lecture": room_lecture
}
