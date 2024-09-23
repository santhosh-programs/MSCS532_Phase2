from collections import deque
# Ensure this import points to your Notification class
from notification import Notification


class NotificationsQueue:
    def __init__(self):
        self.notifications_queue = deque()

    def add_notification(self, notification: Notification):
        self.notifications_queue.append(notification)

    def get_last_notification(self) -> Notification:
        if not self.notifications_queue:
            return None
        return self.notifications_queue.pop()

# Example usage:
# Assuming the Notification class is defined as per previous conversions.


notification1 = Notification(
    id=1, title="Reminder", description="Don't forget the meeting!")
notification2 = Notification(
    id=2, title="Alert", description="New message received.")

notifications_queue = NotificationsQueue()
notifications_queue.add_notification(notification1)
notifications_queue.add_notification(notification2)

# Outputs the last added notification
print(notifications_queue.get_last_notification())
