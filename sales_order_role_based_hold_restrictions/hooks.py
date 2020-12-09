# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sales_order_role_based_hold_restrictions"
app_title = "Sales Order Role Based Hold Restrictions"
app_publisher = "Firsterp"
app_description = "Sales Order Role Based Hold Restrictions"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@firsterp.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sales_order_role_based_hold_restrictions/css/sales_order_role_based_hold_restrictions.css"
# app_include_js = "/assets/sales_order_role_based_hold_restrictions/js/hold_permission.js"

# include js, css files in header of web template
# web_include_css = "/assets/sales_order_role_based_hold_restrictions/css/sales_order_role_based_hold_restrictions.css"
# web_include_js = "/assets/sales_order_role_based_hold_restrictions/js/sales_order_role_based_hold_restrictions.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Sales Order" : "public/js/sales_order.js"}
doctype_js = {"Purchase Order" : "public/js/purchase_order.js"}
doctype_js = {"Sales Invoice" : "public/js/sales_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sales_order_role_based_hold_restrictions.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sales_order_role_based_hold_restrictions.install.before_install"
# after_install = "sales_order_role_based_hold_restrictions.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sales_order_role_based_hold_restrictions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sales_order_role_based_hold_restrictions.tasks.all"
# 	],
# 	"daily": [
# 		"sales_order_role_based_hold_restrictions.tasks.daily"
# 	],
# 	"hourly": [
# 		"sales_order_role_based_hold_restrictions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sales_order_role_based_hold_restrictions.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sales_order_role_based_hold_restrictions.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sales_order_role_based_hold_restrictions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sales_order_role_based_hold_restrictions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sales_order_role_based_hold_restrictions.task.get_dashboard_data"
# }

