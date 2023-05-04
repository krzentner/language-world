

and implement the task following the structure of the other examples.
"""
[eod] [code]# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.win_browser_history_object as win_browser_history_binding
from cybox.common import Time


class _HistoryItemListTypeField(entities.EntityList):
    _binding = win_browser_history_binding
    _binding_class = win_browser_history_binding.HistoryItemListType
    history_item = fields.TypedField("History_Item", HistoryItem)


class _CookieEntryListTypeField(entities.EntityList):
    _binding = win_browser_history_binding
    _binding_class = win_browser_history_binding.CookieEntryListType
    cookie_entry = fields.TypedField("Cookie_Entry", CookieEntry)


class HistoryItem(entities.Entity):
    _binding = win_browser_history_binding
    _binding_class = win_browser_history_binding.HistoryItemType

    def __init__(self):
        super(HistoryItem, self).__init__()
        self.url = None
        self.time = None
        self.number_of_hits = None
        self.cookie_count = None
        self.window_title = None

    url = fields.TypedField("Url", str)
    time = fields.TypedField("Time", Time)
    number_of_hits = fields.TypedField("Number_Of_Hits", int)
    cookie_count = fields.TypedField("Cookie_Count", int)
    window_title = fields.TypedField("Window_Title", str)


class CookieEntry(entities.Entity):
    _binding = win_browser_history_binding
    _binding_class = win_browser_history_binding.CookieEntryType

    def __init__(self):
        super(CookieEntry, self).__init__()
        self.name = None
        self.content = None
        self.expires = None
        self.last_accessed = None
        self.creation_time = None

    name = fields.TypedField("Name", str)
    content = fields.TypedField("Content", str)
    expires = fields.TypedField("Expires", Time)
    last_accessed = fields.TypedField("Last_Accessed", Time)
    creation_time = fields.TypedField("Creation_Time", Time