# -*- coding: utf-8 -*-

###############################################################################
#
# SchoolSearch
# Returns a list of school district profiles and related school information for a zip code, city, state, or other criteria in the search parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SchoolSearch(Choreography):

    """
    Create a new instance of the SchoolSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/SchoolSearch')


    def new_input_set(self):
        return SchoolSearchInputSet()

    def _make_result_set(self, result, path):
        return SchoolSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SchoolSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SchoolSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SchoolSearchInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Your School Finder API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the City input for this choreography. ((conditional, string) The name of a city. Must also be accompanied by the corresponding state parameter.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the County input for this choreography. ((conditional, string) The name of a county.)
        """
        def set_County(self, value):
            InputSet._set_input(self, 'County', value)

        """
        Set the value of the Distance input for this choreography. ((conditional, decimal) A distance in miles from a specific latitude/longitude. The suggested value is around 1.5 miles. Please note that distance is required when using latitude and longitude parameters.)
        """
        def set_Distance(self, value):
            InputSet._set_input(self, 'Distance', value)

        """
        Set the value of the DistrictID input for this choreography. ((optional, string) The internal Education.com id of a school district.)
        """
        def set_DistrictID(self, value):
            InputSet._set_input(self, 'DistrictID', value)

        """
        Set the value of the DistrictLEA input for this choreography. ((optional, string) The NCES Local Education Agency (LEA) id of a school district.)
        """
        def set_DistrictLEA(self, value):
            InputSet._set_input(self, 'DistrictLEA', value)

        """
        Set the value of the Latitude input for this choreography. ((conditional, decimal) A latitude which serves as the center for distance searches. Please note that distance is required when using latitude and longitude parameters.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((conditional, decimal) A longitude which serves as the center for distance searches. Please note that distance is required when using latitude and longitude parameters.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the MinResult input for this choreography. ((optional, decimal) Minimum number of search results to return. The search will be expanded in increments of 0.5 miles until the minresult is reached. minResult is only valid for zip code and latitude/longitude requests.)
        """
        def set_MinResult(self, value):
            InputSet._set_input(self, 'MinResult', value)

        """
        Set the value of the NCES input for this choreography. ((optional, string) The National Center for Education Statistics (NCES) id of the school you want to find.)
        """
        def set_NCES(self, value):
            InputSet._set_input(self, 'NCES', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SchoolID input for this choreography. ((optional, string) The Education.com id of the school you want to find.)
        """
        def set_SchoolID(self, value):
            InputSet._set_input(self, 'SchoolID', value)

        """
        Set the value of the State input for this choreography. ((conditional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Zip input for this choreography. ((conditional, integer) A five digit US postal code.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the SchoolSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SchoolSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Education.com.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SchoolSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SchoolSearchResultSet(response, path)
