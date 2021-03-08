# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a private InsightIDR threat and add indicators to this threat"


class Input:
    INDICATORS = "indicators"
    NOTE_TEXT = "note_text"
    THREAT_NAME = "threat_name"
    

class Output:
    REJECTED_INDICATORS = "rejected_indicators"
    THREAT = "threat"
    

class CreateThreatInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicators": {
      "type": "array",
      "title": "Indicators",
      "description": "Add indicators to new threat in InsightIDR. Accept IP addresses, process hashes (SHA1, MD5, SHA256), domain names, URLs",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "note_text": {
      "type": "string",
      "title": "Note Text",
      "description": "Note text of created threat",
      "default": "Threat created via InsightConnect",
      "order": 2
    },
    "threat_name": {
      "type": "string",
      "title": "Threat Name",
      "description": "Name of created threat",
      "order": 1
    }
  },
  "required": [
    "indicators",
    "threat_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateThreatOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "rejected_indicators": {
      "type": "array",
      "title": "Rejected Indicators",
      "description": "Rejected indicators in new threat",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "threat": {
      "$ref": "#/definitions/threat",
      "title": "Threat",
      "description": "The information about the new threat",
      "order": 2
    }
  },
  "required": [
    "rejected_indicators",
    "threat"
  ],
  "definitions": {
    "threat": {
      "type": "object",
      "title": "threat",
      "properties": {
        "indicator_count": {
          "type": "integer",
          "title": "Indicator Count",
          "description": "The number of indicators in this threat",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the threat",
          "order": 2
        },
        "note": {
          "type": "string",
          "title": "Note",
          "description": "Notes about this threat",
          "order": 3
        },
        "published": {
          "type": "boolean",
          "title": "Published",
          "description": "Indicates whether this threat has been published",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
