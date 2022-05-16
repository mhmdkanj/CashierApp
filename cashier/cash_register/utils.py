def truncate(number):
    # enough to truncate numbers up to two decimal places taking into consideration float storage errors
    return round(number, 2)


class ReceiptPrinter:
    """Utility class for pretty printing receipts."""

    template = f"""
================= RECEIPT =================
$DATETIME
-------------------------------------------
$ITEMS
___________________________________________
Sales Tax: $TOTAL_SALES_TAX
Total: $TOTAL_PRICE
===========================================
    """

    @staticmethod
    def generate_raw_receipt(receipt):
        raw_receipt = ReceiptPrinter.template.replace("$DATETIME", str(receipt.time))
        
        item_log = ''
        for item, (taxed_price, _) in receipt.get_items().items():
            item_log += f"{item} --- {taxed_price}\n"
        raw_receipt = raw_receipt.replace("$ITEMS", item_log)

        raw_receipt = raw_receipt.replace("$TOTAL_SALES_TAX", str(receipt.total_sales_tax))
        raw_receipt = raw_receipt.replace("$TOTAL_PRICE", str(receipt.total_price))
        return raw_receipt

    @staticmethod
    def print_receipt(receipt):
        print(ReceiptPrinter.generate_raw_receipt(receipt))
