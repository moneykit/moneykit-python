from enum import Enum


class LinkStateChangedWebhookWebhookEvent(str, Enum):
    LINK_STATE_CHANGED = "link.state_changed"

    def __str__(self) -> str:
        return str(self.value)
