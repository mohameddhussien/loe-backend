from flask import Blueprint
from controllers.event_controller import EventController

event_bp = Blueprint('event_bp', __name__)

@event_bp.route("/events", methods=["GET"])
def handle_get_all_events():
    eventController = EventController()
    return eventController.get_all_events()

@event_bp.route("/event", methods=["POST"])
def handle_get_event():
    eventController = EventController()
    return eventController.get_event()
