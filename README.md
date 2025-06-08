A modular, cross-platform application for real-time 3D intraoral scanning, post-processing, measurement, and export. Designed for dental clinicians, laboratories, and future integration with AI diagnostics.

---

## 🚀 Features

* **Live 3D Scanning**: Captures RGB + depth streams from USB or structured-light handheld scanners
* **Real-time Reconstruction**: Generates point cloud and meshes on-the-fly
* **Smart Auto-Resume**: Continues scanning from interrupted areas without restarting
* **Mesh Processing Tools**: Includes smoothing, simplification, hole filling, trimming, color correction
* **Occlusion & Bite Scanning**: Supports occlusion modeling and bite registration
* **Interactive 3D Viewer**: Rotate, pan, zoom, and slice (axial/coronal) views
* **Measurement Tools**: Distance, angle, and volume measurements
* **Scan Completeness Heatmap**: Highlights unscanned regions during capture
* **File Export**: STL, OBJ, PLY, and DICOM formats supported
* **CAD/CAM Compatibility**: Ready for integration with common dental platforms
* **Secure Data Management**: Encrypted patient data, session history, version control, GDPR/HIPAA compliance
* **Modular, Extensible Architecture**: Easily add AI-guided margin detection or cloud integration

---

## 🧱 Architecture

```
+--------------------+        +-------------------------+        +-------------------+
| Acquisition Module | → RGB + Depth streams      | Reconstruction Engine | → Real-time 3D Model |
+--------------------+        +-------------------------+        +-------------------+
                                       ↓
                           Post-Processing Tools Module
                                       ↓
                             Interactive GUI Layer
                                       ↓
                         Export & Integration Module
                                       ↓
                      Data Management (Storage & Security)
```

---

## 💻 Tech Stack

* **Backend**:

  * C++ or Python with Open3D / PCL / OpenCV
  * Core engine handles sensor input, point cloud fusion, mesh generation

* **Frontend**:

  * Qt (C++) or Electron (JS/TS)
  * Real-time 3D rendering and UI tools

* **Communication**:

  * WebSocket or REST for scanner device connectivity

* **Data Handling**:

  * Encrypted SQLite / JSON file storage
  * Local first, optional cloud sync

* **AI Module (Optional)**:

  * ML model for margin detection & scan guidance

---

## 📦 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/sdkh732/sina.git
   cd sina
   git checkout initial-project-skeleton
   ```

2. **Install dependencies**

   * **Python backend**:

     ```bash
     pip install -r backend/requirements.txt
     ```
   * **C++ backend**

     ```bash
     mkdir build && cd build
     cmake ..
     make
     ```
   * **Frontend (Electron)**:

     ```bash
     cd frontend
     npm install
     ```

---

## 🧪 Usage Examples

* **Start backend**

  ```bash
  ./backend/run_scanner --device /dev/video0
  ```

* **Launch UI**

  ```bash
  cd frontend && npm start
  ```

* **Simulate scan (testing)**

  ```bash
  ./backend/run_scanner --simulate sample_data/
  ```

---

## 🛠️ Development Workflow

1. Create feature branch

   ```bash
   git checkout -b feature/mesh-processing
   ```

2. Code new module in `backend/src/meshing` or `frontend/src/components`

3. Add unit tests in `tests/backend` or `tests/frontend`

4. Build and run tests

   ```bash
   # Backend
   pytest tests/backend
   # Frontend
   npm test
   ```

5. Open pull request, describe changes, and assign reviewers

---

## ✅ Roadmap

* [ ] Integrate AI for margin detection and scan guidance
* [ ] Implement DICOM and PACS export
* [ ] Add cloud synchronization and multi-user support
* [ ] Extend measurement features (e.g., arch form analysis)
* [ ] Implement touch/tablet-friendly UI controls

---

## 📄 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

* **sdkh732** – Project initiator
