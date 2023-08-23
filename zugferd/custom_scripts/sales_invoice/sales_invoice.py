import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from zugferd.utils.zugferd.zugferd import create_zugferd_pdf

class CustomSalesInvoice(SalesInvoice):
	def on_submit(self):
		super(CustomSalesInvoice, self).on_submit()
		# Create zugeferd pdf and attach it to invoice
		create_zugferd_pdf(self.name)
