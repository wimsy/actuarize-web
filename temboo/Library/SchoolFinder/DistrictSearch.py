# -*- coding: utf-8 -*-

###############################################################################
#
# DistrictSearch
# Returns a list of school profiles and related school information for a zip code, city, state, or other criteria in the search parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DistrictSearch(Choreography):

    """
    Create a new instance of the DistrictSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/DistrictSearch')


    def new_input_set(self):
        return DistrictSearchInputSet()

    def _make_result_set(self, result, path):
        return DistrictSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DistrictSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DistrictSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DistrictSearchInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your School Finder API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((conditional, string) The name of a city. City requests must also be accompanied by the corresponding state parameter.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the DistrictID input for this choreography. ((conditional, string) The internal Education.com id of a school district.)
        """
        def set_DistrictID(self, value):
            InputSet._set_input(self, 'DistrictID', value)

        """
        Set the value of the DistrictLEA input for this choreography. ((conditional, string) The NCES Local Education Agency (LEA) id of a school district.)
        """
        def set_DistrictLEA(self, value):
            InputSet._set_input(self, 'DistrictLEA', value)

        """
        Set the value of the DistrictName input for this choreography. ((conditional, string) The name of the district.)
        """
        def set_DistrictName(self, value):
            InputSet._set_input(self, 'DistrictName', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the State input for this choreography. ((conditional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)


"""
A ResultSet with methods tailored to the values returned by the DistrictSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DistrictSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Education.com.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DistrictSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DistrictSearchResultSet(response, path)
