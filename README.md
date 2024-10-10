
# altFreme

altFreme is a small Python application that creates two small transparent dots on your screen, which change color when you press the `Alt` and `Shift` keys. The dots are positioned at the top-right corner of your screen and stay always on top of other windows.

## Features
- **Transparent Background:** The dots are transparent and blend into the background when inactive.
- **Color Change:** The top dot turns red when the `Alt` key is pressed, and the bottom dot turns green when the `Shift` key is pressed.
- **Lightweight:** The application is designed to be lightweight and runs in the background without interrupting your workflow.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.7+
- Required Python packages:
  ```bash
  pip install tkinter keyboard screeninfo
  ```
  If you don't have these packages installed, you can install them using:
  ```bash
  pip install keyboard screeninfo
  ```

### Running the Application
To run the Python script directly:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/altFreme.git
   cd altFreme
   ```

2. Run the application:
   ```bash
   python altFreme.py
   ```

### Building the Executable
If you want to build an `.exe` file for Windows:
1. Make sure you have `PyInstaller` installed:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole altFreme.py
   ```

3. The executable file will be located in the `dist` folder.

### Auto-Start on Windows
To ensure the application runs automatically when you start your Windows machine, add the executable file to your Startup folder:
1. Press `Win + R`, type `shell:startup`, and hit Enter.
2. Copy the generated `.exe` file into this folder.

## Repository Structure
```
/altFreme
│
├── dist/                   # Folder containing the built .exe file
├── src/                    # Folder containing the source code
│   └── altFreme.py         # Main application script
├── README.md               # Project documentation
└── requirements.txt        # List of required Python packages
```

## Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Special thanks to the Python community for providing useful libraries.
- Created with ❤️ by [Mohammad Rahimi](https://github.com/your-username)
