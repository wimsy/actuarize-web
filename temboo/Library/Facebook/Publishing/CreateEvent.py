# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEvent
# Creates an event.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEvent(Choreography):

    """
    Create a new instance of the CreateEvent Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/CreateEvent')


    def new_input_set(self):
        return CreateEventInputSet()

    def _make_result_set(self, result, path):
        return CreateEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEventChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEvent
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEventInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the EndTime input for this choreography. ((optional, date) The end time of the event formatted as a ISO-8601 string (i.e 2012-07-04 or 2012-07-04T19:00:00-0700).)
        """
        def set_EndTime(self, value):
            InputSet._set_input(self, 'EndTime', value)

        """
        Set the value of the Name input for this choreography. ((required, string) The name of the event.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the ProfileID input for this choreography. ((optional, string) The id of the profile that the event will be created for. Defaults to "me" indicating the authenticated user.)
        """
        def set_ProfileID(self, value):
            InputSet._set_input(self, 'ProfileID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the StartTime input for this choreography. ((required, date) The start time of the event formatted as a ISO-8601 string (i.e 2012-07-04 or 2012-07-04T19:00:00-0700).)
        """
        def set_StartTime(self, value):
            InputSet._set_input(self, 'StartTime', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEvent choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEventResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEventResultSet(response, path)
