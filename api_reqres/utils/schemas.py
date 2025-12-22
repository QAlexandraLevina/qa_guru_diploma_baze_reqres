post_user_create_schema = {
 "type": "object",
  "additionalProperties": False,
 "properties": {
 "name": {
 "type": "string"
 },
 "job": {
 "type": "string"
 },
 "id": {
 "type": "string"
 },
 "createdAt": {
 "type": "string"
 }
 },
 "required": [
 "name",
 "job",
 "id",
 "createdAt"
 ]
}


get_single_user_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "avatar": {"type": "string"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        },
        "_meta": {
            "type": "object",
            "properties": {
                "powered_by": {"type": "string"},
                "upgrade_url": {"type": "string"},
                "docs_url": {"type": "string"},
                "template_gallery": {"type": "string"},
                "message": {"type": "string"},
                "features": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "upgrade_cta": {"type": "string"}
            },
            "required": [
                "powered_by", "upgrade_url", "docs_url", "template_gallery",
                "message", "features", "upgrade_cta"
            ]
        }
    },
    "required": ["data", "support", "_meta"]
}


put_update_user_schema = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "updatedAt"
  ]
}


patch_update_user_schema = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "updatedAt"
  ]
}


post_unsuccessful_login_schema = {
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}