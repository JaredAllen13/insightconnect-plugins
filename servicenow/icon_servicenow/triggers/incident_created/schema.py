# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Identifies if a new incident has been created"


class Input:
    
    FREQUENCY = "frequency"
    QUERY = "query"
    

class Output:
    
    SYSTEM_ID = "system_id"
    

class IncidentCreatedInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "frequency": {
      "type": "integer",
      "title": "Frequency",
      "description": "How often to poll for new incidents (in seconds)",
      "default": 5,
      "order": 2
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Non-encoded query string to match new incident records (will poll for any new incident if query is omitted)",
      "order": 1
    }
  },
  "required": [
    "frequency"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IncidentCreatedOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "system_id": {
      "type": "string",
      "title": "System ID",
      "description": "System ID of new incident",
      "order": 1
    }
  },
  "required": [
    "system_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
