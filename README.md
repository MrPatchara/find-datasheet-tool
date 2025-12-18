# 📄 Datasheet Viewer Tool

A powerful and user-friendly desktop application for managing and accessing electronic component datasheets. Built with Python and Tkinter, this tool helps engineers, hobbyists, and students efficiently organize, search, and access datasheets both locally and online.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ✨ Features

### 🔍 **Search Capabilities**
- **Online Search**: Quickly search for datasheets on DatasheetArchive.com
- **Local Database Search**: Search through your saved datasheets by name
- **Type Filtering**: Filter datasheets by component type (IC, Transistor, Resistor, Capacitor, Diode, Other)

### 💾 **Database Management**
- **Add Datasheets**: Store local PDF datasheets with custom names and types
- **Edit Entries**: Update datasheet names and types
- **Remove Entries**: Delete datasheets from your database
- **View Details**: Display complete information about any datasheet

### 🎯 **User-Friendly Interface**
- Clean and intuitive GUI built with Tkinter
- Easy-to-use menu system
- Organized layout with clear sections
- Quick access buttons for common operations

### 📂 **File Management**
- Open local datasheet files directly from the application
- Support for PDF files
- Automatic file path management

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MrPatchara/find-datasheet-tool.git
   cd find-datasheet-tool
   ```

2. **Navigate to the application directory**
   ```bash
   cd Datasheet_viewer
   ```

3. **Run the application**
   ```bash
   python Find-Datasheet.py
   ```

### First Run

On first launch, the application will automatically create a SQLite database (`datasheets.db`) in the same directory to store your datasheet information.

## 📖 Usage Guide

### Searching for Datasheets Online

1. Enter the component name in the "Name" field
2. Click **"Search Online"** to open the component's datasheet page on DatasheetArchive.com

### Adding a Datasheet to Database

1. Enter the component name in the "Name" field
2. Select the component type from the dropdown menu
3. Click **"Add to Database"**
4. Select the PDF file from your computer
5. The datasheet will be added to your local database

### Opening a Local Datasheet

1. Select a datasheet from the list
2. Click **"Open Local"** to open the file in your default PDF viewer

### Searching in Local Database

1. Enter a keyword in the "Search in Database" field
2. Click **"Search"** to filter the list by matching names

### Filtering by Type

1. Select a component type from the "Filter by Type" dropdown
2. Click **"Filter"** to show only datasheets of that type
3. Select "All" to show all datasheets

### Editing a Datasheet Entry

1. Select a datasheet from the list
2. Click **"Edit Selected"**
3. Modify the name and/or type in the popup window
4. Click **"Save Changes"**

### Removing a Datasheet

1. Select a datasheet from the list
2. Click **"Remove from Database"**
3. The entry will be removed from your database (the file itself is not deleted)

### Viewing Datasheet Details

1. Select a datasheet from the list
2. Click **"View Details"** to see complete information including ID, name, type, and file path

## 📁 Project Structure

```
find-datasheet-tool/
│
├── Datasheet_viewer/
│   ├── Find-Datasheet.py    # Main application file
│   ├── datasheets.db         # SQLite database (created automatically)
│   └── icon.ico              # Application icon
│
├── README.md                 # This file
└── LICENSE                   # MIT License
```

## 🛠️ Technical Details

### Database Schema

The application uses SQLite with the following schema:

```sql
CREATE TABLE datasheets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    filepath TEXT NOT NULL
)
```

### Component Types

The application supports the following component types:
- IC (Integrated Circuit)
- Transistor
- Resistor
- Capacitor
- Diode
- Other

### Dependencies

- **tkinter**: GUI framework (included with Python)
- **sqlite3**: Database management (included with Python)
- **webbrowser**: Opening web pages (included with Python)

No external packages required! The application uses only Python standard library modules.

## 🎨 Screenshots

_Add screenshots of your application here to showcase the interface_

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add support for more file formats
- Implement export/import functionality
- Add tags or categories
- Improve UI/UX design
- Add keyboard shortcuts
- Implement batch operations
- Add data backup/restore features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Patchara Al-umaree**

- Email: Patcharaalumaree@gmail.com
- GitHub: [@MrPatchara](https://github.com/MrPatchara)

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Uses SQLite for lightweight database management
- DatasheetArchive.com for online datasheet search functionality

## 📧 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/MrPatchara/find-datasheet-tool/issues) page
2. Create a new issue with detailed information
3. Contact the developer via email: Patcharaalumaree@gmail.com

## 🔮 Future Enhancements

- [ ] Dark mode support
- [ ] Cloud sync functionality
- [ ] Advanced search with multiple criteria
- [ ] PDF preview within the application
- [ ] Batch import/export features
- [ ] Custom tags and categories
- [ ] Statistics and analytics
- [ ] Multi-language support

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
