# -*- coding: utf-8 -*-

###############################################################################
#
# GetActiveChannels
# Returns the active Channels associated with this syndication service for the publisher.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetActiveChannels(Choreography):

    """
    Create a new instance of the GetActiveChannels Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AdSenseForContentService/GetActiveChannels')


    def new_input_set(self):
        return GetActiveChannelsInputSet()

    def _make_result_set(self, result, path):
        return GetActiveChannelsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetActiveChannelsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetActiveChannels
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetActiveChannelsInputSet(InputSet):
        """
        Set the value of the ChannelService_Type input for this choreography. ((required, string) One of 'Url' or 'Custom'.)
        """
        def set_ChannelService_Type(self, value):
            InputSet._set_input(self, 'ChannelService_Type', value)

        """
        Set the value of the ClientID input for this choreography. ((required, string) The ID of the publisher to get active channels of.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((required, password) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SynServiceID input for this choreography. ((required, string) The ID of this service.)
        """
        def set_SynServiceID(self, value):
            InputSet._set_input(self, 'SynServiceID', value)


"""
A ResultSet with methods tailored to the values returned by the GetActiveChannels choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetActiveChannelsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetActiveChannelsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetActiveChannelsResultSet(response, path)
