from .saba import SabaClient
from .fb import FbClient
from .im import ImClient

clients = {
    "saba": SabaClient,
    "fb": FbClient,
    "im": ImClient,
}