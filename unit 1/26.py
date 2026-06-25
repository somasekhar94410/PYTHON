bill_amount = float(input("Enter Original Bill Amount: "))
gst_percentage = float(input("Enter GST Percentage: "))

gst_amount = (bill_amount * gst_percentage) / 100
final_bill = bill_amount + gst_amount

print("GST Amount =", gst_amount)
print("Final Bill Amount =", final_bill)