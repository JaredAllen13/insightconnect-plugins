import komand
from .schema import ConnectionSchema, Input
# Custom imports below

import requests
from requests.auth import HTTPBasicAuth

from icon_trendmicro_deepsecurity.util.shared import tryJSON
from icon_trendmicro_deepsecurity.util.shared import checkResponse


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        """
        Get all connection parameters
        """

        self.ivm_url = params.get("ivm_url")
        self.ivm_user = params.get("ivm_user")
        self.ivm_password = params.get("ivm_password")
        self.dsm_url = params.get("dsm_url")
        self.dsm_api_key = params.get("dsm_api_key")
        self.asset_hostname_ivm = params.get("asset_hostname_ivm")
        self.asset_hostname_dsm = params.get("asset_hostname_dsm")

    def test(self):
        """
        Test connection to the Deep Security Manager
        """

        # Prepare request
        url = self.dsm_url + "/api/policies"
        
        post_header = {
                        "Content-type": "application/json",
                        "api-secret-key": self.dsm_api_key,
                        "api-version": "v1"
                        }

        # Get list of policies
        response = requests.get(url,
                                 #data=json.dumps(data),
                                 headers=post_header,
                                 verify=False)                                
        response.close()

        # Try to convert the response data to JSON
        response_data=tryJSON(response)

        # Check response errors
        checkResponse(response)

        self.logger.info("Found " + str(len(response_data['policies'])) + " policies!")
        for policy in response_data['policies']:
          self.logger.info(policy['name'])

        return {'data': response.ok}
