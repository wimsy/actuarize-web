# -*- coding: utf-8 -*-

###############################################################################
#
# ByGoogleLat
# Retrieves information from multiple APIs about places near a set of coordinates retrieved from Google Latitude.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByGoogleLat(Choreography):

    """
    Create a new instance of the ByGoogleLat Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GetPlaces/ByGoogleLat')


    def new_input_set(self):
        return ByGoogleLatInputSet()

    def _make_result_set(self, result, path):
        return ByGoogleLatResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByGoogleLatChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByGoogleLat
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByGoogleLatInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Limits the number of Foursquare venues returned.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) This keyword input can be used to narrow search results for Google Places and Foursquare.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that the response should be in. Valid values are json (the default) and xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) Filters results by type of place, such as: bar, dentist, etc. This is used to filter results for Google Places and Yelp.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the ByGoogleLat choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByGoogleLatResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (Contains the merged results from the API responses.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByGoogleLatChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByGoogleLatResultSet(response, path)
