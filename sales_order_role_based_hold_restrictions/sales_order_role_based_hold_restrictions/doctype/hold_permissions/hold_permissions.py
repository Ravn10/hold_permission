# -*- coding: utf-8 -*-
# Copyright (c) 2020, Firsterp and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class HoldPermissions(Document):
	def autoname(self):
		name = self.document

@frappe.whitelist()
def get_roles(docname):
	roles = frappe.get_all("Role List",filters={"parenttype":"Hold Permissions","parent":docname},fields=["role"])
	role_list = []
	for role in roles:
		role_list.append(role.role)
	
	return role_list
		