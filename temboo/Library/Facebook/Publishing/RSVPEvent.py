# -*- coding: utf-8 -*-

###############################################################################
#
# RSVPEvent
# RSVP to an event as "attending", "maybe", or "declined".
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RSVPEvent(Choreography):

    """
    Create a new instance of the RSVPEvent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/RSVPEvent')


    def new_input_set(self):
        return RSVPEventInputSet()

    def _make_result_set(self, result, path):
        return RSVPEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RSVPEventChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RSVPEvent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RSVPEventInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the EventID input for this choreography. ((required, string) The id for the event  to rsvp for.)
        """
        def set_EventID(self, value):
            InputSet._set_input(self, 'EventID', value)

        """
        Set the value of the RSVP input for this choreography. ((required, string) The RSVP for the event. Valid values are: attending, maybe, or declined.)
        """
        def set_RSVP(self, value):
            InputSet._set_input(self, 'RSVP', value)


"""
A ResultSet with methods tailored to the values returned by the RSVPEvent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RSVPEventResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RSVPEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RSVPEventResultSet(response, path)
