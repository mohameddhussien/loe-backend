from models.db import Database

class EventModel:
    def __init__(self, db: Database):
        self.db = db
        
    def get_all_events(self):
        events = self.db.call_stored_procedure("GetAllEvents")
        return events

    def get_event_by_key(self, event_key):
        event = self.db.call_stored_procedure("GetEventByKey", (event_key,))
        return event

    def get_images_by_event_id(self, event_id):
        images = self.db.call_stored_procedure("GetAllImagesOfEvent", (event_id,))
        return images
