# Google Form Macro

Automatic refresh and automatic field filling for Google Forms.

### config.py

- `FORM_URL`

URL of target Google Form.

- `FIELD_VALUE`

Dictionary of known field names and values to fill.

The `key` should be a substring of the field name in the actual form.

```
FIELD_VALUE = {
    'Email': 'john@example.com',
    'Name': 'John Doe',
    'Address': 'Some City Some Street Some Apartment',
}
```
