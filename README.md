# MaxTracker

MaxTracker is a Python program designed to efficiently archive and compress files on Windows systems. By compressing files, it helps in saving disk space and improving load times for data retrieval. This is especially useful for systems with limited storage or when dealing with large volumes of data.

## Features

- Archive files from a specified source directory.
- Save the compressed files into a specified archive directory.
- Automatically generates unique archive names based on the current timestamp.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Make sure you have Python 3.x installed on your Windows machine. If not, download and install it from the [official Python website](https://www.python.org/downloads/).
2. Clone or download the repository to your local machine.

## Usage

1. Open a command prompt or terminal window.
2. Navigate to the directory where `max_tracker.py` is located.
3. Run the script using the following command:
    ```bash
    python max_tracker.py
    ```
4. Follow the on-screen prompts to input the source folder and the archive folder paths.

## Example

Suppose you have a folder `C:\Data` with files you want to compress and save the archive to `C:\Archives`. 

- When prompted, enter `C:\Data` as the source folder.
- Enter `C:\Archives` as the archive folder.

The program will create a compressed archive in the `C:\Archives` directory with a unique name based on the current date and time.

## Contributing

If you want to contribute to MaxTracker, feel free to fork the repository and submit a pull request. You can also report issues or suggest features via the issue tracker.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.