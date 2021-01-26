# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of activity types"


class Input:
    pass

class Output:
    ACTIVITY_TYPES = "activity_types"
    

class ActivitiesTypesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ActivitiesTypesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activity_types": {
      "type": "array",
      "title": "Activity Types",
      "description": "Result of activities types",
      "items": {
        "$ref": "#/definitions/activities_types"
      },
      "order": 1
    }
  },
  "required": [
    "activity_types"
  ],
  "definitions": {
    "activities_types": {
      "type": "object",
      "title": "activities_types",
      "properties": {
        "action": {
          "type": "string",
          "title": "Action",
          "description": "Action descripted in the activity",
          "order": 3
        },
        "descriptionTemplate": {
          "type": "string",
          "title": "Description Template",
          "description": "Activity description template as seen in activity page",
          "order": 2
        },
        "id": {
          "type": "number",
          "title": "Type ID",
          "description": "Activity type ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
