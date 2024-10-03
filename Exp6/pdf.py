import csv
import PyPDF2
from datetime import date

with open("orders.csv", "r") as f:
    csv_reader = csv.DictReader(f) 
    mergeFile = PyPDF2.PdfMerger()

    for row in csv_reader:
        total = int(row['Quantity']) * int(row['Unit Price'])

        writer = PyPDF2.PdfWriter()
        writer.add_blank_page(600.0, 600.0)

        annotation = PyPDF2.generic.AnnotationBuilder.free_text(
            f"Invoice No.: {row['Order ID']}\nDate of Purchase: {date.today()}\nCustomer Name: {row['Customer Name']}\nProduct Name: {row['Product Name']}\nQuantity: {row['Quantity']}\nUnit Price: {row['Unit Price']}\nTotal Amount: {total}\n",
            rect=(500, 500, 100, 50), 
        )
        writer.add_annotation(page_number=0, annotation=annotation)

        with open(row['Order ID'] + ".pdf", 'wb+') as pdf_file:
            writer.write(pdf_file)
            mergeFile.append(pdf_file)

mergeFile.write("Merged_File.pdf")
