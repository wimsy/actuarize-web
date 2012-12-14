# -*- coding: utf-8 -*-

###############################################################################
#
# AdvancedSearch
# Performs a detailed search of the EPA Design for the Environment database.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AdvancedSearch(Choreography):

    """
    Create a new instance of the AdvancedSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/DesignForEnvironment/AdvancedSearch')


    def new_input_set(self):
        return AdvancedSearchInputSet()

    def _make_result_set(self, result, path):
        return AdvancedSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AdvancedSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AdvancedSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AdvancedSearchInputSet(InputSet):
        """
        Set the value of the Operator input for this choreography. ((optional, string) Default output is "=" when SearchType=sector_id or product_id, and "CONTAINING" when SearchType=partner, product, or sector. Other possible values are: "<", " >", "!=", and "BEGINNING".)
        """
        def set_Operator(self, value):
            InputSet._set_input(self, 'Operator', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((conditional, string) Response can be returned in JSON or XML. Defaults to XML.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the RowEnd input for this choreography. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        def set_RowEnd(self, value):
            InputSet._set_input(self, 'RowEnd', value)

        """
        Set the value of the RowStart input for this choreography. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        def set_RowStart(self, value):
            InputSet._set_input(self, 'RowStart', value)

        """
        Set the value of the SearchType input for this choreography. ((conditional, string) Indicate either "sector", "sector_id", "partner", "product", or "product_id." Used together with SearchValue and the optional Operator input to formulate a specific search of the DfE database.)
        """
        def set_SearchType(self, value):
            InputSet._set_input(self, 'SearchType', value)

        """
        Set the value of the SearchValue input for this choreography. ((conditional, integer) Indicate the product, code, or sector to search for. Used together with SearchType and the optional Operator input to create a customized search.)
        """
        def set_SearchValue(self, value):
            InputSet._set_input(self, 'SearchValue', value)


"""
A ResultSet with methods tailored to the values returned by the AdvancedSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AdvancedSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Count" output from this choreography execution. (The total number of records returned for any given search.)
        """
        def get_Count(self):
            return self._output.get('Count', None)
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from EnviroFacts.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AdvancedSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AdvancedSearchResultSet(response, path)
