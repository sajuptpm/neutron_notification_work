###SM added
import oslo_messaging

class EventsNotificationEndpoint(object):

    def __init__(self):
        super(EventsNotificationEndpoint, self).__init__()

    def info(self, ctxt, publisher_id, event_type, payload, metadata):
        msg = "=====infoooooooooooooooooooooooo====in===EventsNotificationEndpoint--info====="
        print msg
        #return oslo_messaging.NotificationResult.HANDLED
        return oslo_messaging.NotificationResult.REQUEUE
        #raise Exception(msg)



