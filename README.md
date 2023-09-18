# fastapi_form_list_example
This example tries to resolve the question about how to deal with old-style forms using fields lists/arrays like "field[]"

## Description

Here is an approach working in FastAPI using a field-by-field and a Pydantic method.

This example reads a form sent by GET or POST in which params use the format "field[]", and the FastAPI method can process them as expected.
These kinds of fields were often used in the old school for PHP programs to be able to process a list of fields into one only field as an array which variable was named "field[]"
