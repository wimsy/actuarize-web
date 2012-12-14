# -*- coding: utf-8 -*-

###############################################################################
#
# ByFoursquare
# Retrieves weather and UV index data based on coordinates returned from a Foursquare recent check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ByFoursquare(Choreography):

    """
    Create a new instance of the ByFoursquare Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/GetWeather/ByFoursquare')


    def new_input_set(self):
        return ByFoursquareInputSet()

    def _make_result_set(self, result, path):
        return ByFoursquareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByFoursquareChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ByFoursquare
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ByFoursquareInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary containing your Foursquare and Yahoo credentials. See Choreo documentation for formatting examples.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the Shout input for this choreography. ((optional, string) A message about your check-in. The maximum length of this field is 140 characters.)
        """
        def set_Shout(self, value):
            InputSet._set_input(self, 'Shout', value)

        """
        Set the value of the VenueID input for this choreography. ((optional, string) The venue where the user is checking in. Required if creating a Foursquare checkin.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the ByFoursquare choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ByFoursquareResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) Contains weather information based on the coordinates returned from the Foursquare checkin.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ByFoursquareChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByFoursquareResultSet(response, path)
