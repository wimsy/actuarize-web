# -*- coding: utf-8 -*-

###############################################################################
#
# Music
# Retrieves music associated with a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Music(Choreography):

    """
    Create a new instance of the Music Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/Music')


    def new_input_set(self):
        return MusicInputSet()

    def _make_result_set(self, result, path):
        return MusicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MusicChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Music
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MusicInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the Fields input for this choreography. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Used to page through results. Limits the number of records returned in the response.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through results. Returns results starting from the specified number.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ProfileID input for this choreography. ((optional, string) The id of the profile to retireve music for. Defaults to "me" indicating the authenticated user.)
        """
        def set_ProfileID(self, value):
            InputSet._set_input(self, 'ProfileID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Since input for this choreography. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        def set_Since(self, value):
            InputSet._set_input(self, 'Since', value)

        """
        Set the value of the Until input for this choreography. ((optional, date) Used for time-based pagination. Values can be a unix timestamp or any date accepted by strtotime.)
        """
        def set_Until(self, value):
            InputSet._set_input(self, 'Until', value)


"""
A ResultSet with methods tailored to the values returned by the Music choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MusicResultSet(ResultSet):
        """
        Retrieve the value for the "HasNext" output from this choreography execution. ((boolean) A boolean flag indicating that a next page exists.)
        """
        def get_HasNext(self):
            return self._output.get('HasNext', None)
        """
        Retrieve the value for the "HasPrevious" output from this choreography execution. ((boolean) A boolean flag indicating that a previous page exists.)
        """
        def get_HasPrevious(self):
            return self._output.get('HasPrevious', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.  Enhanced Choreo Outputs generated for this field.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MusicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MusicResultSet(response, path)
