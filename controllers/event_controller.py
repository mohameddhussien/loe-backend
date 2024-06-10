from flask import jsonify, request, g
from models.event_model import EventModel
from models.db import Database

class EventController:
    def __init__(self):
        self.db: Database = g.db

    def get_all_events(self):
        eventModel = EventModel(self.db)
        events = eventModel.get_all_events()
        for event in events:
            event["images"] = eventModel.get_images_by_event_id(event["e_id"])
        return jsonify(events if events else [])


    def get_event(self):
        eventModel = EventModel(self.db)
        event_key = request.json.get("event_key")
        if event_key:
            event = eventModel.get_event_by_key(event_key)
            if event:
                event = event[0]
                event["images"] = eventModel.get_images_by_event_id(event["e_id"])
                return jsonify(event)
            else:
                return jsonify({"error": "Event not found"}), 404
        return jsonify({"error": "Event key not provided"}), 400
