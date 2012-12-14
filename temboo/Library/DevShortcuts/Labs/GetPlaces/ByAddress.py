# -*- coding: utf-8 -*-

###############################################################################
#
# ByAddress
# Retrieves information from multiple APIs about places near a specified street address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByAddress(Choreography):

    """
    Create a new instance of the ByAddress Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GetPlaces/ByAddress')


    def new_input_set(self):
        return ByAddressInputSet()

    def _make_result_set(self, result, path):
        return ByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByAddressChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByAddress
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByAddressInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Address input for this choreography. ((required, string) The street address of the user's location.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Limits the number of Foursquare venues results.)
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
A ResultSet with methods tailored to the values returned by the ByAddress choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByAddressResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) Contains combined weather data from Yahoo Weather, NOAA, and EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByAddressResultSet(response, path)
