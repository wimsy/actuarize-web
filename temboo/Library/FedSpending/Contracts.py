# -*- coding: utf-8 -*-

###############################################################################
#
# Contracts
# Allows access to the information in the Federal Procurement Data System (FPDS) database, which reports all federal contracts awarded. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Contracts(Choreography):

    """
    Create a new instance of the Contracts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FedSpending/Contracts')


    def new_input_set(self):
        return ContractsInputSet()

    def _make_result_set(self, result, path):
        return ContractsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ContractsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Contracts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ContractsInputSet(InputSet):
        """
        Set the value of the City input for this choreography. ((conditional, string) The city within a contractor's address.)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the CompanyName input for this choreography. ((conditional, string) The name of a a contractor or contractor parent company.)
        """
        def set_CompanyName(self, value):
            InputSet._set_input(self, 'CompanyName', value)

        """
        Set the value of the Completion input for this choreography. ((conditional, string) The competition status of a contract. Valid values: c=Full competition, o=Full competition, one bid, p=Competition, exclusion of sources, n=Not complete, a=Not available, f=Follow-up, u=Unknown.)
        """
        def set_Completion(self, value):
            InputSet._set_input(self, 'Completion', value)

        """
        Set the value of the Detail input for this choreography. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        def set_Detail(self, value):
            InputSet._set_input(self, 'Detail', value)

        """
        Set the value of the FirstYearRange input for this choreography. ((conditional, integer) Specifies the first year in a range of years; if used, must be used with LastYearRange and without FiscalYear.)
        """
        def set_FirstYearRange(self, value):
            InputSet._set_input(self, 'FirstYearRange', value)

        """
        Set the value of the FiscalYear input for this choreography. ((conditional, integer) Specifies a single year; defaults to all years.)
        """
        def set_FiscalYear(self, value):
            InputSet._set_input(self, 'FiscalYear', value)

        """
        Set the value of the LastYearRange input for this choreography. ((conditional, integer) Specifies the last year in a range of years; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        def set_LastYearRange(self, value):
            InputSet._set_input(self, 'LastYearRange', value)

        """
        Set the value of the MajAgency input for this choreography. ((conditional, string) The 2-character code for a major governmental agency issuing contracts.)
        """
        def set_MajAgency(self, value):
            InputSet._set_input(self, 'MajAgency', value)

        """
        Set the value of the MaxRecords input for this choreography. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        def set_MaxRecords(self, value):
            InputSet._set_input(self, 'MaxRecords', value)

        """
        Set the value of the ModAgency input for this choreography. ((conditional, string) The 4-digit code for a specific governmental agency issuing contracts.)
        """
        def set_ModAgency(self, value):
            InputSet._set_input(self, 'ModAgency', value)

        """
        Set the value of the PIID input for this choreography. ((conditional, integer) A Federal ID number for the contract.)
        """
        def set_PIID(self, value):
            InputSet._set_input(self, 'PIID', value)

        """
        Set the value of the PSCCategory input for this choreography. ((conditional, string) The 2-character code for a major product or service category.)
        """
        def set_PSCCategory(self, value):
            InputSet._set_input(self, 'PSCCategory', value)

        """
        Set the value of the PSC input for this choreography. ((conditional, string) The 4-character code for a product or service.)
        """
        def set_PSC(self, value):
            InputSet._set_input(self, 'PSC', value)

        """
        Set the value of the PopCountryCode input for this choreography. ((conditional, string) The two-letter country code for the place of performance country.)
        """
        def set_PopCountryCode(self, value):
            InputSet._set_input(self, 'PopCountryCode', value)

        """
        Set the value of the PopDistrict input for this choreography. ((conditional, string) The Congressional District of the place of performance.)
        """
        def set_PopDistrict(self, value):
            InputSet._set_input(self, 'PopDistrict', value)

        """
        Set the value of the PopZipCode input for this choreography. ((conditional, integer) The ZIP code of the place of performance.)
        """
        def set_PopZipCode(self, value):
            InputSet._set_input(self, 'PopZipCode', value)

        """
        Set the value of the SortBy input for this choreography. ((optional, string) Determines how records are sorted. Valid values: r (contractor/recipient name), f (dollars of awards),g (major contracting agency),p (Product or Service Category),d (date of award). Defaults to f.)
        """
        def set_SortBy(self, value):
            InputSet._set_input(self, 'SortBy', value)

        """
        Set the value of the StateCode input for this choreography. ((conditional, string) The state abbreviation of the state of the place of performance.)
        """
        def set_StateCode(self, value):
            InputSet._set_input(self, 'StateCode', value)

        """
        Set the value of the State input for this choreography. ((conditional, string) The state abbreviation within a contractor's address.)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the TextSearch input for this choreography. ((conditional, string) Free text search within the text that describes what the contract is for.)
        """
        def set_TextSearch(self, value):
            InputSet._set_input(self, 'TextSearch', value)

        """
        Set the value of the VendorCountryCode input for this choreography. ((conditional, string) The two-letter country code for the country in a contractor's address.)
        """
        def set_VendorCountryCode(self, value):
            InputSet._set_input(self, 'VendorCountryCode', value)

        """
        Set the value of the VendorDistrict input for this choreography. ((conditional, string) The 4-character Congressional District within which a contractor is located.)
        """
        def set_VendorDistrict(self, value):
            InputSet._set_input(self, 'VendorDistrict', value)

        """
        Set the value of the ZipCode input for this choreography. ((conditional, integer) The ZIP code within a contractor's address.)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the Contracts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ContractsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FedSpending.org.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ContractsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ContractsResultSet(response, path)
