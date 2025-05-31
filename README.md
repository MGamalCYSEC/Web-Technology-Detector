## Web Technology Detector

**Web Technology Detector** is a Python script designed to identify web technologies, frameworks, CMSs, and server-side software used by websites. The script analyzes the website's response content, headers, and cookies to detect technologies, then categorizes the results for easy interpretation. It supports scanning single URLs or batch URLs from a file.

### Key Features

* Detects a wide range of technologies, frameworks, CMSs, and server-side software.
* Categorizes detected technologies into meaningful groups (e.g., CMSs, Web Development Frameworks, Web Servers).
* Supports two modes of operation:

  1. **Single URL Scan**: Specify a single URL via command-line argument.
  2. **Batch URL Scan**: Provide a file containing multiple URLs.
* `--all` option to include headers and cookies in the analysis.
* Color-coded output for enhanced readability:

  * **Categories** are displayed in green.
  * **Detected Technologies** are displayed in red.

---

### Usage

#### Prerequisites

* Python 3.x
* Install required libraries:

  ```bash
  pip install requests colorama
  ```

#### Clone the Repository

```bash
git clone https://github.com/MGamalCYSEC/Web-Technology-Detector.git
```

#### Run the Script

1. **Single URL Scan**

   ```bash
   python3 detect_technologies.py -u <URL>
   ```

   Example:

   ```bash
   python3 detect_technologies.py -u http://example.com
   ```

2. **Batch URL Scan**

   ```bash
   python3 detect_technologies.py -f <file>
   ```

   Example:

   ```bash
   python3 detect_technologies.py -f urls.txt
   ```

3. **Enable Comprehensive Scanning**
   Use the `--all` option to include headers, cookies, and HTML content:

   ```bash
   python3 detect_technologies.py -u <URL> --all
   ```

   Example:

   ```bash
   python3 detect_technologies.py -f urls.txt --all
   ```

---

### Example Output

```plaintext
Scanning http://example.com...
Technologies detected on http://example.com:
  Web Development Frameworks: Laravel
  Web Servers: Apache
```
