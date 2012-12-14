# -*- coding: utf-8 -*-

###############################################################################
#
# ByGoogleLat
# Retrieves weather and UV index data based on coordinates returned from Google Latitude.
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
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GetWeather/ByGoogleLat')


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
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary containing your Google Latitude and Yahoo credentials. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)


"""
A ResultSet with methods tailored to the values returned by the ByGoogleLat choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByGoogleLatResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) Contains weather information based on the coordinates returned from the Foursquare checkin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByGoogleLatChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByGoogleLatResultSet(response, path)
