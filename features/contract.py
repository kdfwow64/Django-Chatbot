class Contract(dict):
    """Base Reply class. Initializes with content. Can post, and can format content."""
    def __init__(self, reply_content, reply_type="text", prompt_content="Type already!", prompt_type="text"):
        self["reply"] = {}
        self["reply"]["content"] = reply_content
        self["reply"]["type"] = reply_type
        self["prompt"] = {}
        self["prompt"]["content"] = prompt_content
        self["prompt"]["type"] = prompt_type
    def add(self, extra):
        self["reply"]["content"] += ("\n" + extra) if self["reply"]["content"] else extra
    def add_buttons(self, buttons):
        self["prompt"]["content"] = buttons
        self["prompt"]["type"] = "button"
    def add_image(self, image_url):
        self["reply"]['image'] = image_url
        self["reply"]["type"] = 'card'



# # This represents a reply with menu options such as museums, parks etc.
# class SlidyReply(Reply):
#     """UNTESTED!!! SlidyReply. TODO: get nice format for slidy
#     Initializes with list of ???. Post a carousel of generic templates
#     https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic#carousel
#     Each generic template will require: title, image_url, subtitle, default_action, buttons
#     """
#     #TODO: format list_of_places properly
#     def __init__(self, list_of_scrolly_pics):
#         super().__init__("", "slidy")
#         self.list_of_scrolly_pics = list_of_scrolly_pics
#     def formatter(self, fbid):
#         list_of_generic_templates = []
#         for scrolly_pic in self.list_of_scrolly_pics:
#             list_of_generic_templates.append(scrolly_pic.generic_template_formatter())
#         return json.dumps({"recipient":{"id": fbid},
#                            "message":{
#                              "attachment":{
#                                "type":"template",
#                                "payload":{
#                                  "template_type":"generic",
#                                  "elements": list_of_generic_templates
#                                }
#                              }
#                            }
#                          })
#
# class QuicksterReply(Reply):
#     """
#     Initializes with a list of quick replies. Formats list and posts quick replies
#     https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies
#     """
#     def __init__(self, content, list_of_options):
#         super().__init__(content, "quicky")
#         self.list_of_options = list_of_options
#     def formatter(self, fbid):
#         quick_replies = []
#         for text in self.list_of_options:
#             quick_replies.append({"content_type": "text",
#                                   "title": text,
#                                   "payload": text})
#         return json.dumps({"recipient":{"id":fbid},
#                            "message":{"text": self.content,
#                                       "quick_replies": quick_replies}
#                           })
#
# class ScrollyReply(Reply):
#     """
#     Initializes with a list of button replies. Formats list and posts button replies
#     https://developers.facebook.com/docs/messenger-platform/send-messages/template/button
#     """
#     def __init__(self, content, list_of_options):
#         super().__init__(content, "scrolly")
#         self.list_of_options = list_of_options
#     def formatter(self, fbid):
#         list_of_buttons = []
#         for option in self.list_of_options:
#             list_of_buttons.append({
#               "type":"postback",
#               "title":option,
#               "payload":option
#             })
#         return json.dumps({"recipient":{"id": fbid},
#                            "message":{
#                              "attachment":{
#                                "type":"template",
#                                "payload":{
#                                  "template_type":"button",
#                                  "text": self.content,
#                                  "buttons": list_of_buttons
#                                }
#                              }
#                            }
#                          })
#
# class ScrollyPicReply(Reply):
#     """
#     Initializes with a list of button replies. Formats list and posts button replies
#     https://developers.facebook.com/docs/messenger-platform/send-messages/template/button
#     """
#     def __init__(self, content, subtitle, list_of_options, image_url, did=None):
#         super().__init__(content, "scrolly")
#         self.subtitle = subtitle
#         self.list_of_options = list_of_options
#         self.image_url = image_url
#         self.did = " " + str(did) if did != None else ""
#     def generic_template_formatter(self):
#         list_of_buttons = []
#         for option in self.list_of_options:
#             list_of_buttons.append({
#               "type":"postback",
#               "title":option,
#               "payload":option + self.did
#             })
#         return { "title": self.content,
#                  "subtitle": self.subtitle,
#                  "image_url": self.image_url,
#                  "buttons": list_of_buttons
#                }
#     def formatter(self, fbid):
#         generic_template = self.generic_template_formatter()
#         return json.dumps({"recipient":{"id": fbid},
#                            "message":{
#                              "attachment":{
#                                "type":"template",
#                                "payload":{
#                                  "template_type":"generic",
#                                  "elements": [generic_template]
#                                }
#                              }
#                            }
#                          })
#
# class GiffyReply(Reply):
#     """docstring for GiffyReply."""
#     def __init__(self, content):
#         super().__init__(content, "giffy")
