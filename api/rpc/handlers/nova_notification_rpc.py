###SM added

class EventsNotificationEndpoint(object):

    def __init__(self):
        super(EventsNotificationEndpoint, self).__init__()

    def info(self, ctxt, publisher_id, event_type, payload, metadata):
        msg = "=====infoooooooooooooooooooooooo====in===EventsNotificationEndpoint--info====="
        print msg
        #raise Exception(msg)



