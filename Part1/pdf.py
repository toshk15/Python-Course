import fitz

# Path of the PDF file
input_file = r"a.pdf"

# Path for the output PDF file
output_file = r"b.pdf"

# Opening the PDF file and creating a handle for it
file_handle = fitz.open(input_file)

# The index (page no.) from where the pages are to be deleted
start = 13

# The index to which the pages are to be deleted
end = 155

# Passing the start & end index as arguments
file_handle.delete_pages(start, end)

# Saving the file
file_handle.save(output_file)