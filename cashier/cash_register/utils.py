from cashier.cash_register.register import Receipt

class ReceiptPrinter:
    template = f"""
    ================= RECEIPT =================
    $DATETIME
    -------------------------------------------
    $ITEMS
    ___________________________________________
    $TOTAL_SALES_TAX
    $TOTAL_PRICE
    ===========================================
    """

    @staticmethod
    def generate_raw_receipt(receipt: Receipt):
        raw_receipt = ReceiptPrinter.template.replace("$DATETIME", receipt.time)
        
        item_log = ''
        for item, (taxed_price, _) in receipt.get_items().items():
            item_log += f"{item} --- {taxed_price}\n"
        raw_receipt = raw_receipt.replace("$ITEMS", item_log)

        raw_receipt = raw_receipt.replace("$TOTAL_SALES_TAX", receipt.total_sales_tax)
        raw_receipt = raw_receipt.replace("$TOTAL_PRICE", receipt.total_price)
        return raw_receipt

    @staticmethod
    def print_receipt(receipt):
        print(ReceiptPrinter.generate_raw_receipt(receipt))
