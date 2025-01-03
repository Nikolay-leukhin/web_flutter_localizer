# CSV Localizer Web Application

This project is a web application built with Flask that allows users to upload CSV files and generate localization files (.arb) for various languages. Users can download the generated files directly from the web interface.

## Features

- Upload CSV files containing localization data.
- Specify the key column used for localization keys.
- Generate `.arb` files for all available languages in the CSV file.
- Download generated `.arb` files via the web interface.
- Clean and user-friendly UI with a responsive design.

## Project Structure

```
project/
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template for the web interface
├── static/
│   └── css/
│       └── styles.css  # CSS styles for the UI
├── uploads/            # Directory for uploaded CSV files
├── outputs/            # Directory for generated localization files
```

## Requirements

- Python 3.7+
- Flask
- pandas

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/csv-localizer.git
   cd csv-localizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. Upload a CSV file with the following structure:
   - One column for localization keys (e.g., `keyname`).
   - Additional columns for each language (e.g., `en`, `fr`, `de`).

4. Enter the name of the key column (e.g., `keyname`) and click "Generate Localization Files".

5. Download the generated `.arb` files from the provided links.

## Example CSV File Format

| keyname   | en          | fr           | de           |
|-----------|-------------|--------------|--------------|
| greeting  | Hello       | Bonjour      | Hallo        |
| farewell  | Goodbye     | Au revoir    | Auf Wiedersehen |

## Notes

- Ensure that the uploaded CSV file has a valid format.
- The generated files will be available in the `outputs/` directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bug reports.

