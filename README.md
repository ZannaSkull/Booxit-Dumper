# Booxit Fetcher

<p align="center">
<img src="https://i.pinimg.com/736x/4c/51/f8/4c51f8640950dc3d12dcbe0ef1bdec80.jpg", width="500", height="500">
</p>



## Description
The **Booxit Fetcher** is a Python script designed to retrieve order details from the Booxit website. It utilizes multithreading to efficiently fetch data for a range of order numbers, extract relevant information, and save it to a text file.

## Features
- Fetches order details concurrently using threading.
- Extracts specific information such as name, phone number, address, and notes.
- Saves the fetched data into a text file (`dati.txt`).
- Displays a colorful banner in the console.

## Requirements
- Python 3.x
- Pip

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pystyle etc
