class EpsAction(object):
    """
    Mitigation action to perform with the Cisco Endpoint Protection Service
    (EPS).
    """

    #: Quarantine action
    QUARANTINE = "quarantine"
    #: Unquarantine action
    UNQUARANTINE = "unquarantine"
    #: Shutdown action
    SHUTDOWN = "shutdown"
    #: Terminate action
    TERMINATE = "terminate"
    #: Reauthenticate action
    REAUTHENTICATE = "reAuthenticate"
    #: Port bounce action
    PORT_BOUNCE = "portBounce"
