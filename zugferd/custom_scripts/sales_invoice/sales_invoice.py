import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from zugferd.utils.zugferd.zugferd import create_zugferd_pdf

class CustomSalesInvoice(SalesInvoice):
	def on_submit(self):
		super(CustomSalesInvoice, self).on_submit()
		# Create zugeferd pdf and attach it to invoice
		print_format = None
		with_letterhead = 1
		settings_exist = frappe.db.exists("Zugferd Defaults", {"for_doctype": "Sales Invoice"})
		if settings_exist:
			print_format, with_letterhead = frappe.db.get_value("Zugferd Defaults", settings_exist, 
					["print_format", "with_letterhead"])
		create_zugferd_pdf(self.name, format=print_format, no_letterhead=with_letterhead)
