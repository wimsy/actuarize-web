# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Returns objects associated with Geo points near a specified set of coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Query(Choreography):

    """
    Create a new instance of the Query Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Parse/GeoPoints/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Query
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class QueryInputSet(InputSet):
        """
        Set the value of the ApplicationID input for this choreography. ((required, string) The Application ID provided by Parse.)
        """
        def set_ApplicationID(self, value):
            InputSet._set_input(self, 'ApplicationID', value)

        """
        Set the value of the ClassName input for this choreography. ((required, string) The class name for the object being created.)
        """
        def set_ClassName(self, value):
            InputSet._set_input(self, 'ClassName', value)

        """
        Set the value of the Count input for this choreography. ((optional, boolean) A flag indicating to include a count of objects in the response. Set to 1 to include a count. Defaults to 0.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the Include input for this choreography. ((optional, string) Specify a field to return multiple types of related objects in this query.  For example, enter: post.author, to retrieve posts and their authors related to this class.)
        """
        def set_Include(self, value):
            InputSet._set_input(self, 'Include', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude coordinate of the Geo Point.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of results to return.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude coordinate of the Geo Point.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the RESTAPIKey input for this choreography. ((required, string) The REST API Key provided by Parse.)
        """
        def set_RESTAPIKey(self, value):
            InputSet._set_input(self, 'RESTAPIKey', value)

        """
        Set the value of the Skip input for this choreography. ((optional, integer) Returns only records after this number. Used in combination with the Limit input to page through many results.)
        """
        def set_Skip(self, value):
            InputSet._set_input(self, 'Skip', value)


"""
A ResultSet with methods tailored to the values returned by the Query choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class QueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Parse.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
