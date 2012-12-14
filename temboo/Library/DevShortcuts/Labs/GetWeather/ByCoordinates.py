# -*- coding: utf-8 -*-

###############################################################################
#
# ByCoordinates
# Retrieves weather and UV index data for a given Geo point using the Yahoo Weather, NOAA, and EnviroFacts APIs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByCoordinates(Choreography):

    """
    Create a new instance of the ByCoordinates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GetWeather/ByCoordinates')


    def new_input_set(self):
        return ByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return ByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByCoordinatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByCoordinates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByCoordinatesInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary containing a Yahoo App ID. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate to use when looking up weather information.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate to use when looking up weather information.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)


"""
A ResultSet with methods tailored to the values returned by the ByCoordinates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByCoordinatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) Contains combined weather data from Yahoo Weather, NOAA, and EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByCoordinatesResultSet(response, path)
