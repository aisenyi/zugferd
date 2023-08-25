// Copyright (c) 2023, Othermo GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Zugferd Settings', {
	onload: function(frm) {
		frm.set_query("for_doctype", "default_settings", function(doc, cdt, cdn){
			return{
				"filters": {
					"name": "Sales Invoice"
				}
			}
		});
		
		frm.set_query("print_format", "default_settings", function(doc, cdt, cdn){
			return{
				"filters": {
					"doc_type": locals[cdt][cdn].for_doctype
				}
			}
		});
	}
});
