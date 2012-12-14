# -*- coding: utf-8 -*-

###############################################################################
#
# GetNearbyContacts
# Searches Foursquare recent check-ins and the Facebook social graph with a given set of Geo coordinates
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetNearbyContacts(Choreography):

    """
    Create a new instance of the GetNearbyContacts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DevShortcuts/Labs/Social/GetNearbyContacts')


    def new_input_set(self):
        return GetNearbyContactsInputSet()

    def _make_result_set(self, result, path):
        return GetNearbyContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNearbyContactsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetNearbyContacts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetNearbyContactsInputSet(InputSet):
        """
        Set the value of the APICredentials input for this choreography. ((required, json) A JSON dictionary containing Facebook and Foursquare credentials.)
        """
        def set_APICredentials(self, value):
            InputSet._set_input(self, 'APICredentials', value)

        """
        Set the value of the AfterTimestamp input for this choreography. ((optional, date) Seconds after which to look for checkins, e.g. for looking for new checkins since the last fetch.)
        """
        def set_AfterTimestamp(self, value):
            InputSet._set_input(self, 'AfterTimestamp', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate of the location to search for.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Used to page through results. Limits the number of records returned in the API responses.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((conditional, decimal) The longitude coordinate of the location to search for.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through Facebook results. Returns results starting from the specified number.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)


"""
A ResultSet with methods tailored to the values returned by the GetNearbyContacts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetNearbyContactsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) A merged result of Foursquare and Facebook location based searches.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetNearbyContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNearbyContactsResultSet(response, path)
