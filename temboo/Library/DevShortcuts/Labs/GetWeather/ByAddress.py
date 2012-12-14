# -*- coding: utf-8 -*-

###############################################################################
#
# ByAddress
# Retrieves weather and UV index data for a given Geo point using the Yahoo Weather, NOAA, and EnviroFacts APIs.
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
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GetWeather/ByAddress')


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
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary containing a Yahoo App ID. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Address input for this choreography. ((required, string) The street address of the location to get weather for.)
        """
        def set_Address(self, value):
            InputSet._set_input(self, 'Address', value)


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
