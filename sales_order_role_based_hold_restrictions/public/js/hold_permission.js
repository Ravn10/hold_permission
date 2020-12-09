
frappe.ui.form.on("Sales Order",{
    refresh:function(frm){
        frappe.call({
            method:"sales_order_role_based_hold_restrictions.sales_order_role_based_hold_restrictions.doctype.hold_permissions.hold_permissions.get_roles",
            args:{"docname":frm.doctype},
            callback:function(r){
                console.log(r.message)
                if(r.message){
                    if((flt(doc.per_delivered, 6) < 100 || flt(doc.per_billed) < 100) && has_common(frappe.user_roles, r.message)) {
							// hold
							this.frm.remove_custom_button(__('Hold'), __("Status"))
                            // close
                            this.frm.remove_custom_button(__('Close'), __("Status"))
						}
                }
            }
        })
     }
    }
)

frappe.ui.form.on("Sales Invoice",{
    refresh:function(frm){
        frappe.call({
            method:"sales_order_role_based_hold_restrictions.sales_order_role_based_hold_restrictions.doctype.hold_permissions.hold_permissions.get_roles",
            args:{"docname":frm.doctype},
            callback:function(r){
                if(r.message){
                    console.log(r.message)
                    if((flt(doc.per_delivered, 6) < 100 || flt(doc.per_billed) < 100) && has_common(frappe.user_roles, r.message)) {
							// hold
							this.frm.remove_custom_button(__('Hold'), __("Status"))
                            // close
                            this.frm.remove_custom_button(__('Close'), __("Status"))
						}
                }
            }
        })
     }
    }
)

frappe.ui.form.on("Purchase Order",{
    refresh:function(frm){
        frappe.call({
            method:"sales_order_role_based_hold_restrictions.sales_order_role_based_hold_restrictions.doctype.hold_permissions.hold_permissions.get_roles",
            args:{"docname":frm.doctype},
            callback:function(r){
                if(r.message){
                    console.log(r.message)
                    if((flt(doc.per_delivered, 6) < 100 || flt(doc.per_billed) < 100) && has_common(frappe.user_roles, r.message)) {
							// hold
							this.frm.remove_custom_button(__('Hold'), __("Status"))
                            // close
                            this.frm.remove_custom_button(__('Close'), __("Status"))
						}
                }
            }
        })
     }
    }
)