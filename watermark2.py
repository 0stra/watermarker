import PyPDF2
# use reader to open the file on which u want to add the watermarker -> wtr.pdf reader -> 'rb'
template = PyPDF2.PdfFileReader(open('sample.pdf', 'rb'))
# use reader to open the watermarker that u want on the sample.pdf reader -> 'rb'
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# write thw output with writer to create object in memory
output = PyPDF2.PdfFileWriter()
# loop through the pages and withe help of getNumpages  it will tell us that how many pages does the template has
for i in range(template.getNumPages()):
# create a object
    page = template.getPage(i)
# merge the template(page) with the watermarker page with the help os mergepage
    page.mergePage(watermark.getPage(0))
# for output
    output.addPage(page)
# new name of the watermarked file -> 'watermarked_output and we write the output -> 'wb'
    with open('watermark_output.pdf', 'wb') as file:
        output.write(file)
