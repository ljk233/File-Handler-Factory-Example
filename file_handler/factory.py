"""factory.py
"""

import abc
import csv


class Handler(abc.ABC):
    """Abstract base class for file handlers.

    Subclasses must implement the load and save methods.
    """

    @abc.abstractmethod
    def load(self, file_path, *args, **kwargs):
        """Abstract method to load data from a file.

        Args:
            file_path (str): The path to the file to be loaded.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, file_path, data, *args, **kwargs):
        """Abstract method to save data to a file.

        Args:
            file_path (str): The path to the file to which data will be
            saved.
            data: The data to be saved.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Raises:
            NotImplementedError: This method must be implemented by
            subclasses.
        """
        raise NotImplementedError


class CSVHandler(Handler):
    """Handler class for CSV files."""

    def load(self, file_path, delimiter=","):
        """Load data from a CSV file.

        Args:
            file_path (str): The path to the CSV file to be loaded.
            delimiter (str, optional): The delimiter used in the CSV file.
            Default is ",".

        Returns:
            list: A list of lists representing the CSV data.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(file_path, "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=delimiter)
                data = [row for row in reader]
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {file_path}")

    def save(self, file_path, data, delimiter=","):
        """Save data to a CSV file.

        Args:
            file_path (str): The path to the CSV file where data will be
            saved.
            data (list): A list of lists representing the data to be
            saved.
            delimiter (str, optional): The delimiter to be used in the
            CSV file. Default is ",".
        """
        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=delimiter)
            writer.writerows(data)


# Dictionary mapping data source to handler class
HANDLER_CLASSES = {
    "csv": CSVHandler,
    # "json": handlers.json_handler.JSONHandler(),
    # "toml": handlers.toml_handler.TOMLHandler(),
    # Add more entries for other handler classes as needed
}


def create_handler(data_source: str) -> Handler:
    """Create an instance of a file handler based on the specified data
    source.

    Args:
        data_source (str): The data source for which to create a file
        handler.

    Returns:
        Handler: An instance of the file handler class.

    Raises:
        ValueError: If the specified data source is not supported.
    """
    handler_class = HANDLER_CLASSES.get(data_source)

    if handler_class:
        return handler_class()
    else:
        raise ValueError(f"Unsupported data source: {data_source}")
