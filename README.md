
# File Handler Factory Example

This repository showcases a simple yet extensible file handling system implemented in Python.
The primary purpose of the file handler is to provide a flexible solution for loading and saving data from various file formats.
The implementation adheres to the **Factory** design pattern, allowing users to seamlessly switch between different file handlers based on their specific data sources.

## Project Structure

```plaintext
File-Handler-Factory-Example/
|--- file_handler/   # Source code directory.
|    |-- init.py
|    |-- factory.py  # Implementation of the file handler factory.
|--- .gitignore
|--- README.md
```

## Usage

The file handler factory allows you to create instances of file handlers based on the specified data source.

```python
from file_handler.factory import create_handler

# Example: Create a CSV file handler
handler = create_handler("csv")
handler.load("path/to/example.csv")
```

## Extending the module

To add a handler for a specific file type, follow these steps:

**(1)** Import any required modules.

Import any additional packages or modules into `factory.py`.

```python
# factory.py

# Existing imports ...

# Import additional packages or modules.
import json
```

**(2)** Implement the New Handler.

- Implement the new handler class.
- Inherit from the Handler abstract base class.
- Override the load and save methods.

```python
# factory.py

# Existing implementations ...

class JSONHandler(Handler):
    def load(self, file_path):
        # Implementation for loading JSON data

    def save(self, file_path, data):
        # Implementation for saving data to a JSON file
```

**(3)** Update the `HANDLER_CLASSES` dictionary.

```python
# factory.py

HANDLER_CLASSES = {
    # Exisiting entries ...
    "json": JSONHandler,
}
```

We should now be able to create a file handler for JSON files.

```python
# example_json.py

from file_handler.factory import create_handler


# Example: Create a JSON file handler
json_handler = create_handler("json")
json_handler.load("path/to/example.json")
```

## Contributing

If you find issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
