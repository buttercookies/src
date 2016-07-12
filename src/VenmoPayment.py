__author__ = 'lawrenberg'


class VenmoPayment(object):
    def __init__(self, actor, target, timestamp):
        self.actor = actor
        self.target = target
        self.timestamp = timestamp

    def get_actor(self):
        return self.actor

    def get_target(self):
        return self.target

    def get_timestamp(self):
        return self.timestamp

    def __str__(self):
        return {"actor": self.get_actor(), "target": self.get_target(), "timestamp": self.get_timestamp() }
